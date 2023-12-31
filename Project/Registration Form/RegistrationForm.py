#pip intall tkinter

from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
	print("Accepted")
#Heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")

gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")

#Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for Storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#Creating Entry Field
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
paymentmoodentry = Entry(root, textvariable = paymentmoodvalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)

#Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymentmoodentry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

#Submit Button
Button(text="submit", command=getvals()).grid(row=7, column=3)
root.mainloop()
