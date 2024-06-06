import random
from tkinter import *
import pyperclip
from tkinter import messagebox

#root window
w=Tk()
w.config(bg='black')
w.geometry('560x400+450+200')
w.title('password generator')
w.resizable(height=True,width=False)

#stores integer value entered by user
passlength=IntVar()
passlength.set('')


#to retrieve string
pswrd=StringVar()


#function for password generation
def generate_password():
    characters='abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890!@#$%^&*()~'
    password=''
    if passlength.get()>=6:
        for i in range(passlength.get()):
            password+=random.choice(characters)
        pswrd.set(password)
    else:
        messagebox.showwarning('length too small')


#function for copying to clipboard
def copy():
    random_pswrd = pswrd.get()
    pyperclip.copy(random_pswrd)
    Label(w,text="Copied to Clipboard",bg="red").pack(pady=6)


label=Label(w,text='Enter your the length of password: \n (atleast 6 in length)',width=30,font=('Times New Roman',16),fg='midnight blue')
label.pack(padx=20,pady=20)

#inputs password length from user
Entry(w, textvariable=passlength,font=('Times New Roman',16)).pack(pady=3)

#button to generate the password
generate_but= Button(w,width=30,text='Generate Password',font=('Times New Roman',14),fg='midnight blue',command=generate_password)
generate_but.pack(padx=20,pady=20)

#shows the password generated
Entry(w, textvariable=pswrd,font=('Times New Roman',16)).pack(pady=3)

#button for copying generated password to the4 clipbaord
copy_button=Button(w,width=30,text='Copy to clipboard',font=('Times New Roman',14),fg='midnight blue',command=copy)
copy_button.pack(padx=20,pady=20)


w.mainloop()