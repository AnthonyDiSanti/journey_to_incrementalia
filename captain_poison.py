import numpy as np

# Constants
CB = 0.45
GB = 0.23
HB = 0.7
PM = 4.64

# Initialize variables to store the maximum m and corresponding c, g, h
max_m = -np.inf
best_c = None
best_g = None
best_h = None

# Define the ranges for c, g, h
c_range_max = 370
c_range = range(0, c_range_max)
g_range = range(0, int(c_range_max*.8))
h_range = range(0, 222)    # h from 100 to 221

# Perform exhaustive search
for c in c_range:
    for g in g_range:
        for h in h_range:
            # Check the constraint
            total = 3 * c + 5 * g + 5 * h
            if total <= 1109:
                # Compute MC
                MC = CB * (1 + GB * g)
                # Compute m
                m = (1 + MC * c) * (1 + HB * h + PM)
                # Update maximum m and corresponding variables
                if m > max_m:
                    max_m = m
                    best_c = c
                    best_g = g
                    best_h = h

# Print the optimal results
print(f"Optimal m: {max_m}")
print(f"Optimal c: {best_c}, g: {best_g}, h: {best_h}")
print(f"Constraint value (should be <= 1109): {3 * best_c + 5 * best_g + 5 * best_h}")
