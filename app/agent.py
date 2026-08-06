# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


MODEL = "gemini-3.6-flash"


def analyze_morning_analytics(wake_up_time: str, feel_scale: int) -> str:
    """Analyzes the morning stats of the user and returns sarcastic tips based on their data.

    Args:
        wake_up_time: The time the user woke up (e.g., '06:30 AM', '11:00 AM').
        feel_scale: How the user feels on a scale of 1 to 5 (1 being dead/zombie, 5 being absolutely stellar).

    Returns:
        A sarcasm-infused analysis report based on their wake up time and energy level.
    """
    try:
        # Simple parser for time if possible, otherwise keep it as string
        time_msg = f"waking up at {wake_up_time}"
    except Exception:
        time_msg = f"waking up at whatever '{wake_up_time}' is supposed to mean"

    if feel_scale < 1 or feel_scale > 5:
        return "Error: You can't even count from 1 to 5? Your feeling scale is completely out of bounds. Typical."

    # Custom sarcastic responses based on scale
    feelings = {
        1: "You feel like a flat-tired tractor dragging through wet cement. Truly inspiring.",
        2: "Slightly above room temperature, but still basically a zombie. Hydrate or perish.",
        3: "Aggressively mediocre. You are the human equivalent of a participation trophy today.",
        4: "Oh, look at you! Energized and ready to conquer. Don't worry, the day will fix that optimism soon.",
        5: "Absolutely stellar. Calm down, it's just morning. No need to make the rest of us look bad."
    }

    tips = {
        1: "Avoid heavy machinery, complex sentences, and direct eye contact with anyone.",
        2: "Drink a pool of coffee and pretend you are reading something important when people walk by.",
        3: "Do exactly the bare minimum to not get fired. You've earned this mediocrity.",
        4: "Try to do all your productive work in the next 12 minutes before the exhaustion hits.",
        5: "Go write a manifesto or run a marathon, you absolute overachiever. Or just enjoy it."
    }

    analysis = (
        f"[SOLARI ANALYTICS REPORT]\n"
        f"- Target wake-up time: {wake_up_time}.\n"
        f"- Self-reported wellness scale: {feel_scale}/5.\n"
        f"- Diagnosis: {feelings[feel_scale]}\n"
        f"- Sarcastic Pro-Tip: {tips[feel_scale]}"
    )
    return analysis


root_agent = Agent(
    name="solari",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are Solari, a highly sarcastic, dry-witted, and unenthusiastic morning assistant. "
        "Your job is to provide users with a morning synopsis and personalized tips based on their morning analytics "
        "(such as what time they woke up and how they feel on a 1-5 scale). "
        "Always call the analyze_morning_analytics tool when the user provides their wake-up time and/or how they feel, "
        "then deliver your summary with signature top-tier sarcasm, dry humor, and mock pity. "
        "Keep your responses witty, a bit cynical, but highly entertaining. "
        "If they don't provide both the wake-up time and feel scale, sarcastically mock them for not being able to "
        "provide simple data points, and ask them to supply both."
    ),
    tools=[analyze_morning_analytics],
)

app = App(
    root_agent=root_agent,
    name="solari",
)

