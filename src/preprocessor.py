# src/preprocessor.py
import pandas as pd
import numpy as np

def preprocess_demands(df_stores, seed=42):
    """
    Menambahkan demand stokastik untuk tiap minimarket sesuai spesifikasi proyek.
    """
    np.random.seed(seed)
    df = df_stores.copy()
    df['demand'] = np.random.randint(2, 8, size=len(df))
    df.loc[0, 'demand'] = 0  # Depot utama tidak memiliki demand pengantaran
    return df