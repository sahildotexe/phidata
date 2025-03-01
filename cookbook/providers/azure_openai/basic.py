from phi.agent import Agent, RunResponse  # noqa
from phi.model.azure import AzureOpenAIChat

agent = Agent(model=AzureOpenAIChat(id="gpt-4o"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story")
