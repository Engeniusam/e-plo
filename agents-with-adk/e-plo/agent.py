from google.adk.agents.llm_agent import Agent

from .shared_libraries import constants
from . import prompt
from .sub_agents.elawyer.agent import elawyer

root_agent = Agent(
    model=constants.LAW_MODEL,
    name=constants.AGENT_NAME,
    description=constants.DESCRIPTION,
    instruction=prompt.ROOT_PROMPT,
    sub_agents=[
        elawyer
    ]
)