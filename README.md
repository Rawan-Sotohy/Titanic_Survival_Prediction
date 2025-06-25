# Titanic Survival Prediction 🚢

A machine learning project that predicts the survival of passengers on the Titanic using the classic Kaggle dataset.

## 📁 Project Structure

```

titanic-survival-prediction/
│
├── data/
│   ├── raw/             # Original raw CSV files (train/test)
│   └── processed/       # Cleaned data used for training
│
├── notebooks/           # Jupyter Notebooks
│   └── titanic_eda.ipynb
│
├── src/
│   ├── __init__.py       
|   ├── data.py          # Data loading and cleaning
│   ├── features.py      # Feature engineering
│   ├── model.py         # Model training and evaluation
│   ├── predict.py       # Make predictions on new/unseen data
|   └── visualization/   # Data analysis and plotting scripts
|       ├── eda.py       # Exploratory Data Analysis (EDA)
│       └── plots.py     # Accuracy, confusion matrix, and other 
│
│
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md

````

## 📊 Dataset

This project uses the Titanic dataset from [Kaggle](https://www.kaggle.com/c/titanic). It contains demographic and passenger information from 891 passengers.

## 📈 Model



## 🧪 Usage

To train the model:

```bash
python src/model.py
```

To make predictions:

```bash
python src/predict.py
```

## ✍️ Author

* Rawan Sotohy
