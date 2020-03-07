# assign number1 and number2
number1 = 1
number2 = 2
print(number1)
print(number2)
result = 0
sum = 2
while result < 100:  
    result = number1 + number2 
	if result < 100: 
	print(result) 
		if result%2 == 0:
		    sum += result
	else:
		break
	number1 = number2 
	number2 = result  
print('sum of even valued terms below 100 is {}'.format(sum))
