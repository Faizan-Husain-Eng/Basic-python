def fractional_knapsack(weights, profits, capacity):
    n = len(weights)

    # Step 1: Create list of items (weight, profit, ratio)
    items = []
    for i in range(n):
        items.append([weights[i], profits[i], profits[i] / weights[i]])

    # Step 2: Sort items by ratio (descending)
    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0

    # Step 3: Apply greedy selection
    for i in range(n):
        weight = items[i][0]
        profit = items[i][1]
        ratio = items[i][2]

        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += ratio * capacity
            break

    return total_profit


# Example
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, profits, capacity))