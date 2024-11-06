# part 2 (API consumer; script to fetch data)


import requests
import json

# Function to get movie data from IMDb API
def get_movie_data(imdb_id):
   
    url = f"https://search.imdbot.workers.dev/?tt={imdb_id}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            movie_data = response.json()  # Parse the JSON response
            return movie_data
        else:
            print(f"Failed to retrieve data for {imdb_id}. HTTP status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {imdb_id}: {e}")
        return None

# Example usage - Replace this with the actual IMDb IDs you want to process
imdb_id = "tt0068646"  # Example IMDb ID for The Godfather
movie_data = get_movie_data(imdb_id)

if movie_data:
    # Print or store the movie data (you can save it as a JSON file if needed)
    print(json.dumps(movie_data, indent=4))
else:
    print("No data returned for this IMDb ID.")