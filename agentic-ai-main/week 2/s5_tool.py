
from agents import Agent, function_tool
from llm import model

@function_tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    return f"The weather in {city} is sunny with 30 degree temperature."

INSTRUCTIONS = """
You are a helpful AI assistant.
You can use tools to answer user questions.
If user asks about weather, use the get_weather tool.
Explain answers briefly.
"""

agent = Agent(
    name="ToolAgent",
    instructions=INSTRUCTIONS,
    model=model,
    tools=[get_weather]
)
