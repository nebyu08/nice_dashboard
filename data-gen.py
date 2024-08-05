import pandas as pd
import numpy as np
def generate_boolean_values(num_rows,num_cols):
    """this is used for genrating fake values for the boolean type columns

    Args:
        num_cols (num_cols): this is the number of columns
        num_rows (num_rows): this is the number of rows
    """

    return pd.DataFrame(np.random.randint(2,size=(num_rows,num_cols)),dtype=bool)


df=generate_boolean_values(1000,20)
#export into csv
df.to_csv('./fake_data.csv')