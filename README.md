ITP 322: Advanced Geocoding System - Group 1

This project is a full-stack Geocoding application developed for Mountain Province State University (MPSU). It features a FastAPI backend that acts as a secure proxy to the Nominatim Geocoding service and a modern Leaflet.js frontend for interactive mapping.
Features

    Secure API: Implements HTTP Bearer Token authentication to prevent unauthorized access.

    Real-time Geocoding: Converts text-based addresses (e.g., Baguio City) into precise geographic coordinates.

    Interactive Map: A custom-styled Leaflet map with smooth fly-to animations and location markers.

    CORS Enabled: Configured to allow seamless communication between the frontend and backend.

Tech Stack

    Backend: Python 3.10+, FastAPI, Uvicorn, HTTPX

    Frontend: HTML5, CSS3, JavaScript (ES6+)

    Map Engine: Leaflet.js with CartoDB Positron Light tiles

Installation & Setup

    Install Dependencies: pip install fastapi uvicorn httpx

    Run the Backend Server: python main.py

    Launch the Frontend: Open index.html using the Live Server extension in VS Code to ensure the Authorization headers are permitted by the browser.

Authentication

The API requires the following header for all requests:
Header Name: Authorization
Value: Bearer itp322_secret_token
