import requests
import json

def get_movie_data(imdb_id):
    url = f"https://search.imdbot.workers.dev/?tt={imdb_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()
            return movie_data
        else:
            print(f"Failed to retrieve data for {imdb_id}. HTTP status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {imdb_id}: {e}")
        return None

# List of IMDb IDs for testing
imdb_ids = ["tt0068646", "tt0108052", "tt0111161"]  # Add more IDs as needed

movies = []
for imdb_id in imdb_ids:
    data = get_movie_data(imdb_id)
    if data:
        movies.append(data)

# Print all collected data for verification
print(json.dumps(movies, indent=4))
