import pandas as pd


def create_frame(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:'s', 'E', 'p']
    df.columns = ['Symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time.to_datetime(df.Time, unit='ms')
    return df
