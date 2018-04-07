import pandas as pd

columns_data = ['title','artist','lat','lon','hot','dance','duration','energy','key','loudness','tempo','year','timbre','time_sig','pitches','tatum','seg_loudness_max','beats','bars','sections','segments','loud_start','loud_time','track_id']
columns_discogs = ['track_id','discogs_genre']

data = pd.read_csv('data2.csv')
discogs = pd.read_csv('discogs_genre_list.csv')


data['discogs_genre'] = discogs['discogs_genre']
# data['discogs_one_genre'] = discogs['discogs_genre']
# for i in range(len(data['discogs_genre'])):
# 	if data['discogs_one_genre'][i] != '[]':
# 		data['discogs_one_genre'][i] = data['discogs_genre'][i][0]

print(data)





data.to_csv('data_with_discogs.csv',index=False)