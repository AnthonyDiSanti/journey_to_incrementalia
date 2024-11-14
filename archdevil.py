import sys
import numpy as np

# Constants
CRB = 85
AB = 12

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
best_cr = None
best_a = None
best_total = None

# Perform exhaustive search
for cr in range(0, souls):
    for a in range(0, souls):
        # Check the constraint
        total = 1 * cr + 15 * a + 0.2 * a
        if total <= souls and a > (best_a or 0) and (a - 1) * AB <= cr * CRB:
            best_cr = cr
            best_a = a
            best_total = total

# Print the optimal results
print(f"Optimal cr: {best_cr}, a: {best_a}")
print(f"Constraint value (should be <= {souls}): {best_total}")
