import pandas as pd
from tqdm import tqdm
import pickle

data = pd.read_pickle('even_data_with_lyrics_discogs.pkl')
indexes = data.index.tolist()

for i in indexes:
	if data['lyrics'][i] == 0 or data['discogs_genre'][i] == '':
		data = data.drop(i)

print(data)

data.to_pickle('even_lyrics_genre_overlap.pkl', protocol=2)

genre = data['discogs_genre'].tolist()
pickle.dump(genre, open('even_lyrics_genres.pkl', 'wb'))