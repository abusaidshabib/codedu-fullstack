value = str(input("Enter a binary number:" ))
array = list(value)
print(array)

sum = 0
for index, value in enumerate(reversed(array)):
    print(value , index, 2)
    sum += int(value) * pow(2,int(index))

print(sum)