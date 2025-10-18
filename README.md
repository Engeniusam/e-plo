# E-PLO Digital Legal Assistant

The **Digital Legal Assistant** is a virtual assistant powered by artificial intelligence, designed to help legal professionals and users with legal questions, legal research, and document drafting support. The agent is composed of specialized sub-agents, such as the **Researcher**, which performs web and legal-source searches to ensure the information provided is up to date. This project was developed with the Google ADK (Agent Development Kit).

## What is ADK?

The Agent Development Kit (ADK) is a flexible and modular framework for building and deploying AI agents. ADK can be used with popular LLMs and open-source generative AI tools and is designed with integration into the Google ecosystem and Gemini models in mind. ADK makes it easy to start with simple agents powered by Gemini models and Google AI tools.

To learn more: https://google.github.io/adk-docs/

## Features

- **Researcher**: Performs real-time searches on the web and legal sources for legal topics, case law, and legislation, ensuring responses are based on the most recent information.
- **Legal Assistant**: Provides guidance, explanations and drafting examples (such as contract drafts or petition templates), summarizes documents, and highlights key points to consider.
- **Disclaimer**: The information provided does not replace professional legal advice. Always consult a qualified attorney for legal decisions.

## Architecture

The project is composed of a set of agents that collaborate to provide complete and detailed responses. The main agent workflow includes:

1. **Greetings**: The agent introduces itself and collects information about the request.
2. **Search**: The agent performs real-time searches using the **Researcher** sub-agent to ensure information is current.
3. **Tone**: Adjusts response tone to be technical, professional, and approachable.
4. **Key Constraints**: Responses focused on practical and efficient problem solving.

## How to Run

### Prerequisites

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

### Execution Steps

1. Clone the repository:

   ```bash
   git clone git@github.com:ju4nv1e1r4/agents-with-adk.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in the `.env` file:

   ```bash
      # If using Gemini via Google AI Studio
    GOOGLE_GENAI_USE_VERTEXAI="False"
    GOOGLE_API_KEY="paste-your-actual-key-here"

    # # If using Gemini via Vertex AI on Google Cloud
    # GOOGLE_CLOUD_PROJECT="your-project-id"
    # GOOGLE_CLOUD_LOCATION="your-location" # e.g. us-central1
    # GOOGLE_GENAI_USE_VERTEXAI="True"
   ```

   > If you are using Google Cloud, uncomment and configure the appropriate variables for Vertex AI.

5. To run the agent in the terminal:

   ```bash
   adk run development_tutor/
   ```

6. To run the local web interface:

   ```bash
   adk web
   ```

   Access the application at [http://localhost:8000](http://localhost:8000).

## How it Works

1. The **Digital Legal Assistant** starts by asking about the legal matter and collecting context (for example: case type, jurisdiction, deadlines).
2. The **Researcher** sub-agent performs searches in public and legal sources to verify relevant legislation, doctrine, and case law.
3. The **Digital Legal Assistant** provides guidance, draft text, and clear explanations, always indicating consulted sources and the limits of the information.
4. The tone is adjusted to be technical, professional, and accessible; the agent always reminds users that its responses do not replace formal legal counsel.

See some screenshots in the img/ directory.

## Project Structure

```
.
├── development_tutor/
│   ├── agent.py              # main agent
│   ├── prompt.py             # Prompt base for main agent
│   ├── shared_libraries/     # Constants
│   ├── sub_agents/           # SubAgents
│   │   └── researcher/       # Researcher Agent
│   │       ├── agent.py
│   │       ├── prompt.py
│   └── tools/                # Tools
│       └── search.py         # Google Search Tool
└── README.md
```

## Next Steps

- **Deploy to Google Cloud**: The next step is to take this project to the cloud, using Google Cloud to host the agent and make it accessible globally.

---

This project was developed with a focus on helping legal professionals and users find accurate and timely legal information and drafting support.
