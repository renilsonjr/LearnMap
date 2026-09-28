# 2. Create `steps = [4200, 8100, 6500]`, change the second element to `9000`, 
# append `7300`, then print the list and how many items it holds using `len()`.

steps = [4200, 8100, 6500]
steps[1] = 9000
steps.append(7300)

print(steps)
print(len(steps))