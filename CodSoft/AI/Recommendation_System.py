import numpy as np
import pandas as pd

# Load user-item ratings matrix (replace with your data)
ratings = np.array([[4, 5, 0, 1],
                    [3, 0, 4, 4],
                    [1, 2, 3, 5],
                    [0, 3, 4, 3]])

# Calculate user-user similarity matrix (adjust similarity metric as needed)
user_similarity = np.corrcoef(ratings)

def recommend_movies_for_user(user_id):
    # Find similar users
    similar_users = np.argsort(-user_similarity[user_id])[1:]  # Exclude self

    # Recommend movies liked by similar users that the user hasn't rated yet
    recommended_movies = []
    for similar_user in similar_users:
        for movie_id in range(len(ratings[similar_user])):
            if ratings[user_id, movie_id] == 0 and ratings[similar_user, movie_id] > 3:  # Adjust rating threshold
                recommended_movies.append(movie_id)
    return recommended_movies

# Load item features (replace with your data)
books = pd.DataFrame({'title': ['The Martian', 'Project Hail Mary', 'Dune'],
                      'genre': ['sci-fi', 'sci-fi', 'sci-fi'],
                      'author': ['Andy Weir', 'Andy Weir', 'Frank Herbert']})

def recommend_books_based_on_features(book_title):
    # Get features of the target book
    target_book_features = books.loc[books['title'] == book_title]

    # Calculate similarity between the target book and other books based on features
    book_similarities = books.apply(lambda row: calculate_similarity(row, target_book_features), axis=1)

    # Recommend the most similar books
    recommended_books = books.sort_values(by=book_similarities, ascending=False)['title'].tolist()[1:]  # Exclude self
    return recommended_books

def calculate_similarity(book1, book2):
    # Implement your similarity calculation here (e.g., based on genres, authors, keywords)
    # ...
    return similarity_score
