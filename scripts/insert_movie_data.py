import psycopg2

# Function to insert movie data into PostgreSQL
def insert_movie_data(movie_data):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="Assignment2-Soen363",  
            user="postgres",
            password="Postgres@123",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        
        # Extract relevant fields from the movie data
        title = movie_data.get('title', 'Unknown')
        plot = movie_data.get('plot', 'No plot available')
        release_year = movie_data.get('year', 0)
        contentRating = movie_data.get('contentRating', 'N/A')
        viewer_rating = movie_data.get('rating', 0.0)
        original_language = movie_data.get('language', 'Unknown')

        # Insert data into the Movie table
        cursor.execute("""
            INSERT INTO Movie (title, plot, releaseYear, contentRating, viewerRating, original_language)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, plot, release_year, contentRating, viewer_rating, original_language))
        
        # Commit the transaction
        conn.commit()
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
        print(f"Inserted movie: {title}")
    
    except Exception as e:
        print(f"Error inserting movie data: {e}")

# Example usage
# You would get movie data from fetch_movie_data.py, here we simulate the movie data
movie_data = {
    'title': 'The Godfather',
    'plot': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
    'year': 1972,
    'contentRating': 'R',
    'rating': 9.2,
    'language': 'English'
}


insert_movie_data(movie_data)
