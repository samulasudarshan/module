items = [1,2,4543,0,-1]
items.sort()
minium_number = items[0]
print(f"min of [1,2,4543,0,-1] is {minium_number}")
print(f"min of {items} is {minium_number}")
maxium_number = items[-1]
print(f"min of [1,2,4543,0,-1] is {maxium_number}")
print(f"min of {items} is {minium_number}")

items = [1,2,4543,0,-1]
minium = [0]
maxium = [0]
for number in items:
    while minium < number:
        minium = minium < number
        print('minium')