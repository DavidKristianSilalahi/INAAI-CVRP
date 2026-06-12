# src/heuristic.py

def apply_2opt(route, dist_matrix):
    """
    Mengoptimalkan rute tunggal dengan memotong jalur bersilang (Local Search).
    """
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for j in range(i + 1, len(best_route) - 1):
                if j - i == 1: continue
                
                old_dist = dist_matrix[best_route[i-1]][best_route[i]] + dist_matrix[best_route[j]][best_route[j+1]]
                new_dist = dist_matrix[best_route[i-1]][best_route[j]] + dist_matrix[best_route[i]][best_route[j+1]]
                
                if new_dist < old_dist:
                    best_route[i:j+1] = reversed(best_route[i:j+1])
                    improved = True
    return best_route