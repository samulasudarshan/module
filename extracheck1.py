extra_checks = True
max_number = int(input("Enter the number, "))
number1 = 3
number2 = 5
result = 0
index = 1
new_list = []
while index < max_number:
    if extra_checks:
        print('checking for index = '+ str(index))
    is_divisible = (index%3 == 0 or index%5 ==0)
    if extra_checks:
        print('is_divisble by 3 or 5 = '+str(is_divisible))
    if is_divisible:
        new_list.append(index)
        result = result + index	
    if extra_checks:
        print('result so far = '+str(result))
    index += 1
print(result)
#print(new_list)