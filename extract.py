#!/usr/bin/env python3
import numpy as np
import h5py
import os
import os.path
import sys

def extract(filePath):
	try:
			in_file	 = h5py.File(filePath, "r")
	except:
			print("Error: can't open HDF5 file for reading (it might be malformed) ...")
			sys.exit(-1)

	# Profiling_traces = in_file['Profiling_traces']
	raw_traces = in_file['traces']
	# np.delete(raw_traces, [2000], axis=1)
	raw_traces = raw_traces[0:60000,0:1000]
	print(raw_traces.shape)
	raw_data = in_file['metadata']
	raw_plaintexts = raw_data['plaintext']
	raw_keys = raw_data['key']
	raw_masks = raw_data['masks']

	np.save('data/traces', raw_traces)
	np.save('data/plain', raw_plaintexts)
	np.save('data/key', raw_keys)
	np.save('data/masks', raw_masks)


print('extracting arrays to files...\n')
extract('data/ATMega8515_raw_traces.h5')
print('done succesfully.')