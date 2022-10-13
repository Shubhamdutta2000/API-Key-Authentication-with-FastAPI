import pandas as pd

def conv(response):
    df_dict = pd.DataFrame(response).to_dict(orient="list")
    return df_dict
