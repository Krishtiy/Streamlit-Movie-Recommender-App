import streamlit as st
import pickle
import pandas as pd
import requests






def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How would you like to do contacted?',
    movies['title'].values)

if st.button('recommend'):
   recommended_movies = recommend(selected_movie_name)
   cols = st.columns(5)
   for i in range(min(len(recommended_movies), 5)):
       with cols[i]:
           st.text(recommended_movies[i])




