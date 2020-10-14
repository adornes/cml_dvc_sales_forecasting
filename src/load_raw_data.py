import gdown
import numpy as np
import pandas as pd

from config import Config

Config.RAW_DATA_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

gdown.download(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00396/Sales_Transactions_Dataset_Weekly.csv",
    str(Config.RAW_DATA_FILE_PATH),
)

df = pd.read_csv(str(Config.RAW_DATA_FILE_PATH))

print(f"INFO: Raw data successfully loaded with {df.shape[0]} rows and {df.shape[1]} columns")