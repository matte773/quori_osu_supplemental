import random

# Generate numbers for both ranges (excluding 1 and 11)
first_half = list(range(2, 11))  # 2-10
second_half = list(range(12, 21))  # 12-20

# Shuffle both halves
random.shuffle(first_half)
random.shuffle(second_half)

# Start the sequence with 1 and 11
alternating_order = [1, 11]

# Add the shuffled numbers in alternating order
for i in range(9):
    alternating_order.append(first_half[i])
    alternating_order.append(second_half[i])

print(alternating_order)
