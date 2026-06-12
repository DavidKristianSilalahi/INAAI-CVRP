# src/distance.py
import numpy as np

def calculate_distance_matrix(coordinates):
    """
    Menghitung matriks jarak Euclidean (dalam meter) dari koordinat [Lat, Lon].
    Menggunakan rumus konversi derajat ke km (~111.1 km per derajat).
    """
    diff = coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]
    distance_matrix_km = np.sqrt(np.sum(diff ** 2, axis=-1)) * 111.1
    distance_matrix_meter = (distance_matrix_km * 1000).astype(int)
    return distance_matrix_meter.tolist()