max_number = int(input("Enter the value, \n"))
number1 = 3
number2 = 5
result = 0
index = 1
while index < max_number:
    is_divisible = (index%number1 == 0 or index%number2 == 0)
    if is_divisible:
        result = result + index
    index += 1
print(result)
