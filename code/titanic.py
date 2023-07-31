import pandas as pd
from tabulate import tabulate

# Parameter setup.
train_data_path = './../data/train.csv'
test_data_path = './../data/test.csv'

# EDA
# Load data.
train_data = pd.read_csv(train_data_path)
x_train = train_data.drop('Survived', axis=1)
y_train = train_data.Survived

# Present data.
print(train_data.sample(20))

# Find all missing values.

# Plot histogram of possible values in each variable.
