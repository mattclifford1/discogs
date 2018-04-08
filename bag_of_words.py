import pandas as pd
data = pd.read_pickle('lyrics_genre_overlap2.pkl')

indices = data.index.tolist()
lyrics_list_all = [0]*len(indices)
count = 0
for i in indices:
    lyrics_list_all[count] = data['lyrics'][i]
    count += 1
import itertools
merged_lyrics_list = list(itertools.chain(*lyrics_list_all))
lyrics_list = list(set(merged_lyrics_list))


for i in lyrics_list:
    data[i]= 0*len(data)
count = 0

for i in indices:
##    print(i)
    for j in lyrics_list_all[i]:
    #        print(j)
    #        print(type(j))
        data[j][i]+=1
        count+=1
        if count % 1000 == 0:
            print(count)
        
data.to_pickle('bag_of_words.pkl')
