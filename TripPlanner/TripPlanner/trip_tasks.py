from crewai import Task
from textwrap import dedent
from datetime import date
from tools import SearchTool, GeminiSummarizer  # Import optimized tools

class TripTasks:

    def identify_task(self, agent, origin, cities, interests, range):
        return Task(
            description=dedent(f"""
                Analyze and select the best city for the trip based 
                on specific criteria such as weather, seasonal events, 
                and travel costs. Use **SerpAPI** to fetch real-time 
                data on weather, flights, and cultural events. Then, use 
                **Gemini** to summarize findings into a concise report.
                
                Your final answer must include:
                - Best city based on weather & budget
                - Flight costs & weather forecast
                - Top attractions & upcoming events
                
                {self.__tip_section()}

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}
            """),
            agent=agent,
            tools=[SearchTool, GeminiSummarizer],  # Prioritized tools
            expected_output="Detailed city selection report with flight costs, weather forecast, and attractions"
        )

    def gather_task(self, agent, origin, interests, range):
        return Task(
            description=dedent(f"""
                As the **Local Expert**, gather an in-depth travel 
                guide on the selected city. Use **SerpAPI** to find 
                hidden gems and cultural highlights, and **Gemini** to 
                refine insights into a high-quality travel guide.
                
                Your guide should include:
                - Hidden gems & cultural hotspots
                - Must-visit landmarks & best local events
                - Practical travel tips & high-level cost estimates
                
                {self.__tip_section()}

                Trip Date: {range}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent=agent,
            tools=[SearchTool, GeminiSummarizer],  # Prioritized tools
            expected_output="Comprehensive city guide with local insights and travel tips"
        )

    def plan_task(self, agent, origin, interests, range):
        return Task(
            description=dedent(f"""
                Expand the guide into a **full 7-day travel itinerary** 
                with:
                - Actual places to visit
                - Hotel & restaurant recommendations
                - Daily schedule with weather & budget
                
                Use **SerpAPI** to fetch live travel details, then refine 
                the plan with **Gemini** to ensure the best experience. 
                
                Deliverables:
                - Markdown-formatted **7-day itinerary**
                - Reasons why each place was selected
                - Budget breakdown & packing suggestions
                
                {self.__tip_section()}

                Trip Date: {range}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent=agent,
            tools=[SearchTool, GeminiSummarizer],  # Prioritized tools
            expected_output="7-day detailed travel itinerary with budget, weather, and packing guide"
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"

