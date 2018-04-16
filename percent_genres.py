# import pickle
import pandas as pd

def genre_percentages(data):
	labels = data['discogs_genre'].tolist()
	unique = list(set(labels))
	count = [0]*len(unique)
	percentage = [0]*len(unique)

	for i in range(len(labels)):
		ind = unique.index(labels[i])  
		count[ind] += 1
	total = sum(count)
	for i in range(len(count)):
		percentage[i] = count[i]*100/total

	data = [0]*len(unique)
	columns = ['number', 'percentage']

	for i in range(len(unique)):
		data[i] = [count[i], percentage[i]]
	df = pd.DataFrame(data, index=unique, columns = columns)
	print(df)

# if __name__ == "__main__":
# 	labels = pickle.load(open('even_lyrics_genres.pkl', 'rb'))
# 	print('lyrics')
# 	genre_percentages(labels)

# 	labels3 = pickle.load(open('classes.pkl', 'rb')).tolist()
# 	print('\nall')
# 	genre_percentages(labels3)