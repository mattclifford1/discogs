import pandas as pd

data = pd.read_pickle('data_only_genre.pkl')
ind = data.index.tolist()

timbre = pd.DataFrame(data['timbre'].tolist(), index = ind,columns=['timbre'])
timbre['discogs_genre'] =  data['discogs_genre'].tolist()

timbre.to_pickle('just_timbre.pkl')