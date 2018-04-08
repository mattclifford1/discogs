import pandas as pd

def list_to_string(listt):
	string = ''
	for i in range(len(listt)):
		string += listt[i]
		string += ' '
	return string


lyrics = pd.read_pickle('lyrics_genre_overlap.pkl')
indicies = lyrics.index.tolist()   #get indicies (removes some so not in counting up evently)

string_of_lyrics = [0]*len(indicies)
count = 0
for i in indicies:
	string_of_lyrics[count] = list_to_string(lyrics['lyrics'][i])
	count +=1
print(string_of_lyrics[0])
	#do LDA