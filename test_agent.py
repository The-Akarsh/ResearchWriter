import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# 1. Load Environment Variables
# This looks for the .env file and loads the keys so Python can see them.
load_dotenv()

# 2. Define the Brain (LLM)
# We need to explicitly tell CrewAI to use Gemini.
# If we didn't do this, it might try to look for OpenAI by default.
my_llm = LLM(
    model=os.getenv("MODEL"),           # <--- Change this line!
    api_key=os.getenv("GEMINI_API_KEY")
)

# 3. Define the Agent
# Think of an Agent as a digital employee with a specific job.
intern_agent = Agent(
    role='Intern',
    goal='Learn about AI',
    backstory='You are a curious intern eager to learn new concepts.',
    llm=my_llm,  # We give the agent the Gemini brain we defined above
    verbose=True # This lets us see the agent's "thinking" process in the consolet
)

# 4. Define the Task
# A Task is a specific assignment we give to an Agent.
learning_task = Task(
    description='Explain what "Agentic AI" is in one sentence.',
    expected_output='A single sentence definition.',
    agent=intern_agent
)

# 5. Define the Crew
# A Crew is the team container. It holds the agents and the tasks they need to do.
crew = Crew(
    agents=[intern_agent],
    tasks=[learning_task]
)

# 6. Kickoff
# This starts the process.
print("Starting the agent...")
result = crew.kickoff()

print("#################")
print(result)