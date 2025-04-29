Music-and-Movie-Recommender

DESCRIPTION: Recommending music and movies to users can be done in multiple ways using content-based filtering and collaborative filtering approaches. Content-based filtering approach primarily focuses on the item similarity i.e., the similarity in songs/movies, whereas collaborative filtering focuses on drawing a relation between different users of similar choices in listening to songs or watching the movies.

Content-based recommendation: Recommends songs that are similar to the user's input based on the song's genre and/or artist for music recommendation while recommends similar movies to the user’s input based on genre and directors for movie recommendation. The system uses the cosine similarity of the TF-IDF (term frequency-inverse document frequency) features of the genre, director and/or artist columns to find similar songs.
Popularity-based recommendation: Recommends the most popular songs of a user's desired mood and highest rated movies for a particular genre. The system filters the song dataset by the user's desired mood or genre in case of movies and sorts them by rating/imdb in descending order. It then returns the top 5 songs/movies. A while loop is used to ask the user to choose between the two recommendation methods, and then calls the corresponding function based on the user’s input and also provides an option to continue with more recommendations or exit the program.
CODE AND EXPLANATIONS:

Importing the Libraries Firstly, the required libraries are imported.

Following is the brief use of each imported library in the code:

Pandas: This library is used for data manipulation and analysis. In this code, it is used to read the CSV file into a Pandas Dataframe and filter, sort, and display the data as needed.
TfidVectorizer: This is a feature extraction library used for vectorizing text data. In this code, it is used to create a matrix of TF-IDF features for the 'genre' and 'artist' columns of the songs dataset while ‘genre’ and ‘director’ column of movies dataset.
Cosine_similarity: This is a metric used to measure the similarity between two non-zero vectors of an inner product space. In this code, it is used to calculate the cosine similarity of each song with every other song in the matrix based on the chosen column(s). Also the movie similarities are found with every other movie using the same approach.
Music or Movies recommender The main driver code consists of a while loop that asks the user if they want music recommendations or movies recommendations. Based on the user choice that particular recommendation function is called. An appropriate message is displayed in case of an invalid user choice. The loop keeps on executing again until the user wants otherwise.

Now if the choice is song recommendation:

Music Recommendation System

Loading the dataset Then the dataset from the csv file is loaded into a pandas dataframe object named as ‘songs_df’.

While loop for Choice of Recommendation The following while loop starts executing and takes an input from the user: “Please choose one of the following options for your recommendation: Press 1 for content-based song recommendation Press 2 for popularity-based recommendation”

Based on the user choice of recommendation system the respective functions are called and in case of any invalid choice a message is displayed on the screen. After recommending the songs based on user choice the program asks the user if they want to continue running the program again or not using y for yes and n for no. The input is converted to lower case using .lower() function. If the user quits a thank you message is printed and the execution stops, else the while loop begins executing again.

Content-based Recommender Now, if the user choice is 1 content-based recommender is called as shown.

Tfidfvectorizer () converts a collection of raw documents to a matrix of TF-IDF features. TF-IDF stands for Term Frequency Inverse Document Frequency of records. It can be defined as the calculation of how relevant a word in a series or corpus is to a text. The meaning increases proportionally to the number of times in the text a word appears but is compensated by the word frequency in the data-set. In document d, the frequency represents the number of instances of a given word t. Therefore, we can see that it becomes more relevant when a word appears in the text, which is rational. Since the ordering of terms is not significant, we can use a vector to describe the text in the bag of term models. This is called term frequency. Whereas document frequency is the number of occurrences in the document set N of the term t. In other words, the number of papers in which the word is present is DF. The IDF of the word is the number of documents in the corpus separated by the frequency of the text. It is calculated by taking the log(base 2) of Number of documents containing the term t divided by document frequency of the term t. Initially, a TfidfVectorizer object named tfidf_vectorizer with English stop words is created. Then any NaN values in genre and artist columns of songs_df, the dataframe object we created from csv file, are replaced with empty strings.

Tfidf-vectorization A matrix of TF-IDF features is created from the columns genre and artists of songs_df using fit_transform. It is the same as fit function followed by transform but is much more efficiently implemented.

The title of a song of user choice is taken as input, converted to lower case and is searched for in our songs_df dataset. If the song is not present a message is displayed and if it is present then the code asks for user choice for the calculation of cosine similarity.

Cosine Similarity In Data Mining, similarity measure refers to distance with dimensions representing features of the data object, in a dataset. If this distance is less, there will be a high degree of similarity, but when the distance is large, there will be a low degree of similarity. Some of the popular similarity measures are Euclidean distance, Manhattan distance, Minkowski distance, Cosine similarity, etc. Cosine similarity is a measure of similarity between two non-zero vectors defined in an inner product space. It follows that the cosine similarity does not depend on the magnitudes of the vectors, but only on their angle. Thus, it is a metric helpful in determining how similar the data objects are irrespective of their size. We used cosine similarity here to measure the similarity between two sentences or words or strings. The cosine similarity is beneficial because even if the two similar data objects are far apart by the Euclidean distance because of the size, they could still have a smaller angle between them. Smaller the angle, higher the similarity. When plotted on a multi-dimensional space, the cosine similarity captures the orientation (the angle) of the data objects and not the magnitude. Hence, according to the user choice cosine similarity for each song with every other song is calculated on genre or artists columns. If the user chooses the option both, cosine similarity for both genre and artist columns is calculated and added.

The index of the song entered by the user is found in songs_df and the user is asked to enter the n number of songs he wants as output.

_Creating a list of Similarity Scores _ A list of tuples of all songs is created of the format (song_index, similarity score) where similarity score is the cosine similarity of every song with the user entered song. This list of tuples is then sorted in descending order on the basis of these similarity scores. Then the first n (number of songs the user wanted) songs leaving out the user entered song are stored in another list called Top songs.

Recommending the songs An appropriate message is displayed according to the cosine similarity user chose and the titles of the top n recommended songs are printed.

Popularity-based recommender Now, if the user choice is 2 popularity-based recommender is called as shown.

The popularity-based recommender works on a song rating allotted to each song on how frequently the song is played by other users and how well-liked the song is. But instead of displaying the top popular songs, this recommender filters the top songs to show the only ones based on user’s mood and what they want to hear. Filtering the dataset Firstly, the dataframe is filtered to only include the songs based on the user mood creating a new dataframe called mood_df. The songs in the mood_df are then sorted on the song rating in descending order and the top five songs (the ones with the highest rating and user’s mood) are copied to top_songs.

Recommending mood based popular songs The titles of these top 5 songs are then displayed as recommendations.

After the respective functions are called and executed to display the recommended songs the execution of while loop continues.

Movies Recommendation System If the choice is movie recommendation:

The basic steps are all the same as in the Music recommender- the csv file is loaded into a dataframe object. A while loop is called to ask for either content based or popularity-based recommendations. Please choose one of the following options for your recommendation:-

Press 1 for content-based recommendation
Press 2 for popularity-based recommendation
The loop keeps executing until the user wants otherwise and keeps recommending movies based on user’s choice.

Content-based Movie recommendation Similarly, a matrix of TF-IDF features is created from the columns genre and director of the dataset for each movie. The genre and director columns in the dataframe with Null values are substituted with empty strings so as to avoid any errors. Fit_transform function is used to vectorize these dataframe columns from string to matrix with tfidf features.

Tfidf vectorization and Similarity calculation The user is asked for a previously watched movie which is then searched in the dataset and if found the user is asked if they want recommendation based on genre, director or both. Cosine similarity is applied on respective tfidf matrices as per the user choice. In case of ‘both’ the similarity scores are added.

Similarity Scores List The index of the user entered movie is found and the user is asked the number of recommendations they want. A list of tuples of all movies is created of the format (song-index, similarity score) with respect to the user entered movie title. This list of tuples is then sorted in descending order on the basis of these similarity scores. The top n number of movies are copied to another list excluding the user entered movie title.

The recommended movies are then printed with an appropriate message.

Popularity-based Movie recommendation If the user wants recommendations based on popularity the following function is called. Firstly the choice of user genre is asked and the dataset is filtered to include only movies with that particular genre. If there are no movies of that genre a message is displayed else the dataset is sorted based on the imdb ratings of the movies and top five movies are copied to another list.

The titles of the recommended movies are then displayed
