import pandas as pd
from percent_genres import genre_percentages
from genre_add import make_even
from gensim import corpora
import pickle
import gensim
import numpy as np


def list_to_string(listt):
	string = ''
	for i in range(len(listt)):
		string += listt[i]
		string += ' '
	return string

def get_topics(lyrics, NUM_TOPICS):

	genres = lyrics['discogs_genre'].tolist()

	indicies = lyrics.index.tolist()   #get indicies (removes some so not in counting up evently)
	string_of_lyrics = [0]*len(indicies)
	list_of_lyrics = [0]*len(indicies)
	count = 0
	for i in indicies:
		string_of_lyrics[count] = list_to_string(lyrics['lyrics'][i])
		list_of_lyrics[count] = lyrics['lyrics'][i]
		count +=1
	# dictionary = [dictionary.doc2bow(text) for text in text_data]
	dictionary = corpora.Dictionary(list_of_lyrics)
	corpus = [dictionary.doc2bow(text) for text in list_of_lyrics]

	
	# pickle.dump(corpus, open('corpus.pkl', 'wb'))
	# pickle.dump(list_of_lyrics, open('list_of_lyrics.pkl', 'wb'))
	# dictionary.save('dictionary.gensim')

	
	# NUM_TOPICS = 40
	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
	# ldamodel.save('model5.gensim')
	topics = ldamodel.print_topics(num_words=10)
	# for topic in topics:
	#     print(topic)

	visulise = False
	if visulise == True:
		dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
		corpus = pickle.load(open('corpus.pkl', 'rb'))
		lda = gensim.models.ldamodel.LdaModel.load('model5.gensim')
		import pyLDAvis.gensim
		lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
		pyLDAvis.save_html(lda_display,'LDA')

	features = np.zeros([len(list_of_lyrics) ,NUM_TOPICS])  #create topic probabily for songs matrix
	#assign topic probabilities for each 'document' (lyrics of song)
	for i in range(len(list_of_lyrics)):
		bow = dictionary.doc2bow(list_of_lyrics[i]) 
		probs = ldamodel.get_document_topics(bow)
		for j in range(len(probs)):
			topic = probs[j][0]    #find topic number from index
			features[i][topic] = probs[j][1]   #assign probability of that topic
	# np.save('features.npy',features)
	df = pd.DataFrame(features,index=indicies)
	df['discogs_genre'] = genres
	return df

if __name__ == "__main__":
	lyrics = pd.read_pickle('lyrics_genre_overlap.pkl')

	genre_percentages(lyrics)
	#make genres even
	lyrics =  make_even(lyrics, max_number = 134, reduce_genres = ['Rock','Pop','Folk, World, & Country', 'Hip Hop','Electronic'])
	genre_percentages(lyrics)

	get_topics(lyrics, 40)
	df.to_pickle('topics_features_df.pkl')







