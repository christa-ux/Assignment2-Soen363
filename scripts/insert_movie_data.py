import psycopg2

def insert_movie_data(movie_data):
    try:
        conn = psycopg2.connect(
            dbname="Assignment2-Soen363",
            user="postgres",
            password="Postgres@123",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Extract main movie details
        tmdb_id = movie_data.get('tmdbID')
        imdb_id = movie_data.get('imdbID')  # Ensure this is a string
        title = movie_data.get('title', 'Unknown')
        plot = movie_data.get('plot', 'No plot available')
        release_year = movie_data.get('year', 0)
        content_rating = movie_data.get('contentRating', 'N/A')
        viewer_rating = movie_data.get('rating', 0.0)
        original_language = movie_data.get('language', 'Unknown')

        # Get rID for contentRating
        cursor.execute("SELECT rID FROM contentRating WHERE rating = %s", (content_rating,))
        content_rating_id = cursor.fetchone()

        if content_rating_id:
            content_rating_id = content_rating_id[0]
        else:
            print(f"Content rating '{content_rating}' not found in the database.")
            return

        # Insert movie data into the Movie table
        cursor.execute("""
            INSERT INTO Movie (tmdbID, imdbID, title, plot, releaseYear, contentRating, viewerRating, original_language)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING mID
        """, (tmdb_id, imdb_id, title, plot, release_year, content_rating_id, viewer_rating, original_language))
        movie_id = cursor.fetchone()[0]

        # Commit the transaction
        conn.commit()
        cursor.close()
        conn.close()

        print(f"Inserted movie: {title}")
    
    except Exception as e:
        print(f"Error inserting movie data: {e}")

# Example movie data for testing
example_movie_data = {
    'tmdbID': 238,
    'imdbID': 'tt0068646',
    'title': 'The Godfather',
    'plot': 'The aging patriarch...',
    'year': 1972,
    'contentRating': 'R',
    'rating': 9.2,
    'language': 'English',
    'genres': ['Crime', 'Drama'],
    'actors': ['Marlon Brando', 'Al Pacino'],
    'directors': ['Francis Ford Coppola']
}

insert_movie_data(example_movie_data)
