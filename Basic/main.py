################## Variable Disclaration #####################
name ='Rana '
address ='Dhaka'
age = 43

#print(name,address)
print('My name is: ' + name + "And Address is:" + address + ' Age:' + str(age))
# print('My name is: ' + name + "\n" + "And Address is: " + address + " " + ' \n' + 'Age:' + str(age))

################## Condition ###################

number = 85
#if number >= 50:
if number >= 90:
    print("Pass")
else:
    print("Fail")

        # #Python Has 3 Logical Operator
        # #and
        # #or
        # #not
############# To Check multiple Condition #################

# Condition1: Purchase more than 1000 Tk
# Condition2: Customer age less than 50 years
# Condition3: Client must be mail
# Condition4: payment cash
# Condition5: payment on cash will get 10% Disscount, Card will get 20% DIsscount
# Condition5: Gender male Free Pen & female Choklate
# COndition6: After Discount you have to pay amount

purchase = 1000
age = 20
gender = "male"
# Data Input nia Out Put
purchase = int(input("Purchase: "))
age = int(input("Age: "))
gender = input("Gender: ")
payment = input("Payment: ")
#if purchase > 1000 and age < 50:
#if purchase > 1000 and age < 50 and gender =="male" and payment == "cash":
#if purchase > 1000 and age < 50 and gender == "male":
if purchase > 1000 and age < 50:
    print("You are eligible for Discount")
    if gender == "male":
        print("You Got a Pen")
    elif gender == "female":
        print("you got a choklate")
    if payment == "cash":
        print("After Discount 10% you have to pay: ")
        print(purchase - purchase*10/100)
    elif payment == "card":
        print("After Discount 20% you have to pay: ")
        print(purchase - purchase * 20 / 100)
else:
    print("You are Not Eligible for Discount")


############# Import Time & Calender #################
#### Getting formatted time ####
import time;
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
###### Getting formatted calender ####
import calendar
# #here we can fine any month or year of the calender
cal = calendar.month(2023, 6)
print ("Here is the calendar:")
print (cal)