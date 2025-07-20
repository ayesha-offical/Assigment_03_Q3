import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()

load_dotenv()

geemini_api_key = os.getenv("GEMINI_API_KEY")

provider =AsyncOpenAI(
    api_key=geemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

sad_agent =Agent(
    name="Sad mood",
    instructions="Your are a sad mood agent ok if user is sad you have to reply and make sure you answer heal the user if user is said and not happy you have to make sure you answer in a way that makes the user happy and feel better.",
    model=model
)

Happy_agent=Agent(
    name="Happy mood",
    instructions="You are happy agent if user say something that makes him happy you have to reply in a way that makes the user feel happy and make sure you answer in a way that makes the user more happy and feel better.",
    model=model

)

tragie_agent=Agent(
    name="Mood Selecter",
    instructions="You are a mood selecter agent if user is sad you have to  use sad agent and if user is happy you have to use happy agent to anser the user ok and if user asking niether than about mood so tell user that i can only answer about mood and nothing else ok.",
    handoffs=[sad_agent, Happy_agent]
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

user_input = input("Enter your mood: ")

result = Runner.run_sync(tragie_agent, user_input, run_config=config)
print("\nCall The agent's output: \n")
print(result.final_output)