from collections import deque
calculations = deque()

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")

    # add item to start of 'list'
    calculations.appendleft(get_item)

# Show that everything made it to the list...
print()
print("*** The Entire Deque ***")
print(calculations)

print()

print("*** Most Recent 3 ****")
for item in range(0,3):
    print(calculations[item])

