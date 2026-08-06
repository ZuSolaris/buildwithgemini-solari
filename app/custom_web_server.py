import os
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load env variables before importing agent
load_dotenv()

from app.agent import app as adk_app
from google.adk.runners import Runner
from app.app_utils import services

app = FastAPI(title="Solari Cosmic Web UI")

# Support CORS for local development environments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize standard ADK runner
runner = Runner(
    app=adk_app,
    session_service=services.get_session_service(),
    artifact_service=services.get_artifact_service(),
    auto_create_session=True,
)

@app.post("/run")
async def run_agent(req: Request):
    try:
        body = await req.json()
        prompt = body.get("newMessage", {}).get("parts", [{}])[0].get("text", "")
        session_id = body.get("sessionId") or str(uuid.uuid4())
        
        # Execute the ADK agent synchronously or asynchronously via runner
        result_events = []
        async for event in runner.run_async(prompt=prompt, session_id=session_id):
            result_events.append(event)
        
        # Serialize the standard ADK/Gemini response structures
        serialized_events = []
        for e in result_events:
            try:
                if hasattr(e, "model_dump"):
                    serialized_events.append(e.model_dump())
                elif hasattr(e, "to_dict"):
                    serialized_events.append(e.to_dict())
                else:
                    serialized_events.append(e)
            except Exception:
                serialized_events.append(str(e))
                
        return JSONResponse(serialized_events)
    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error: {str(exc)}"}
        )

# Serve our gorgeous custom static files
AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(AGENT_DIR, "app", "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Bind to 0.0.0.0 for external port accessibility in Cloud environments
    uvicorn.run(app, host="0.0.0.0", port=8080)
