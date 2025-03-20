data = input('Enter comma sepparated operands and operator Format->(12,2,+): ')
arr_data = data.split(",")

result = 0
if arr_data[2] == '+':
    result = int(arr_data[0])+int(arr_data[1])
elif arr_data[2] == '-':
    result = int(arr_data[0])-int(arr_data[1])
elif arr_data[2] == '*':
    result = int(arr_data[0])*int(arr_data[1])
elif arr_data[2] == '/':
    result = int(arr_data[0])/int(arr_data[1])
else:
    print('Invalid input format, input should be e.g,(2,5,+)')

print()
print("******* RESULT *********")
print(f"{arr_data[0]} {arr_data[2]} {arr_data[1]} = {result}")
print("************************")