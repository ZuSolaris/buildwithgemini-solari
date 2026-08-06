# ✨ Solari // Cosmic Sarcastic Diagnostics

> "Your telemetry has arrived. It's aggressively mediocre, just like your sleep hygiene."

**Solari** is a high-fidelity, futuristic AI agent designed with an ultra-premium, dark-cyberpunk purple aesthetic. Created by an Interaction Design student, it bridges the gap between state-of-the-art AI tooling and gorgeous, sensory-rich human-computer interaction (HCI).

Solari functions as a sarcastic morning synopsis assistant. It analyzes your wake-up time and self-reported energy levels to deliver wit-infused daily diagnostics, roasts, and productivity tips.

---

## 🎨 Interaction Design Highlights

Designed from the ground up to wow users at first glance, the dashboard incorporates modern AI design trends:
- **Neon-Purple Cosmic Palette**: Built on deep obsidian bases (`#05030f`) with glowing amethyst, vibrant cyber-pink, and starry blue gradient overlays.
- **Glassmorphic Panels**: High-end frosted glass panes (`backdrop-filter: blur(25px)`) with razor-sharp neon borders to give depth and contrast.
- **Active Morphing Shapes**: Fluid SVG shapes animating smoothly in the header.
- **Micro-Animations & Feedback**: Hover transitions on interactive scale selectors, active scaling, typing bubbles, and neon pulsed states.
- **Split-Pane Layout**: An intuitive split layout showing telemetry input/diagnostics on the left and a continuous, responsive conversation workspace on the right.

---

## 🛠️ Technology Stack

- **Engine**: Gemini LLM via the Google Agent Development Kit (ADK)
- **Framework**: Python FastAPI
- **Server**: Standalone ASGI Uvicorn gateway (bound to `0.0.0.0` on port `8080` for cloud connectivity)
- **Frontend**: Vanilla HTML5 / Modern CSS (Custom Design System) / JavaScript (Asynchronous client API integration)

---

## 📂 Project Structure

```text
solari/
├── app/
│   ├── agent.py               # Solari's sarcastic instructions & tool definitions
│   ├── custom_web_server.py   # Standalone web gateway (serves UI & hosts API)
│   ├── fast_api_app.py        # Default ADK backend definition
│   └── static/
│       └── index.html         # The premium, purple cyberpunk dashboard UI
├── GEMINI.md                  # Development guide & system context
├── pyproject.toml             # Python dependency manifest
└── uv.lock                    # Dependency lockfile
```

---

## 🚀 Quick Start (Running Locally)

Get the project running on your machine in seconds:

### 1. Install Dependencies
Make sure you have [uv](https://docs.astral.sh/uv/) installed, then run:
```bash
uv pip install -r pyproject.toml
```

### 2. Configure Your Gemini Key
Create a `.env` file in the project root and add your Gemini API Key:
```text
GEMINI_API_KEY=your_api_key_here
```

### 3. Launch the Cosmic Dashboard
Run the standalone custom server:
```bash
uv run python -m app.custom_web_server
```

### 4. Experience Solari
Open your browser and navigate to:
👉 **[http://localhost:8080](http://localhost:8080)**

---

## 🤖 Solari's Core Agent Design

Solari is built using a custom system instruction prompt that infuses it with a dry, humorous, and highly sarcastic personality. It leverages a custom tool function `analyze_morning_analytics` which handles raw numeric ratings (1–5) and maps them to specialized diagnostic classes (Zombie, Sleepy, Mediocre, Decent, Stellar) before applying Gemini's reasoning to roast your morning.
