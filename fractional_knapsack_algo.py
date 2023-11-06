def fractional_knapsack(values, weights, capacity):
    n = len(values)
    value_per_weight = [(v / w, v, w) for v, w in zip(values, weights)]
    value_per_weight.sort(reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for vpw, v, w in value_per_weight:
        if remaining_capacity >= w:
            total_value += v
            remaining_capacity -= w
        else:
            total_value += (remaining_capacity / w) * v
            break
    
    return total_value

values = [10, 50, 60, 30]
weights = [2, 5, 10, 5]
capacity = 12

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value:", max_value)