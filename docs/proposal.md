# Pokémon-Themed Playlist Generator

## Overview
This application will allow users to generate Spotify playlists based on their favorite Pokémon. Users will log in using third-party authentication (e.g., Google OAuth), and the app will store their profile and preferences in a database. By leveraging the Spotify API and PokeAPI, the application will correlate the user's favorite Pokémon characteristics with music genres and moods to create custom playlists. This ensures that users can enjoy a personalized music experience based on their Pokémon preferences.

## User Benefits
- **Personalized Spotify Playlists:** Users get custom playlists based on their favorite Pokémon characteristics.
- **Engaging Experience:** An entertaining way to discover new music through Pokémon themes.
- **Easy Login and Profile Management:** Secure and straightforward login process using third-party authentication.

## Project Requirements and Implementation Plan

### Database Utilization
- **User Profile Information:** Store user profiles, including Pokémon preferences and music tastes.
- **Playlist Data:** Store generated playlists for user access and history.
- **Pokémon Data Cache:** Cache Pokémon data for quick access and to reduce API call frequency.

**Implementation:** Use a relational database (e.g., PostgreSQL) to manage user profiles, playlist data, and cached Pokémon data.

### Correlate Publicly Available Datasets via API
- **Spotify API:** Fetch user playlists and generate custom playlists based on Pokémon characteristics.
- **PokeAPI:** Retrieve Pokémon data to determine characteristics that influence music genre and mood selection.

**Implementation:** Integrate Spotipy for Spotify API interactions and Requests for PokeAPI interactions.

### Third-Party Authentication
Implement OAuth 2.0 for user authentication via Google, ensuring a secure and straightforward login process.

**Implementation:** Use the Flask-Dance library to handle OAuth authentication.

### Decoupled Architecture
- **Front End:** Develop a user-friendly interface using JavaScript (e.g., React) to display Pokémon and playlists.
- **Back End:** Use Flask to handle API requests, database interactions, and business logic.
- **RESTful Interface:** Ensure communication between front end and back end via RESTful APIs.

**Implementation:** 
- **Front End:** Build a responsive UI with React, allowing users to input Pokémon preferences and view generated playlists.
- **Back End:** Create RESTful endpoints in Flask to serve the front end, handle authentication, interact with APIs, and manage the database.
