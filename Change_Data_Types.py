import pandas as pd


def change_dtypes(df):
    resized_df = df.copy()
    for col in resized_df.columns:
        if resized_df[col].dtype == 'int64' or df[col].dtype == 'float64':
            num_min = resized_df[col].min()
            num_max =  resized_df[col].max()
            if df[col].dtype == 'int64':
                if num_min >= -128 and num_max <= 127:
                    resized_df[col] = resized_df[col].astype('int8')
                elif num_min >= -32768 and num_max <= 32767:
                    resized_df[col] = resized_df[col].astype('int16')
                elif num_min >= -2147483648 and num_max <= 2147483647:
                    resized_df[col] = resized_df[col].astype('int32')
            elif resized_df[col].dtype == 'float64':
                if num_min >= 5.96e-08 and num_max <= 65500:
                    resized_df[col] = resized_df[col].astype('float16')
                elif num_min >= 1.18e-38 and num_max <= 3.4e38:
                    resized_df[col] = resized_df[col].astype('float32')
        elif col == 'date':
            resized_df[col] = pd.to_datetime(resized_df[col], format='%Y-%m-%d')
            resized_df[col] = df[col].dt.date
        elif df[col].dtype == 'O':
            resized_df[col] = pd.Categorical(resized_df[col])
            
    return resized_df
