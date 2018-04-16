import pandas as pd

data = pd.read_pickle('bag_of_words.pkl')
del_column = ['title','artist', 'lat', 'lon', 'hot', 'dance', 'duration', 'energy', 'key', 'loudness', 'tempo', 'year', 'timbre', 'time_sig', 'pitches', 'tatum', 'seg_loudness_max', 'beats', 'bars', 'sections', 'segments', 'loud_start', 'loud_time', 'track_id', 'lyrics', 'discogs_genre']
for col in del_column:
	data = data.drop(col, 1)
data.to_pickle('just_bag_of_words.pkl',protocol=2)
