#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

traces = np.load(r'data/traces.npy')

corr_features = set()
traces = pd.DataFrame(traces)
# create the correlation matrix (default to pearson)
corr_matrix = traces.corr(method='pearson')

print('traces.corr(method=''pearson'') done')
# optional: display a heatmap of the correlation matrix
# plt.figure(figsize=(50,50))
# sns.heatmap(corr_matrix)
# plt.show()

for i in range(len(corr_matrix .columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.5:
            colname = corr_matrix.columns[i]
            corr_features.add(colname)
            
traces.drop(labels=corr_features, axis=1, inplace=True)
# tracesTest.drop(labels=corr_features, axis=1, inplace=True)
traces = np.array(traces)
np.save('data/traces_50features', traces)
print('tracesTrain',np.array(traces).shape)
# print(corr_features)