import pandas as pd
from tsfresh import extract_features
from tqdm import tqdm

removed_missing = True
if removed_missing == False:
	data = pd.read_pickle('data_with_lyrics_discogs.pkl')
	#get rid of any songs without a genre
	for i in tqdm(range(len(data))):
		if data['discogs_genre'][i] == '':
			data = data.drop(i)
	data.to_pickle('data_only_genre.pkl')

sort_time_series = True
if sort_time_series == False:
	#load data with missing genres removed
	data = pd.read_pickle('data_only_genre.pkl')

	#get column names and indicies for future use
	columns = data.columns.tolist()
	indices = data.index.tolist()

	classes = pd.Series(data['discogs_genre'].tolist())
	classes.to_pickle('classes.pkl', protocol=2)   #for python 2

	time_series = pd.DataFrame()

	features = ['timbre','pitches','tatum','seg_loudness_max','beats','bars','sections','segments','loud_start','loud_time']
	features = ['timbre']
	for feat in features:
		current_feature = data[feat].tolist()
		dims = current_feature[0].shape[1]
		for dim in range(dims):  #12 is dim of timbre
			flat_features = []
			ids = []
			for i in tqdm(range(len(current_feature))):
			# for i in tqdm(range(10)):
				current_song = current_feature[i]
				flat_features += list(current_song[:,dim])
				ids += [i]*len(current_song)
			time_series[str(dim)] = flat_features
		time_series['id'] = ids

	time_series.to_pickle('time_series.pkl', protocol=2)  #for python 2

time_series = pd.read_pickle('time_series.pkl')
classes = pd.read_pickle('classes.pkl')

import multiprocessing
num_cores = multiprocessing.cpu_count()

# from tsfresh.utilities.distribution import MultiprocessingDistributor
# Distributor = MultiprocessingDistributor(n_workers=num_cores, disable_progressbar=False, progressbar_title="Feature Extraction")

# from tsfresh import extract_features
from tsfresh.feature_extraction import extract_features, MinimalFCParameters
extracted_features = extract_features(time_series, column_id="id",n_jobs=num_cores, default_fc_parameters=MinimalFCParameters())
#use this one below for parrellel processing
# extracted_features = extract_features(timeseries_container=time_series,column_id='id',distributor=Distributor)
import pickle
pickle.dump(extracted_features, open('extracted_features.pkl', 'wb'))
# extracted_features = pickle.load(open('extracted_features.pkl', 'rb')

from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute

impute(extracted_features)
features_filtered = select_features(extracted_features, classes)
pickle.dump(features_filtered, open('filtered_features.pkl', 'wb'))
# features_filtered = pickle.load(open('filtered_features.pkl', 'rb')








