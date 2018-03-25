#FIRST: pip install discogs_client
import discogs_client as dc
import numpy as np
from tqdm import tqdm
import time
import csv

ds = dc.Client('/find_genre/1.0', user_token='YNwyLvHlapVHyZWnigBSOMRiiMLUpKuyPAESeLDT')

data2=np.load('data.npy')

genre_list=[]

for i in tqdm(range(10000)):
    song_data = data2[0][i]
    artist_data = data2[1][i]
    track_data = data2[12][i]
    results = ds.search(str(artist_data)  + ' - ' + str(song_data), type = 'release')
    try:
        genre = results[0].genres
    except IndexError:
        genre = []
    genre_list.append([track_data, genre])
    time.sleep(1)

with open('discogs_genre_list.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Track ID', 'Discogs Genre'])
    for row in genre_list:
        csv_out.writerow(row) 


#Can get all of these
#['__class__',
# '__delattr__',
# '__dict__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__gt__',
# '__hash__',
# '__init__',
# '__init_subclass__',
# '__le__',
# '__lt__',
# '__module__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# '__weakref__',
# '_known_invalid_keys',
# 'artists',
# 'changes',
# 'client',
# 'companies',
# 'country',
# 'credits',
# 'data',
# 'data_quality',
# 'delete',
# 'fetch',
# 'formats',
# 'genres',
# 'id',
# 'images',
# 'labels',
# 'master',
# 'notes',
# 'refresh',
# 'repr_str',
# 'save',
# 'status',
# 'styles',
# 'thumb',
# 'title',
# 'tracklist',
# 'url',
# 'videos',
# 'year']
