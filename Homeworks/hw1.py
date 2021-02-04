#GLOBALAIHUB PYTHON COURSE HW1 DAY-2
#TARIK AVCI tarikaavci@gmail.com
#Q1
print("Answer 1")
list1 = [1,2,3,4,5,6,7,8,9,10]
print("our list is ",list1)

list_first = list1[0:5]
list_second = list1[5:10]
list_second.extend(list_first)
print("after swap our list",list_second)

print("--------------------------------------------")


#Q2
print("Answer 2")
n = int(input("Enter single digit integer: "))
print(f'Even numbers are to {n}')
for i in range(n+1):
    if(i%2==0):
        print(i)
