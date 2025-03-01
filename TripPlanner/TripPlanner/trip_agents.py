from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI,Ollama
from langchain_openai import ChatOpenAI

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet :
-Think like a boss. Work backwards from the goal and think which employee you need to hire to get the job done.
-Define the captain of the crew who orient the other agents towards the goal.
-Define which experts the captain needs to communicate with and delegate tasks to.
Build a top down structure of the crew.

Goal:
Captain/Manager/Boss

Employees/Experts to hire:

Notes:
-Agents should be results driven and have a clear goal in mind
-Role is their job title
-Goals should be actionable
-Backstory should be their resume
"""

class TripAgents():

  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True)
