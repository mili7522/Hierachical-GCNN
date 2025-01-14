import pandas as pd
import os

os.chdir('Data')

data = pd.read_csv('2018-08-28-NSW-SA2Input.csv', index_col = 0)

# Filter just those SA1s in the giant component
# SA1s = pd.read_csv('Geography/2018-08-28-NSW-SA2s.csv', squeeze = True, header = None)
# data = data.loc[SA1s]

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-08-28-NSW-SA2Input-Normalised.csv')


### SA3
data = pd.read_csv('2018-09-05-NSW-SA3Input.csv', index_col = 0)

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-09-05-NSW-SA3Input-Normalised.csv')


### SA4
data = pd.read_csv('2018-09-05-NSW-SA4Input.csv', index_col = 0)

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-09-05-NSW-SA4Input-Normalised.csv')


##### Normalise with Additional Features
data = pd.read_csv('2018-09-05-NSW-SA2Input-Expanded.csv', index_col = 0)

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-09-05-NSW-SA2Input-Expanded-Normalised.csv')


### SA3
data = pd.read_csv('2018-09-05-NSW-SA3Input-Expanded.csv', index_col = 0)

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-09-05-NSW-SA3Input-Expanded-Normalised.csv')


### SA4
data = pd.read_csv('2018-09-05-NSW-SA4Input-Expanded.csv', index_col = 0)

mean = data.mean()
std = data.std()

data_normalised = (data - mean) / std
data_normalised['2PP'] = data['2PP']

data_normalised.to_csv('2018-09-05-NSW-SA4Input-Expanded-Normalised.csv')