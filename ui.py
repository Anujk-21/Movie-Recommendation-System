import streamlit as st
import pandas as pd
import pickle

# Load model
similarity_loaded = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity_loaded[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in range(1, 6):
        movie_id = distances[i][0]
        recommended_movies.append(movies.iloc[movie_id])
    return recommended_movies

# UI
st.title('Movie Recommendation System 📽️')

movies = pd.read_csv('top10K-TMDB-movies.csv')

movie_name = st.text_input('Enter a movie name')

if st.button('Recommend 🔍'):
    if movie_name:
        try:
            recommended_movies = recommend(movie_name)
            st.subheader('Recommended Movies:')
            for movie in recommended_movies:
                st.write(f"**Title:** {movie['title']}")
            st.balloons()
        except:
            st.write('Movie not found!')
    else:
        st.write('Please enter a movie name.')

# Sidebar for developer info
st.sidebar.title('About')
st.sidebar.write('magine having a cinematic compass guiding you through the vast universe of movies, pointing you towards your next adventure.')
st.sidebar.write('This system is your personalized movie oracle, using the power of algorithms to sift through a galaxy of films and unearth the ones tailored to your unique tastes.')
st.sidebar.title('Developer 😎')
st.sidebar.write('Anuj Karoddeo ')
st.sidebar.write('Email : anujkaroddeo@gmail.com ')
