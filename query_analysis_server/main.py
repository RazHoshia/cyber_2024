from fastapi import FastAPI, Request
import re

app = FastAPI()

# Function to analyze queries
def analyze_query(query):
    print("🔍 Query received for analysis")
    if "SELECT * FROM users WHERE name = 'admin' OR '1'='1';" in query:
        return "block"
    return "allow"

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    query = data.get("query", "")

    print(f"🔍 Received query: {query}")  # Debugging
    decision = analyze_query(query)

    if decision == "block":
        print(f"🚨 BLOCKED: {query}")  # Log blocked queries
    else:
        print(f"✅ ALLOWED: {query}")

    return {"action": decision}