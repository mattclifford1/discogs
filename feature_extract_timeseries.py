import pandas as pd
from tsfresh import extract_features
from tqdm import tqdm
data = pd.read_pickle('data_with_lyrics_discogs.pkl')

#get rid of any songs without a genre
for i in tqdm(range(len(data))):
	if data['discogs_genre'][i] == '':
		data = data.drop(i)
data.to_pickle('data_only_genre.pkl')

data = pd.read_pickle('data_only_genre.pkl')
#get column names and incicies for future use
columns = data.columns.tolist()
indices = data.index.tolist()


genre = data['discogs_genre'].tolist()



timbre = data['timbre'].tolist()
