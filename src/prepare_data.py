from datetime import date

import pandas as pd

from config import Config

Config.PREPARED_DATA_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

raw_data = pd.read_csv(str(Config.RAW_DATA_FILE_PATH))

# Product Code and non-normalized weekly sales for each product
data = raw_data.filter(regex=r"Product|W")

# Reshape to timeseries structure
melt = data.melt(id_vars="Product_Code", var_name="Week", value_name="Sales")

melt["Product_Code"] = (
    melt["Product_Code"].str.extract(r"(\d+)", expand=False).astype(int)
)
melt["Week"] = melt["Week"].str.extract(r"(\d+)", expand=False).astype(int)

# Ensure timeline is respected
melt = melt.sort_values(["Week", "Product_Code"])

melt.to_csv(str(Config.PREPARED_DATA_FILE_PATH), index=None)
