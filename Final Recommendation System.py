# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:12:17 2023

@author: hp
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#MUSIC RECOMMENDER
def music_recommender():
    # load the CSV file into a Pandas DataFrame
    songs_df=pd.read_csv('songs1.csv')
        
    #CONTENT BASED
    def content_based_recommender():

        # create a TfidfVectorizer object
        tfidf_vectorizer=TfidfVectorizer(stop_words='english')

        # replace any NaN values in the 'genre' and 'artist' columns with an empty string
        songs_df['genre']=songs_df['genre'].fillna('')
        songs_df['artist']=songs_df['artist'].fillna('')

        # create a matrix of TF-IDF features for the 'genre' and 'artist' columns
        tfidf_matrix_genre=tfidf_vectorizer.fit_transform(songs_df['genre'])
        tfidf_matrix_artist = tfidf_vectorizer.fit_transform(songs_df['artist'])

        # get user input for song title and number of songs to display
        song_title = input("Enter a song title: ")
        song_title=song_title.lower()
        # check if entered song title is in the database
        if song_title not in songs_df['title'].values:
            print("Sorry, the entered song title is not in the database.")
        else:
            # get user input for choice of cosine similarity column(s)
            similarity_choice=input("Enter 'genre' for genre-based similarity or 'artist' for artist-based similarity or 'both' for both: ")

            # calculate the cosine similarity of each song with every other song in the matrix based on the chosen column(s)
            if similarity_choice=='genre':
                cosine_sim=cosine_similarity(tfidf_matrix_genre)
            elif similarity_choice=='artist':
                cosine_sim=cosine_similarity(tfidf_matrix_artist)
            else:
                cosine_sim_genre=cosine_similarity(tfidf_matrix_genre)
                cosine_sim_artist=cosine_similarity(tfidf_matrix_artist)
                cosine_sim=cosine_sim_genre+cosine_sim_artist
                
            # get the index of the song you want to use as an example
            song_index=songs_df[songs_df['title']==song_title].index[0]
                
            # get user input for number of songs to display
            n=int(input("Enter the number of songs to display: "))
            
            # get a list of tuples of the form (song index, similarity score) for all songs
            similarity_scores=list(enumerate(cosine_sim[song_index]))

            # sort the list by similarity score in descending order
            similarity_scores=sorted(similarity_scores, key=lambda x: x[1], reverse=True)

            # get the top n most similar songs (excluding the input song itself)
            top_songs=[song for song in similarity_scores if song[0]!=song_index][:n]

            # print the titles of the top n most similar songs
            if similarity_choice=='genre':
                print("Based on the genre of your entered song, you might like")
            elif similarity_choice=='artist':
                print("Based on the artist of your entered song, you might like")
            else:
                print("Based on the genre and artist of your entered song, you might like")
            for song in top_songs:
                print('- ', songs_df.iloc[song[0]]['title'])
                
    #POPULARITY BASED
    def popularity_based_recommender():
        # Get the user's desired genre input
        mood=input("Enter the mood of music you'd like to listen to: ")

        # Filter the DataFrame to only include songs of the desired genre
        mood_df=songs_df[songs_df['mood']==mood]
        if mood_df.empty:
            print(f"No {mood} songs found in the database. Try a different mood.")
        else:
            # Sort the DataFrame by rating in descending order
            sorted_mood_df=mood_df.sort_values(by='rating', ascending=False)
            
            # Get the top 5 songs with the highest rating
            top_songs=sorted_mood_df.head(5)
            
            # Print the titles of the top 5 songs
            print(f"\nTop 5 {mood} songs in the world today:")
            for song_title in top_songs['title']:
                print('- ', song_title)
            
    #DRIVER CODE
    while True:
        method=input("Please choose one of the following options for your recommendation: \n - Press 1 for content based song recommendation \n - Press 2 for popularity based recommendation \n")

        # perform recommendation based on user's choice
        if method=='1':
            content_based_recommender()
        elif method=='2' :
            popularity_based_recommender()
        else:
            print("Invalid recommendation method")
        
        con=input("Would you like another song recommendation? (y/n) \n")
        if con.lower()=='n':
            break
        
#MOVIE RECOMMENDER
def movie_recommender():
    # load the CSV file into a Pandas DataFrame
    movie_df=pd.read_csv('movies.csv')
        
    #CONTENT BASED
    def content_based_recommender():

        # create a TfidfVectorizer object
        tfidf_vectorizer=TfidfVectorizer(stop_words='english')

        # replace any NaN values in the 'genre' and 'artist' columns with an empty string
        movie_df['genre']=movie_df['genre'].fillna('')
        movie_df['director']=movie_df['director'].fillna('')

        # create a matrix of TF-IDF features for the 'genre' and 'artist' columns
        tfidf_matrix_genre=tfidf_vectorizer.fit_transform(movie_df['genre'])
        tfidf_matrix_director=tfidf_vectorizer.fit_transform(movie_df['director'])

        # get user input for song title and number of songs to display
        movie_name=input("Enter a movie name: ")
        movie_name=movie_name.lower()
        # check if entered song title is in the database
        if movie_name not in movie_df['title'].values:
            print("Sorry, the entered movie title is not in the database.")
        else:
            # get user input for choice of cosine similarity column(s)
            similarity_choice=input("Enter 'genre' for genre-based similarity or 'director' for director-based similarity or 'both' for both: ")

            # calculate the cosine similarity of each song with every other song in the matrix based on the chosen column(s)
            if similarity_choice=='genre':
                cosine_sim=cosine_similarity(tfidf_matrix_genre)
            elif similarity_choice=='director':
                cosine_sim=cosine_similarity(tfidf_matrix_director)
            else:
                cosine_sim_genre=cosine_similarity(tfidf_matrix_genre)
                cosine_sim_director=cosine_similarity(tfidf_matrix_director)
                cosine_sim=cosine_sim_genre+cosine_sim_director
                
            # get the index of the song you want to use as an example
            movie_index=movie_df[movie_df['title']==movie_name].index[0]
                
            # get user input for number of songs to display
            n=int(input("Enter the number of movies to display: "))
            
            # get a list of tuples of the form (song index, similarity score) for all songs
            similarity_scores=list(enumerate(cosine_sim[movie_index]))

            # sort the list by similarity score in descending order
            similarity_scores=sorted(similarity_scores, key=lambda x: x[1], reverse=True)

            # get the top n most similar songs (excluding the input song itself)
            top_movies=[movie for movie in similarity_scores if movie[0]!=movie_index][:n]

            # print the titles of the top n most similar songs
            if similarity_choice=='genre':
                print("Based on the genre of your entered song, you might like")
            elif similarity_choice=='director':
                print("Based on the director of your entered song, you might like")
            else:
                print("Based on the genre and director of your entered song, you might like")
            for movie in top_movies:
                print('- ', movie_df.iloc[movie[0]]['title'])
                
    #POPULARITY BASED
    def popularity_based_recommender():
        # Get the user's desired genre input
        genre = input("Enter the genre of movie you'd like to watch: ")
        
        # Filter the DataFrame to only include movies of the desired genre
        genre_df = movie_df[movie_df['genre'] == genre]

        if genre_df.empty:
            print(f"No {genre} movies found in the database. Try a different genre.")
        else:
            # Sort the DataFrame by rating in descending order
            sorted_genre_df = genre_df.sort_values(by='rating', ascending=False)

            # Get the top 5 movies with the highest rating
            top_movies = sorted_genre_df.head(5)
            
            # Print the titles of the top 5 movies
            print(f"\nTop {genre} movies based on IMDb ratings:")
            for movie_name in top_movies['title']:
                print('- ', movie_name)
            
    #DRIVER CODE
    while True:
        method=input("Please choose one of the following options for your recommendation: \n - Press 1 for content based recommendation \n - Press 2 for popularity based recommendation \n")

        # perform recommendation based on user's choice
        if method=='1':
            content_based_recommender()
        elif method=='2' :
            popularity_based_recommender()
        else:
            print("Invalid recommendation method")
        
        con=input("Would you like another movie recommendation? (y/n) \n")
        if con.lower()=='n':
            break
        
#THE OTHER DRIVER CODE
while True:
     method=input("Enter M if you want a movie recommendation. Enter S if you want a song recommendation \n")

     # perform recommendation based on user's choice
     if method.lower()=='m':
         movie_recommender()
     elif method.lower()=='s' :
         music_recommender()
     else:
         print("Invalid recommendation")
     
     con=input("Do you want to continue? (y/n) \n")
     if con.lower()=='n':
         print("Thank you :)")
         break

