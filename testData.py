import os
import glob
import hdf5_getters
import numpy as np

def get_all_titles(basedir,songNum,ext='.h5') :
	title = [0]*songNum
	artist = [0]*songNum
	lat = [0]*songNum
	lon = [0]*songNum
	hot = [0]*songNum
	dance = [0]*songNum
	duration = [0]*songNum
	energy = [0]*songNum
	key = [0]*songNum
	loudness = [0]*songNum
	tempo = [0]*songNum
	year = [0]*songNum
	track_ID = [0]*songNum
	i = 0
	for root, dirs, files in os.walk(basedir): #iterate over all the folders
		files = glob.glob(os.path.join(root,'*'+ext))
		for f in files:      #to do ..... convert to ints......
			h5 = hdf5_getters.open_h5_file_read(f)
			title[i] = str(hdf5_getters.get_title(h5))
			artist[i] = str(hdf5_getters.get_artist_name(h5))
			lat[i] = float(hdf5_getters.get_artist_latitude(h5))
			lon[i] = float(hdf5_getters.get_artist_longitude(h5))
			hot[i] = float(hdf5_getters.get_song_hotttnesss(h5))
			dance[i] = float(hdf5_getters.get_danceability(h5))
			duration[i] = float(hdf5_getters.get_duration(h5))
			energy[i] = float(hdf5_getters.get_energy(h5))
			key[i] = float(hdf5_getters.get_key(h5))
			loudness[i] = float(hdf5_getters.get_loudness(h5))
			tempo[i] = float(hdf5_getters.get_tempo(h5))
			year[i] = float(hdf5_getters.get_year(h5))
			track_ID[i] = str(hdf5_getters.get_track_id(h5))
        		print(hdf5_getters.get_segments_timbre(h5))    
			h5.close()
			i += 1
			if i % 1000 == 0:
				print(i)
	return [title,artist,lat,lon,hot,dance,duration,energy,key,loudness,tempo,year, track_ID]

def count_all_files(basedir,ext='.h5') :
	cnt = 0
	for root, dirs, files in os.walk(basedir):
		files = glob.glob(os.path.join(root,'*'+ext))
		cnt += len(files)
	return cnt

cwd = os.getcwd()
d = os.path.join(cwd,'MillionSongSubset')
# directory = os.path.join(cwd,'MillionSongSubset')
# tracks = os.path.join(directory,'AdditionalFiles/subset_unique_tracks.txt')
# f = open(tracks,'r')

# # f = open('subset_unique_artists.txt','r')
# for line in f.xreadlines():
#     parts = line.strip().split('<SEP>')
#     if len(parts)>3 and parts[3] == 'Radiohead':
#         print('Radiohead track:',parts[2])
#         break
# f.close()

songNum = count_all_files(d)
data = get_all_titles(d, songNum)
array = np.array(data)
np.save('data.npy',data)
