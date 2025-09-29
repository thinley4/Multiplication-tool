from langchain_core.tools import tool
import os
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Load your Google API key from environment variable
google_key = os.getenv("GOOGLE_API_KEY")

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

agent = create_react_agent(
    model = ChatGoogleGenerativeAI(
        model= "gemini-2.5-flash",
        temperature=1.0,
        max_retries=2,
        google_api_key=google_key,
    ),
    # model="google_genai:gemini-2.0-flash",
    tools=[multiply]
)
detailOutput = agent.invoke({"messages": [{"role": "user", "content": "what's 8282 x 99191?"}]})

print(detailOutput)

final_output = detailOutput["messages"][-1]

print(f"AIMessage(content='{final_output.content}')")