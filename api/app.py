# api/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.solver import solve_cvrp

app = FastAPI(title="INaAI 2026 Logistics Optimization API", version="1.0")

class VRPRequest(BaseModel):
    distance_matrix: List[List[int]]
    demands: List[int]
    num_vehicles: int
    vehicle_capacity: int
    depot_index: int = 0

@app.get("/")
def home():
    return {"status": "running", "competition": "INaAI 2026", "track": "AI Engineer"}

@app.post("/api/v1/optimize")
def optimize_routing(payload: VRPRequest):
    result = solve_cvrp(
        dist_matrix=payload.distance_matrix,
        num_vehicles=payload.num_vehicles,
        vehicle_capacity=payload.vehicle_capacity,
        depot_idx=payload.depot_index,
        demands=payload.demands,
        use_2opt=True
    )
    return {
        "status": "success",
        "total_distance_km": round(result["total_distance_km"], 2),
        "computation_time_s": round(result["runtime_seconds"], 4),
        "optimized_routes": result["routes"],
        "vehicle_loads": result["loads"]
    }