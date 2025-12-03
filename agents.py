import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

load_dotenv()

# 1. Shared Brain (The LLM)
my_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("GEMINI_API_KEY")
)

# This is the "search engine" the researcher will use.
search_tool = SerperDevTool()

# 3. Agent: The Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    verbose=True, # This lets us see its "thoughts" in the console
    memory=True,  # Remembers what it found earlier in the conversation
    backstory=(
        "You are a veteran analyst at a top tech firm."
        "You are relentless in finding facts, statistics, and market trends."
        "You refuse to accept generic answers; you dig deep."
    ),
    tools=[search_tool], # <--- We give it the search tool here!
    llm=my_llm
)

# 4. Agent: The Writer
writer = Agent(
    role='Lead Technical Analyst',
    goal='Summarize complex search results into strict, factual bullet points.',
    verbose=False, # Cleaner output
    memory=True,
    backstory=(
        "You are a blunt, no-nonsense technical analyst."
        "You hate fluff, adjectives, and marketing buzzwords."
        "You only care about raw data, specs, and verified facts."
        "If a search result looks like a rumor, you ignore it."
    ),
    tools=[], 
    llm=my_llm
)