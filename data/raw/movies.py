import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv"

df = pd.read_csv(url)

df.to_csv('movies.csv', index=False)
print("Dataset saved as 'movies.csv'")