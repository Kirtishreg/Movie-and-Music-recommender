import pandas as pd

# Load the CSV file into a Pandas DataFrame
songs_df = pd.read_csv('songs.csv')

# Get the user's desired genre input
genre = input("Enter the genre of music you'd like to listen to: ")

# Filter the DataFrame to only include songs of the desired genre
genre_df = songs_df[songs_df['genre'] == genre]

# Sort the DataFrame by rating in descending order
sorted_genre_df = genre_df.sort_values(by='rating', ascending=False)

# Get the top 5 songs with the highest rating
top_songs = sorted_genre_df.head(5)

# Print the titles of the top 5 songs
print(f"\nTop 5 {genre} songs based on ratings:")
for song_title in top_songs['title']:
    print(song_title)
