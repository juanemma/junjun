🌟 What is this project?

This is a web-based mapping tool that allows a user to search for a location (like "Baguio City") and see it instantly on an interactive map.

Instead of just showing a map, we built a Secure Backend that protects our data and prevents people from spamming our system.
🚀 Key Features

    Secure Access: Only users with the correct "Secret Token" can use the search.

    Anti-Spam (Rate Limiting): The system only allows 5 searches per minute to keep the network fast.

    Interactive Map: A smooth, zooming map that works without needing a credit card or expensive Google billing.

    Clean Code: We separated the "Security" (Main Server) from the "Searching" (Services) to keep the project organized.

🛠️ How it Works (The "Behind the Scenes")

    The User: Types a place in the search bar on index.html.

    The Security Guard: The request goes to our FastAPI server. It checks if the "Bearer Token" is correct.

    The Searcher: If the token is good, our services.py talks to LocationIQ to get the exact Latitude and Longitude.

    The Map: The coordinates are sent back to the browser, and Leaflet.js moves the map to that spot.

📂 Project Files

    main.py: The "Brain" of the project. It handles security and limits.

    services.py: The "Worker." It handles the actual searching.

    index.html: The "Face." This is the map the user sees.

    .env: The "Safe." This hides our private API keys.

🏃 How to Start the App

    Install the tools:
    Open your terminal and type:
    pip install fastapi uvicorn requests python-dotenv slowapi

    Add your Key:
    Make sure your pk.xxxx key is inside the .env file.

    Run the Server:
    Type: uvicorn main:app --reload

    Open the Map:
    Double-click index.html to start searching!

💡 Tips

    Test the Limit: Search 6 times very fast. Show the instructor the error message that says you are searching too quickly.

    Test the Security: Try to search without the token. Show that the system blocks you with an "Unauthorized" message.

    Show the Map: Search for "Bontoc" to show the marker landing right on our home campus area!
