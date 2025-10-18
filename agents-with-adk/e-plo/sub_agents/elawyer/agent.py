from google.adk.agents import Agent
from . import prompt
from ...shared_libraries import constants
from ...tools.search import google_search_grounding

elawyer = Agent(
    model=constants.BASE_MODEL,
    name="e_lawyer",
    description="Web search on law",
    instruction=prompt.RESEARCHER_PROMPT,
    tools=[google_search_grounding]
)
