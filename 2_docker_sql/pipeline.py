import sys
import pandas as pd

print(sys.argv)

# Ensure a command-line argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide a day argument.")
    sys.exit(1)

day = sys.argv[1]

# Some fancy stuff with pandas
print(f'job finished successfully for day = {day}')