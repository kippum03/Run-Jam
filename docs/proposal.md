# Safe Running Route and Playlist Generator

**Overview:**
This application will help users find the safest running routes in their area based on crime statistics from publicly available datasets (e.g., FBI crime data). Users will log in using third-party authentication (e.g., Facebook OAuth), and the app will store their profile and running preferences in a database. Based on the user's desired running time and location, the app will generate a safe running route and create a Spotify playlist tailored to the length and style of the run. This ensures that users can enjoy a safe and musically enjoyable workout experience.

**User Benefits:**
- Safe running routes based on real-time crime data to ensure user safety.
- Custom Spotify playlists that match the duration and intensity of their run.
- A seamless integration of safety and entertainment for a more enjoyable running experience.

## Project Requirements and Implementation Plan

### Database Utilization
- **User Profile Information:** Store user profiles, including preferences and running history.
- **Run Data:** Store past run data and routes for personalized recommendations.
- **Crime Data Cache:** Cache crime data for quick access and to reduce API call frequency.

*Implementation:* Use a relational database (e.g., PostgreSQL) to manage user profiles, run data, and cached crime data.

### Correlate Publicly Available Datasets via API
- **Spotify API:** Fetch user playlists and generate custom playlists based on running duration.
- **Crime Data API:** Utilize crime data from a public API (e.g., Crimeometer, FBI crime data) to determine the safety of potential running routes.

*Implementation:* Integrate Spotipy for Spotify API interactions and Requests for crime data API interactions.

### Third-Party Authentication
- Implement OAuth 2.0 for user authentication via Facebook or Google, ensuring a secure and straightforward login process.

*Implementation:* Use the Flask-Dance library to handle OAuth authentication.

### Decoupled Architecture
- **Front End:** Develop a user-friendly interface using JavaScript (e.g., React) to display routes and playlists.
- **Back End:** Use Flask to handle API requests, database interactions, and business logic.
- **RESTful Interface:** Ensure communication between front end and back end via RESTful APIs.

*Implementation:*
- **Front End:** Build a responsive UI with React, allowing users to input running preferences and view routes and playlists.
- **Back End:** Create RESTful endpoints in Flask to serve the front end, handle authentication, interact with APIs, and manage the database.
