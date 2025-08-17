import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools
from pathlib import Path
from agno.storage.sqlite import SqliteStorage

def create_research_agent(storage_dir:str='temp') -> Agent:
    Path(storage_dir).mkdir(exist_ok=True)

    return Agent(
        name = "Reasearch Specialist",
        model=Gemini(id="gemini 2.0-flash"),
        tools = [
            GoogleSearchTools(),
            ArxivTools(),
        ],
    )