import sys
import os
import pandas as pd
import numpy as np

def main():
    # Check number of arguments
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters.")
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2].split(',')
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    # Check if file exists
    if not os.path.exists(input_file):
        print("Error: File not found.")
        sys.exit(1)

    # Read CSV file
    try:
        data = pd.read_csv(input_file)
    except Exception:
        print("Error: Unable to read input file.")
        sys.exit(1)

    # Check minimum 3 columns
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    # Check numeric columns (from 2nd column onwards)
    for col in data.columns[1:]:
        if not pd.api.types.is_numeric_dtype(data[col]):
            print("Error: All columns except first must contain numeric values.")
            sys.exit(1)

    # Check weights & impacts length
    if len(weights) != len(impacts) or len(weights) != (data.shape[1] - 1):
        print("Error: Number of weights, impacts and criteria must be same.")
        sys.exit(1)

    # Check impacts values
    for impact in impacts:
        if impact not in ['+', '-']:
            print("Error: Impacts must be either '+' or '-'.")
            sys.exit(1)

    # Convert weights to float
    try:
        weights = np.array([float(w) for w in weights])
    except:
        print("Error: Weights must be numeric.")
        sys.exit(1)

    # -------- TOPSIS IMPLEMENTATION -------- #

    # Step 1: Normalize matrix
    decision_matrix = data.iloc[:, 1:].values
    norm = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

    # Step 2: Multiply by weights
    weighted_matrix = norm * weights

    # Step 3: Determine ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate distances
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate scores
    scores = distance_worst / (distance_best + distance_worst)

    # Add results
    data['Topsis Score'] = scores
    data['Rank'] = pd.Series(scores).rank(method='max', ascending=False).astype(int)



    # Save output
    data.to_csv(output_file, index=False)

    print("TOPSIS calculation completed successfully.")
    print("Output saved to", output_file)

if __name__ == "__main__":
    main()
