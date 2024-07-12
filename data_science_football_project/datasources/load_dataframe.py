import pandas as pd

def get_football_kaggle_data() -> pd.DataFrame:
    """
    Get the football kaggle data in the football.csv file.
    
    Return:
        pd.DataFrame: The football kaggle data.
    """
    return pd.read_csv("./data/football.csv")
