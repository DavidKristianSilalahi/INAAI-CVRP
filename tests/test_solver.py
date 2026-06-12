# tests/test_solver.py
import pytest
from src.solver import solve_cvrp

def test_cvrp_solver_basic():
    # Setup matriks jarak dummy sederhana berbentuk segitiga (3 titik)
    dummy_matrix = [
        [0, 1000, 1500],
        [1000, 0, 1200],
        [1500, 1200, 0]
    ]
    dummy_demands = [0, 10, 20]
    
    result = solve_cvrp(
        dist_matrix=dummy_matrix,
        num_vehicles=2,
        vehicle_capacity=30,
        depot_idx=0,
        demands=dummy_demands,
        use_2opt=False
    )
    
    assert "routes" in result
    assert result["total_distance_km"] > 0
    assert result["loads"][0] <= 30