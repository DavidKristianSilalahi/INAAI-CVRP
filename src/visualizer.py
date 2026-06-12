# src/visualizer.py
import folium

def generate_folium_map(df_stores, routes):
    """
    Membangun peta interaktif sebaran armada logistik Kota Medan.
    """
    mean_lat = df_stores['latitude'].mean()
    mean_lon = df_stores['longitude'].mean()
    m = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)
    
    # Plot Depot Utama
    folium.Marker(
        location=[df_stores.loc[0, 'latitude'], df_stores.loc[0, 'longitude']],
        popup="GUDANG PUSAT LOGISTIK",
        icon=folium.Icon(color='red', icon='cloud')
    ).add_to(m)
    
    return m