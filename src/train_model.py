import math
import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error

from config import Config

Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(str(Config.ENRICHED_DATA_FILE_PATH))

valid_begin = math.ceil(
    np.percentile(data.Week.unique(), (1 - Config.VALID_FRACTION) * 100)
)

train = data[data["Week"] < valid_begin]

X = train.drop(["Sales"], axis=1)
y = train["Sales"].values

model = RandomForestRegressor(n_estimators=1000, n_jobs=-1, random_state=0)
model.fit(X, y)

pickle.dump(model, open(str(Config.MODELS_PATH / "model.pickle"), "wb"))
