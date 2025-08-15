import asyncio
from datetime import datetime, timezone

import dotenv
from agents.mcp import MCPServerStdio, MCPServerStdioParams
from agents import Agent, Runner, trace

from satellites_search_tool import get_satellite_passes

dotenv.load_dotenv(override=True)

# Set your own URL if you need
TLE_URL = 'https://celestrak.org/NORAD/elements/stations.txt'

agent_instructions = f"""
You are a helpful agent. Your goal is to calculate satellites passes for user user. 
You have access to satellites_searcher tool that can calculate satellites passes. params: lat and lon are required. If user does not give you that information ask about these details. If there is no satellite name provided, inform user that ISS (ZARYA) will be calculated
When you use it it is very important to return calculated satellites passes. You have to return all the details. Remember to not parse tools details. Return details as they are
But sometimes it may happen that there will be no satellites passes for user's location then just return short information about.
Current date is {datetime.now(tz=timezone.utc).isoformat()} UTC
"""
# user_input = "My coordinates are 50.06143 19.93658. Show me ISS (ZARYA) passes for the next 1 days."
user_input =  " My coordinates are 50.06143 19.93658. Show me satellite passes for the next 10 days. My elevation is 1 meter, use Europe/Warsaw timezone"
model = "gpt-4.1-mini"

async def main():
    # we run our own mcp server with our code
    mcp_params = {"command": "uv", "args": ["run", "satellites_search_server.py"]}
    mcp_params = MCPServerStdioParams(**mcp_params)

    async with MCPServerStdio(params=mcp_params, client_session_timeout_seconds=120) as our_mcp_server:
        agent = Agent(name="agent", instructions=agent_instructions, model=model, mcp_servers=[our_mcp_server])

        # See the track here https://platform.openai.com/traces
        with trace("Satellites Search"):
            result = await Runner.run(agent, user_input)
            print(result.final_output)


# async def main():
#     agent = Agent(name="agent", instructions=agent_instructions, model=model, tools=[get_satellite_passes])
#
#     # See the track here https://platform.openai.com/traces
#     with trace("Satellites Search"):
#         result = await Runner.run(agent, user_input)
#         print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
