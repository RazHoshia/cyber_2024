from fastapi import FastAPI, Request
import re

app = FastAPI()

# Function to analyze queries
def analyze_query(query):
    print("🔍 Query received for analysis")
#    if "SELECT * FROM users WHERE ?=?;" in query:
    if "select * from users limit ?" in query:
        return "block"
    return "allow"

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    query = data.get("query", "")

    print(f"🔍 Received query: {query}")  # Debugging
    decision = analyze_query(query)

    response_message = {
        "action": f"🚨 BLOCKED: {query}" if decision == "block" else f"✅ ALLOWED: {query}",
        "received_data": data  # Including all received data
    }

    if decision == "block":
        print(f"🚨 BLOCKED: {query}")  # Log blocked queries
    else:
        print(f"✅ ALLOWED: {query}")

    return response_message