# Data Processing
import pandas as pd
import os

train_path = os.path.join('data', 'raw', 'train.csv')
test_path = os.path.join('data', 'raw', 'test.csv')

if __name__ == "__main__":
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
