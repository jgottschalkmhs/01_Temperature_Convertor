from collections import deque
calculations = deque()

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    calculations.appendleft(get_item)

for item in calculations:
    print(item)
