import numpy as np
from tabulate import tabulate

def threshold(x):
    # Standard threshold: 1 if x >= 0, else 0.
    # Adjust to 1 if needed for your specific lab logic.
    return 1 if x >= 0 else 0

def main():
    # 1. User Inputs
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print(f"\nEnter the {rows}x{cols} input matrix (row by row, space-separated):")
    X = [np.array(list(map(float, input(f"Row {i+1}: ").split()))) for i in range(rows)]

    print("\nEnter the target outputs (y):")
    y = [float(input(f"Target {i+1}: ")) for i in range(rows)]

    weights = np.array(list(map(float, input("\nEnter initial weights (space-separated): ").split())))
    bias = float(input("Enter initial bias: "))
    lr = float(input("Enter learning rate: "))
    epochs = int(input("Enter maximum epochs: "))

    # 2. Training Loop
    for epoch in range(1, epochs + 1):
        table_data = []
        headers = ["Input (x)", "Target (y)", "Output (o)", "Error", "Weight Diff (w)", "New Weights", "New Bias"]

        # Track if any change occurs in this epoch
        changed_in_epoch = False

        for i in range(rows):
            # Step 1: Calculate Net Input and Output
            net_input = np.dot(X[i], weights) + bias
            output = threshold(net_input)

            # Step 2: Calculate Error
            error = y[i] - output

            # Step 3: Calculate Weight/Bias Difference
            delta_w = lr * error * X[i]
            delta_b = lr * error

            # Check if weights or bias actually changed
            if not np.all(delta_w == 0) or delta_b != 0:
                changed_in_epoch = True

            # Step 4: Update Weights and Bias
            weights = weights + delta_w
            bias = bias + delta_b

            # Step 5: Format for Tabulate
            table_data.append([
                str(X[i].tolist()),
                y[i],
                output,
                error,
                str(delta_w.tolist()),
                str(np.round(weights, 4).tolist()),
                round(bias, 4)
            ])

        print(f"\n--- Epoch {epoch} ---")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

        # TERMINATION LOGIC: If no changes happened across all rows, stop.
        if not changed_in_epoch:
            print(f"\nTermination condition met: No changes in weights or bias during Epoch {epoch}.")
            break
    else:
        print("\nReached maximum epochs without full convergence.")

if __name__ == "__main__":
    main()
