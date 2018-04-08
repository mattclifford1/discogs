import pandas as pd
from tqdm import tqdm

data = pd.read_pickle('data_with_lyrics_discogs.pkl')

for i in tqdm(range(len(data))):
	if data['lyrics'][i] == 0 or data['discogs_genre'][i] == '':
		data = data.drop(i)

print(data)

data.to_pickle('lyrics_genre_overlap2.pkl', protocol=2)

