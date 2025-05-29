import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set Streamlit config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Inject custom CSS for background (target .stApp only)
st.markdown("""
    <style>
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        height: 100%;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Segoe UI', sans-serif;
    }

    header {
        display: none !important;
    }

    .block-container {
        padding-top: 2rem;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .select-label {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .movie-box {
        background-color: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 15px 20px;
        margin-bottom: 10px;
        color: white;
        backdrop-filter: blur(10px);
        font-size: 1.1rem;
        font-weight: 500;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)






# Title
st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

# Selectbox
selected_movie_name = st.selectbox("🎞️ SELECT A MOVIE", movies['title'].values)

# Button & output
if st.button("🎯 Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader("📽️ Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.markdown(f"**{i}.** {movie}")
