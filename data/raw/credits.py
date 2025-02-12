import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv"

df = pd.read_csv(url)

df.to_csv('credits.csv', index=False)
print("Dataset saved as 'credits.csv'")