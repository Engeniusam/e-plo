import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "e_plo"
DESCRIPTION = "An online legal advisor for Kenyans, providing legal information and guidance on various topics, including family law, criminal law, and civil rights. The agent is designed to assist users in understanding their legal rights and options, as well as providing resources for further assistance."
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "EMPTY")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
LAW_MODEL = os.getenv("LAW_MODEL", "gemini-2.0-flash")
BASE_MODEL = os.getenv("BASE_MODEL", "gemini-2.0-flash-thinking-exp-01-21")