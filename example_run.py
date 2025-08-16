import asyncio
import os
from datetime import datetime, timezone

import dotenv
from agents.mcp import MCPServerStdio, MCPServerStdioParams
from agents import Agent, Runner, trace

dotenv.load_dotenv(override=True)
if 'OPENAI_API_KEY' not in os.environ.keys():
    raise Exception('OPENAI_API_KEY environment variable not set')


# example agent instructions
agent_instructions = f"""
Your goal is to calculate satellite passes for the user. 
You have access to the satellites_searcher tool that can calculate satellite passes. params: lat and lon are required. If the user does not give you that information, ask about these details.
Return the response from the tool as it is; do not parse the response from the tool in any way.
It may happen that there will be no satellite passes for the user's location; then just return short information about it.
The current date is {datetime.now(tz=timezone.utc).isoformat()} UTC
"""

# example user prompt
# user_input = "My coordinates are 50.06143 19.93658."
# user_input = "My coordinates are 50.06143 19.93658. Show me ISS (ZARYA)"
#user_input = "My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 10 days."
# user_input = "My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days."
# user_input = "My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days. Use timezone Europe/Warsaw"
user_input = "My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days. Search for the passes with minimum culmination altitude 20 deg"
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
