# src/solver.py
import time
import numpy as np
from src.heuristic import apply_2opt

def solve_cvrp(dist_matrix, num_vehicles, vehicle_capacity, depot_idx, demands, use_2opt=True):
    """
    Core solver CVRP dengan opsi optimasi Metaheuristik 2-Opt.
    """
    start_time = time.time()
    unvisited = set(range(1, len(demands)))
    routes = {i: [depot_idx] for i in range(num_vehicles)}
    current_loads = {i: 0 for i in range(num_vehicles)}
    
    # Tahap 1: Greedy Construction
    for vehicle_id in range(num_vehicles):
        curr_node = depot_idx
        while unvisited:
            nodes_list = list(unvisited)
            distances = [dist_matrix[curr_node][node] for node in nodes_list]
            nearest_indices = np.argsort(distances)
            
            allocated = False
            for idx in nearest_indices:
                candidate = nodes_list[idx]
                if current_loads[vehicle_id] + demands[candidate] <= vehicle_capacity:
                    routes[vehicle_id].append(candidate)
                    current_loads[vehicle_id] += demands[candidate]
                    unvisited.remove(candidate)
                    curr_node = candidate
                    allocated = True
                    break
            if not allocated: break
        routes[vehicle_id].append(depot_idx)

    # Tahap 2: Metaheuristic Optimization via 2-Opt
    if use_2opt:
        for vehicle_id in range(num_vehicles):
            if len(routes[vehicle_id]) > 4:
                routes[vehicle_id] = apply_2opt(routes[vehicle_id], dist_matrix)

    # Hitung total metrik jarak
    total_dist_meter = 0
    for r in routes.values():
        for i in range(len(r) - 1):
            total_dist_meter += dist_matrix[r[i]][r[i+1]]
            
    runtime = time.time() - start_time
    return {
        "routes": routes,
        "total_distance_km": total_dist_meter / 1000,
        "runtime_seconds": runtime,
        "loads": current_loads
    }