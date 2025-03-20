my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"APPEND: {my_list}")
my_list.insert(1,15)
print(f"INSERTION: {my_list}")
my_list.extend([50,60,70])
print(f"EXTENSION: {my_list}")
my_list.remove(my_list[-1])
print(f"REMOVE: {my_list}")
my_list.sort(reverse=False)
print(f"SORTED: {my_list}")

for i,v in enumerate(my_list):
    if v == 30:
        print(F"Index of {v} is: {i}")
    
    
