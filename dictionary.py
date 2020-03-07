fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
    print(name + ' loves a number')


fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

name = input("What's your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
age = int(age)
print("my age is, " + str(age))

pi = input("What's the value of pi? ")
pi = float(pi)
print("my pi is, " + str(pi))

