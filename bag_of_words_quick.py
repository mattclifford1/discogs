import pandas as pd
import pickle
import numpy as np

data = pd.read_pickle('lyrics_genre_overlap.pkl')
indicies = data.index.tolist()   #get indicies (removes some so not in counting up evently)
list_of_lyrics = [0]*len(indicies)
count = 0
genres = data['discogs_genre'].tolist()
for i in indicies:
	list_of_lyrics[count] = data['lyrics'][i]
	count +=1
	
from gensim import corpora

dictionary = corpora.Dictionary(list_of_lyrics)
corpus = [dictionary.doc2bow(text) for text in list_of_lyrics]

max_ = 0
for i in range(len(corpus)):
	for j in range(len(corpus[i])):
		if corpus[i][j][0] > max_:
			max_ = corpus[i][j][0]

features = np.zeros([len(indicies), (max_+1)], dtype = int)

for i in range(len(corpus)):
	for j in range(len(corpus[i])):
		features[i, corpus[i][j][0]] = int(corpus[i][j][1] )

df = pd.DataFrame(features, index=indicies)
df['discogs_genre'] = genres
df.to_pickle('bag_of_words.pkl')
pickle.dump(data['discogs_genre'].tolist(), open('lyrics_genres.pkl', 'wb'))
