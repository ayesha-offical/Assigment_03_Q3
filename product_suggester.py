import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemeni_api_key = os.getenv('GEMINI_API_KEY')

provider = AsyncOpenAI(
    api_key= gemeni_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

agent =Agent(
    name="Product Suggester",
    instructions="Suggest products ans explain them and give short description based on user preferences and requirements.",
    model=model,
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

user_input = input("Enter your preferences and requirements: ")


result =Runner.run_sync(agent, user_input,run_config=config)
print("\nCall The agent's output: \n")
print(result.final_output)