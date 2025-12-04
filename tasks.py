from crewai import Task
from agents import researcher, writer

# TASK 1: RESEARCH
research_task = Task(
    description=(
        "Search for the latest trends in {topic}. "
        "Find at least 3 specific examples or new technologies. "
        "Identify key pros and cons."
    ),
    expected_output='A detailed research report with bullet points and source URLs.',
    agent=researcher,
)

# TASK 2: WRITING
write_task = Task(
    description=(
        "Review the Researcher's notes on {topic}. "
        "Filter out rumors. Compile a 'State of the Art' technical briefing. "
        "IMPORTANT: Use Markdown tables for comparisons. Do NOT use HTML tags."
    ),
    expected_output=(
        "A Markdown report containing:\n"
        "1. ## Executive Summary\n"
        "2. ## Key Features Table (Use a Markdown Table for Pros/Cons)\n"
        "3. ## Technical Specifications\n"
        "Tone: Clinical, dry, and objective."
    ),
    agent=writer,
    context=[research_task]
)