from datetime import date

import pandas as pd

from config import Config

Config.ENRICHED_DATA_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(str(Config.PREPARED_DATA_FILE_PATH))

# Last Week Sales: this is simply the amount of sales that a product had in the previous week
# Last Week Diff: the difference between the amount of sales in the previous week and the week before it (t-1 - t-2)

data['Last_Week_Sales'] = data.groupby(['Product_Code'])['Sales'].shift()
data['Last_Week_Diff'] = data.groupby(['Product_Code'])['Last_Week_Sales'].diff()
data = data.dropna()

data.to_csv(str(Config.ENRICHED_DATA_FILE_PATH), index=None)