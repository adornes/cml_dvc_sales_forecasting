from pathlib import Path


class Config:
    RANDOM_SEED = 42
    VALID_FRACTION = 0.2
    ASSETS_PATH = Path("./assets")
    RAW_DATA_FILE_PATH = (
        ASSETS_PATH / "raw_data" / "Sales_Transactions_Dataset_Weekly.csv"
    )
    PREPARED_DATA_FILE_PATH = ASSETS_PATH / "prepared_data" / "prepared_data.csv"
    ENRICHED_DATA_FILE_PATH = ASSETS_PATH / "enriched_data" / "enriched_data.csv"
    MODELS_PATH = ASSETS_PATH / "models"
    METRICS_FILE_PATH = ASSETS_PATH / "metrics.json"
