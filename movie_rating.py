import streamlit as st
import requests

API_KEY = "ef0362332e0bc5753fe44a17da572645"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(movie_name):
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(search_url)

    if response.status_code == 200:
        results = response.json()["results"]
        if results:
            return results[0]  # Return the first matched movie
    return None

st.title("🎬 Movie Rating Search (Like Google)")

movie_name = st.text_input("Enter a Hollywood movie name:")

if st.button("Search"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        movie = search_movie(movie_name)
        if movie:
            st.subheader(movie["title"])
            st.write(f"⭐ Rating: {movie['vote_average']} / 10")
            st.write(f"📅 Release Date: {movie['release_date']}")
            st.write("📝 Overview:")
            st.write(movie["overview"])

            poster_path = movie.get("poster_path")
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                st.image(poster_url, use_column_width=True)
        else:
            st.error("Movie not found. Try another title.")
