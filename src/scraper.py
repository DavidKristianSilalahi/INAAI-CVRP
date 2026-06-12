# src/scraper.py
import pandas as pd
import numpy as np

def generate_medan_retail_data(seed=42):
    """
    Simulasi fungsi scraper tangguh untuk mengambil data minimarket di Kota Medan.
    Mengembalikan DataFrame dengan koordinat dan nama toko.
    """
    np.random.seed(seed)
    lat_center, lon_center = 3.5952, 98.6722
    
    retail_names = (
        [f"Alfamart Jamin Ginting {i}" for i in range(1, 25)] +
        [f"Indomaret Dr. Mansyur {i}" for i in range(1, 25)] +
        [f"Alfamidi Krakatau {i}" for i in range(1, 25)]
    )
    retail_names = retail_names[:72]
    
    latitudes = np.random.uniform(lat_center - 0.04, lat_center + 0.04, 72)
    longitudes = np.random.uniform(lon_center - 0.04, lon_center + 0.04, 72)
    
    df = pd.DataFrame({
        'name': retail_names,
        'latitude': latitudes,
        'longitude': longitudes
    })
    
    # Set Gudang Pusat di indeks 0
    df.loc[0, 'name'] = "CENTRAL LOGISTICS DEPOT (GUDANG PUSAT)"
    return df