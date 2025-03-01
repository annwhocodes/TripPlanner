from langchain.tools import Tool
from langchain_google_search import GoogleSerperAPIWrapper
from langchain_openai import ChatOpenAI

# Initialize SerpAPI search
search = GoogleSerperAPIWrapper()

# Initialize Gemini Model
gemini = ChatOpenAI(model="gemini-pro")

def search_internet(query):
    """Search the internet using SerpAPI"""
    return search.run(query)

def summarize_with_gemini(text):
    """Use Gemini to summarize search results"""
    prompt = f"Summarize the following travel information concisely:\n\n{text}"
    return gemini.predict(prompt)

# Define tools
SearchTool = Tool(
    name="Search Tool",
    func=search_internet,
    description="Use this to fetch travel-related information from the web."
)

GeminiSummarizer = Tool(
    name="Gemini Summarizer",
    func=summarize_with_gemini,
    description="Use this to summarize travel-related search results."
)
