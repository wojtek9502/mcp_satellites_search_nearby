import asyncio
from datetime import datetime, timezone

import dotenv
from agents.mcp import MCPServerStdio, MCPServerStdioParams
from agents import Agent, Runner, trace

dotenv.load_dotenv(override=True)

# example agent instructions
agent_instructions = f"""
Your goal is to calculate satellites passes for user user. 
You have access to satellites_searcher tool that can calculate satellites passes. params: lat and lon are required. If user does not give you that information ask about these details. If there is no satellite name provided, inform user that ISS (ZARYA) will be calculated
Return the response from the tool as they are, do not parse the response from the tool in any way
S it may happen that there will be no satellites passes for user's location then just return short information about.
Current date is {datetime.now(tz=timezone.utc).isoformat()} UTC
"""

# example user prompt
user_input = "My coordinates are 50.06143 19.93658. Show me ISS (ZARYA) passes for the next 10 days."
model = "gpt-4.1-mini"

async def main():
    # we run our own mcp server with our code
    mcp_params = {"command": "uv", "args": ["run", "satellites_search_server.py"]}
    mcp_params = MCPServerStdioParams(**mcp_params)

    async with MCPServerStdio(params=mcp_params, client_session_timeout_seconds=120) as mcp_server:
        agent = Agent(name="agent", instructions=agent_instructions, model=model, mcp_servers=[mcp_server])

        # See the track here https://platform.openai.com/traces
        with trace("Satellites Search"):
            result = await Runner.run(agent, user_input)
            print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
