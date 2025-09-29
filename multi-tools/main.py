import os
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from tools.operators import multiply, add, subtract, divide

load_dotenv()

# Load your Google API key from environment variable
google_key = os.getenv("GOOGLE_API_KEY")


agent = create_react_agent(
    model = ChatGoogleGenerativeAI(
        model= "gemini-2.5-flash",
        temperature=1.0,
        max_retries=2,
        google_api_key=google_key,
    ),
    # model="google_genai:gemini-2.0-flash",
    tools=[multiply, add, subtract, divide]
)
detailOutput = agent.invoke({"messages": [{"role": "user", "content": "what is multiplication of 3213123 and 23191?"}]})

print(detailOutput)

final_output = detailOutput["messages"][-1]

print(f"AIMessage(content='{final_output.content}')")