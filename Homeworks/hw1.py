#GLOBALAIHUB HW1
# Tarık AVCI  - tarikaavci@gmail.com

array = []

for i in range(5):
    t = (input("Please enter 5 values: "))
    array.append(t)


for i in range(5):
    print(f'{i+1}. value: {array[i]} ')
    print(f'Type of {i+1}. value : {type(array[i])}')

