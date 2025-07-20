import os
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()

def configation():
    client =AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-1.5-flash",
        openai_client=client,
    )

    config =RunConfig(
        model =model,
        model_provider=client,
        tracing_disabled=True,
    )


    country_capital_agent =Agent(
        name="Country_capital_agent",
        instructions="Answer only questions about the **capital cities** of countries. If the question is unrelated, do not answer.",
        model=model
    )

    country_language_agent =Agent(
        name="country_language_agent",
        instructions="Answer only questions about the **Languages** of countries. If the question is unrelated, do not answer.",
        model=model
    )

    print("Country_population_agent called:")
    country_population_agent = Agent(
        name="country_population_agent",
        instructions="Answer only questions about the **population of countries**. If the question is unrelated, do not answer.",
        model=model
    )


    country_info_agent=Agent(
        name="country_info_agent",
        instructions=(
            "You are a helpful agent that provides information about countries. "
            "Use the country_capital_agent tool to get the capital of a country, "
            "the country_language_agent tool to get the language of a country, and "
            "the country_population_agent tool to get the population of a country. "
            "Only answer if the query is related to country information. Otherwise, say you cannot help."
        ),

    tools=[
    country_capital_agent.as_tool(
        tool_name="country_capital_agent",
        tool_description="This tool is used to get the capital of a country."
    ),
    country_language_agent.as_tool(
        tool_name="country_language_agent",
        tool_description="This tool is used to get the language of a country."
    ),
    country_population_agent.as_tool(
        tool_name="country_population_agent",
        tool_description="This tool is used to get the population of a country."
    ),
    ],
    model=model
    )

    return country_info_agent, config

country_info_agent, config = configation()

user_input = input("Enter your country-related question: ")

result = Runner.run_sync(country_info_agent, user_input, run_config=config)

print("\nCall The agent's output: \n")

print(result.final_output)
