### Project README: Secure Geocoding and Maps Integration 

## 1. Introduction
This project demonstrates a secure, production-ready implementation of a Geocoding API. It uses a **FastAPI** backend as a protected proxy to communicate with **LocationIQ**. This architecture ensures that sensitive API keys are never exposed to the frontend, while also implementing security layers like Bearer Authentication and Rate Limiting.

## 2. Step-by-Step Implementation

### Step 1: Environment Setup
We begin by isolating our sensitive credentials. Using a `.env` file prevents hardcoding secrets into the source code, which is a critical practice for Information Assurance.
1. Create a `.env` file in the root directory.
2. Add your `LOCATIONIQ_TOKEN` (from LocationIQ dashboard) and your `AUTH_TOKEN` (your custom password).



### Step 2: Backend Development (FastAPI)
The backend acts as the "Secure Gateway."
1. **Authentication:** We implemented `HTTPBearer` to intercept requests. The `verify_token` function compares the browser's token with the `.env` file.
2. **Rate Limiting:** To prevent abuse, we added a sliding window logic. It stores timestamps in a list and blocks users if they exceed **5 requests per minute**.
3. **Logic:** The backend uses `httpx` to secretly call LocationIQ and returns only the necessary Latitude, Longitude, and Address to the user.



### Step 3: Frontend Integration (Leaflet.js)
The frontend provides the interactive user interface.
1. **Security UI:** A blurred background and an "Auth Overlay" prevent unauthorized map access.
2. **Map Rendering:** Using Leaflet.js, we initialize a map centered on the Bontoc Campus.
3. **API Calling:** When a user searches, the JavaScript `fetch` command sends the address and the "Bearer" token to our FastAPI server.



---

## 3. How to Use the API

### Prerequisites
Ensure you have Python installed and the following libraries:
```bash
pip install fastapi uvicorn httpx python-dotenv
```

### Running the System
1. **Launch Backend:** Open your terminal and run:
   ```bash
   python main.py
   ```
   The server will start at `http://127.0.0.1:8000`.

2. **Access Frontend:** Open `index.html` in your browser.

### Interaction Steps
1. **Unlock:** Enter your `AUTH_TOKEN` (e.g., `itp322_secret`) in the prompt.
2. **Search:** Once the map unblurs, type a location (e.g., "Bontoc Strategy") in the search bar.
3. **View Result:** The map will automatically fly to the location and drop a pin with the full address.

---

## 4. API Error Reference

401 Unauthorized
This error occurs when the security guard in main.py rejects your request. 

404 Not Found
This means the connection to the backend was successful, but the address you searched for does not exist in the LocationIQ database.

429 Too Many Requests
This is triggered by the Rate Limiter. 

503 Service Unavailable
This error indicates a "Communication Breakdown." It happens when your Python backend is working fine, but it cannot reach the external LocationIQ servers. This is usually caused by a loss of internet connection or the LocationIQ service being temporarily down for maintenance.


---

## 5. File Architecture

* **`main.py`**: The "Brain." Handles security, rate limiting, and API proxying.
* **`index.html`**: The "Face." Handles the map UI, animations, and user input.
* **`.env`**: The "Vault." Stores your private API keys and tokens.
