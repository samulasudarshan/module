old_list = [3, 6, 9]
new_list = []
for item in old_list:
    new_list.append(item**2)
#print(new_list)
print(f"{old_list} {new_list}")
print('{} {}'.format(new_list, old_list))
print("%s %s", (old_list, new_list))
