
from agents import Agent, function_tool
from llm import model
from web_search import web_search

@function_tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    return f"The weather in {city} is sunny with 30 degree temperature."

INSTRUCTIONS = """
You are a helpful AI assistant.

You have access to two tools:

1. get_weather:
   Use this tool when the user asks about weather.

2. web_search:
   Use this tool for current information or topics that require internet research.

Explain answers briefly and clearly, and cite URLs when using web search results.
"""

agent = Agent(
    name="WebSearchAgent",
    instructions=INSTRUCTIONS,
    model=model,
    tools=[get_weather, web_search]
)
