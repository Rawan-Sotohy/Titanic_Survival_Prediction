# Data Processing
import os
import pandas as pd

# Define file paths
RAW_TRAIN_PATH = os.path.join('data', 'raw', 'train.csv')
RAW_TEST_PATH = os.path.join('data', 'raw', 'test.csv')
PROCESSED_TRAIN_PATH = os.path.join('data', 'processed', 'train_clean.csv')
PROCESSED_TEST_PATH = os.path.join('data', 'processed', 'test_clean.csv')


def load_raw_data():
    """Load raw train and test CSV files."""
    train_df = pd.read_csv(RAW_TRAIN_PATH)
    test_df = pd.read_csv(RAW_TEST_PATH)
    return train_df, test_df


def clean_data(df):
    df = df.copy()

    # ===> Missing Values Handling <===
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    if 'Fare' in df.columns:
        df['Fare'].fillna(df['Fare'].median(), inplace=True)

    # ===> Feature Engineering <===
    df['HasCabin'] = df['Cabin'].notnull().astype(int)

    # ===> Encoding Categorical Features <===
    # Sex: Label Encoding
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    # Embarked: One-Hot Encoding
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

    # Title: Extract from Name and One-Hot Encode
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace(['Mme', 'Lady', 'Countess', 'Dona'], 'Mrs')
    df['Title'] = df['Title'].replace(['Dr', 'Rev', 'Major', 'Col', 'Capt', 'Don', 'Jonkheer', 'Sir'], 'Rare')
    df = pd.get_dummies(df, columns=['Title'], drop_first=True)

    # ===>Drop Irrelevant Columns <===
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

    return df


def save_clean_data(train_df, test_df):

    os.makedirs(os.path.join('data', 'processed'), exist_ok=True)
    train_df.to_csv(PROCESSED_TRAIN_PATH, index=False)
    test_df.to_csv(PROCESSED_TEST_PATH, index=False)


if __name__ == "__main__":
    # Load raw data
    train_df, test_df = load_raw_data()

    # Clean data
    train_clean = clean_data(train_df)
    test_clean = clean_data(test_df)

    # Save cleaned data
    save_clean_data(train_clean, test_clean)
