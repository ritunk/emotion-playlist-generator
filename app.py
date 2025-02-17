import streamlit as st
from transformers import pipeline
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


st.title("Emotion-Based Playlist Generator")


user_text = st.text_input("How are you feeling today?")

if user_text:
    st.write(f"You said: {user_text}")

   
    sentiment_tool = pipeline("sentiment-analysis")

  
    analysis_result = sentiment_tool(user_text)
    sentiment_value = analysis_result[0]['label']
    st.write(f"Detected sentiment: {sentiment_value}")

   
    detected_mood = "happy" if sentiment_value == "POSITIVE" else "sad"
    st.write(f"Mood: {detected_mood}")

  
    if detected_mood == "happy":
        st.write("Suggested Playlist: 'Feel Good Hits'")
    else:
        st.write("Suggested Playlist: 'Chill Vibes'")

   
    spotify_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="a15cacf7b250480da528b4e2337f4d7e",
        client_secret="2f85b67cc1fa4e7195a0fb1988b91e62"
    ))

   
    search_query = "feel good hits" if detected_mood == "happy" else "chill vibes"

    try:
      
        search_response = spotify_client.search(q=search_query, type="playlist", limit=1)
        # st.write("Raw Spotify response:", search_response)  
        playlist_data = search_response.get('playlists', {})
        playlist_items = playlist_data.get('items', [])
        if playlist_items and playlist_items[0]:
            urls = playlist_items[0].get('external_urls', {})
            playlist_link = urls.get('spotify')
            if playlist_link:
                st.write("Spotify Playlist:", playlist_link)
            else:
                st.write("No playlist URL found in the response.")
        else:
            st.write("No playlists were found for this mood. Try a different search term or check your connection.")
    except Exception as err:
        st.write("An error occurred while retrieving the playlist:", err)




