import json
import math
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_squared_log_error

from config import Config


# Root Mean Squared Log Error (RMSLE) metric function
def rmsle(ytrue, ypred):
    return np.sqrt(mean_squared_log_error(ytrue, ypred))


data = pd.read_csv(str(Config.ENRICHED_DATA_FILE_PATH))

valid_begin = math.ceil(
    np.percentile(data.Week.unique(), (1 - Config.VALID_FRACTION) * 100)
)

val = data[data["Week"] >= valid_begin]

X = val.drop(["Sales"], axis=1)
y = val["Sales"].values

model = pickle.load(open(str(Config.MODELS_PATH / "model.pickle"), "rb"))

r_squared = model.score(X, y)

y_pred = model.predict(X)

rmse = math.sqrt(mean_squared_error(y, y_pred))
rmsle = rmsle(y, y_pred)

with open(str(Config.METRICS_FILE_PATH), "w") as outfile:
    json.dump(dict(r_squared=r_squared, rmse=rmse, rmsle=rmsle), outfile)
