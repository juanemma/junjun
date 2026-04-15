# --- FILE: main.py ---
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import os
import uvicorn
import time  # Import time to track request timestamps
from dotenv import load_dotenv

load_dotenv()
LOCATIONIQ_TOKEN = os.getenv("LOCATIONIQ_TOKEN")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

app = FastAPI()
security = HTTPBearer()

# --- RATE LIMIT STORAGE ---
# This list will store the timestamps of each successful request
request_history = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid Security Key")
    return True

# --- RATE LIMIT CHECKER ---
def check_rate_limit():
    current_time = time.time()
    global request_history
    
    # 1. Clean up: Remove timestamps older than 60 seconds
    request_history = [t for t in request_history if current_time - t < 60]
    
    # 2. Check: If we have 5 or more requests in the last minute, block the user
    if len(request_history) >= 5:
        raise HTTPException(
            status_code=429, 
            detail="Rate limit exceeded. Maximum 5 requests per minute allowed."
        )
    
    # 3. Record: Add the current request timestamp to the history
    request_history.append(current_time)

@app.get("/api/v1/geocode")
async def geocode(
    address: str, 
    authorized: bool = Depends(verify_token),
    rate_limit: bool = Depends(check_rate_limit) # Injects the rate limiter here
):
    url = f"https://us1.locationiq.com/v1/search.php?key={LOCATIONIQ_TOKEN}&q={address}&format=json"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()
        except Exception:
            raise HTTPException(status_code=503, detail="LocationIQ Service Unavailable")

    if not data or (isinstance(data, dict) and "error" in data):
        raise HTTPException(status_code=404, detail="Location not found")

    return {
        "status": "success",
        "data": {"lat": float(data[0]["lat"]), "lng": float(data[0]["lon"]), "address": data[0]["display_name"]}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)