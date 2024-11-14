import sys
import numpy as np

# Constants
GC = 1
CRB = 85
AB = 12

# Check if the total constraint is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 archdevil.py souls_limit")
    sys.exit(1)

try:
    souls = int(sys.argv[1])
except ValueError:
    print("Error: souls_limit parameter must be an integer.")
    print("")
    print("Usage: python3 archdevil.py souls_limit")
    sys.exit(1)

# Initialize variables to store the maximum m and corresponding c, g, h
best_cr = None
best_a = None
best_total = None

# Perform exhaustive search
for cr in range(GC * 90, souls):
    for a in range((best_a or 0) + 1,
                   min(int((souls - 1 * cr) / (15 + 0.2)),
                       int((cr * CRB) / AB + 1))):
        best_a = a
        best_cr = cr
        best_total = 1 * cr + 15 * a + 0.2 * a

# Print the optimal results
print(f"Optimal cr: {best_cr}, a: {best_a}")
print(f"Souls cost (should be <= {souls}): {best_total}")
