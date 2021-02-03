#GLOBALAİHUB - PYTHON COURSE
#TARIK AVCI - tarikaavci@gmail.com
#HW-2 DAY-3
#Q1

username = "tarikavci"
password = "123456"

username_1 = input("Please enter username: ")
print("- - - - - - - - - - - - - - - - - - -")
password_1 = input("Please enter password: ")
if (username_1 == username and password_1 == password):
    print("Successfully. Youre in")
elif (username_1 == username and password_1 != password):
    print("wrong password")
elif (username_1 != username and password_1 == password):
    print("wrong username")
else:
    print("Wrong username and password")

#EXTRA -- Q2

dict = {'username' : "tarikavci", 'password' : "123456"}
user_name = dict.get('username')
pass_word = dict.get('password')

username_2 = input("Please enter username: ")
print("- - - - - - - - - - - - - - - - - - -")
password_2 = input("Please enter password: ")
if (username_2 == user_name and password_2 == pass_word):
    print("Successfuly. you are in")
else :
    print("please try agin. Wrong username or passsword.")