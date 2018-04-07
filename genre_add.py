import pandas as pd
from tqdm import tqdm

data = pd.read_pickle('data2.pkl')
data['lyrics'] = [0]*len(data)
data['discogs_genre'] = [0]*len(data)
lyrics_df = pd.read_pickle('matt_lyrics.pkl')
discogs_genre = pd.read_pickle('discogs_genre_convert.pkl')

for i in tqdm(range(len(lyrics_df))):
	a = data['track_id'][data['track_id'] == lyrics_df.loc[i,0]]
	index = int(a.index.get_values())
	data['lyrics'][index] = lyrics_df.loc[i,1]

for i in tqdm(range(len(discogs_genre))):
	a = data['track_id'][data['track_id'] == discogs_genre[i][0]]
	if len(a) > 0:
		index = int(a.index.get_values())
		data['discogs_genre'][index] = discogs_genre[i][1]

print(data)
data.to_pickle('data_with_lyrics_discogs.pkl')
# data = pd.read_csv('data2.csv')
# discogs = pd.read_csv('discogs_genre_list.csv')


# data['discogs_genre'] = discogs['discogs_genre']
# data['discogs_one_genre'] = discogs['discogs_genre']
# for i in range(len(data['discogs_genre'])):
# 	if data['discogs_one_genre'][i] != '[]':
# 		data['discogs_one_genre'][i] = data['discogs_genre'][i][0]






# data.to_csv('data_with_discogs.csv',index=False)