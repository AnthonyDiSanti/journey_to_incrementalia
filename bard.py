import sys
import numpy as np

# Constants
S = 6
BB = 0.072
JB = 0.03
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
best_b = None
best_j = None
best_total = None

# Define the ranges for c, g, h
b_range = range(0, souls)
j_range = range(0, souls) #int(b_range_max*.8))

# Perform exhaustive search
for b in b_range:
    for j in j_range:
        # Check the constraint
        total = 3 * b + 1 * j + S
        if total <= souls:
            # Compute MC
            BM = BB + JB * (j - 1) - 0.01 * (b - 1)
            # Compute m
            m = (1 + BM * b) * (1 + FM)
            # Update maximum m and corresponding variables
            if m > max_m:
                max_m = m
                best_b = b
                best_j = j
                best_total = total

# Print the optimal results
print(f"Optimal m: {max_m}")
print(f"Optimal b: {best_b}, j: {best_j}")
print(f"Constraint value (should be <= {souls}): {best_total}")
