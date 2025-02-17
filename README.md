# Emotion-Based Playlist Generator

**Emotion-Based Playlist Generator** is a Streamlit-based web application that leverages sentiment analysis to determine your mood and recommend a corresponding Spotify playlist. The project uses Hugging Face's Transformers library for sentiment analysis and Spotipy to interact with the Spotify Web API.

## Features

- **User Input:** Type in how you're feeling.
- **Sentiment Analysis:** Uses a pre-trained sentiment analysis pipeline to detect whether the sentiment is positive or negative.
- **Mood Mapping:** Maps detected sentiment to a mood (e.g., "happy" for positive, "sad" for negative).
- **Playlist Recommendation:** Searches Spotify for a playlist that matches your mood (e.g., "Feel Good Hits" for happy, "Chill Vibes" for sad).
- **Error Handling:** Provides user-friendly messages if playlists can't be retrieved or if errors occur.

## Requirements

- Python 3.10
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [PyTorch](https://pytorch.org/) (or TensorFlow, if preferred)
- Additional dependencies are listed in the `requirements.txt` file.


