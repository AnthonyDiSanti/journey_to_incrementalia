import sys
import numpy as np

# Constants
S = 6
CB = 0.63
GB = 0.26
FM = 0.75

# Check if the total constraint is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py souls")
    sys.exit(1)

try:
    souls = int(sys.argv[1])
except ValueError:
    print("Error: souls parameter must be an integer.")
    sys.exit(1)

# Initialize variables to store the maximum m and corresponding c, g, h
max_m = -np.inf
best_c = None
best_g = None
best_total = None

# Define the ranges for c, g, h
c_range_max = 370
c_range = range(0, c_range_max)
g_range = range(0, int(c_range_max*.8))

# Perform exhaustive search
for c in c_range:
    for g in g_range:
        # Check the constraint
        total = 3 * c + 5 * g + S
        if total <= souls:
            # Compute MC
            CM = CB * (1 + GB * g)
            # Compute m
            m = (1 + CM * c) * (1 + FM)
            # Update maximum m and corresponding variables
            if m > max_m:
                max_m = m
                best_c = c
                best_g = g
                best_total = total

# Print the optimal results
print(f"Optimal m: {max_m}")
print(f"Optimal c: {best_c}, g: {best_g}")
print(f"Constraint value (should be <= {souls}): {best_total}")
