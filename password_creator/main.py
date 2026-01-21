import random
from tkinter import messagebox
from tkinter import *
from venv import create


# Letters A to Z
letters = [
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

# Numbers 0 to 9
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]

# Special symbols
special_symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','|',';',
    ':',"'",'"',',','.','<','>','?','/','`','~'
]

window = Tk()
window.minsize(width=500,height=300)
window.title("PASSWORD GENERATOR :")


Label(window,text="Enter how many numbers: ").grid(row=0, column=1)
Label(window,text="Enter how many char you want: ").grid(row=1,column=1)
Label(window,text="Enter how many special symbol: ").grid(row=2,column=1)
Label(window,text="Password: ").grid(row=3,column=1)


num = Entry(window)
char = Entry(window)
alpha = Entry(window)
password = Entry(window)


num.grid(row=0,column=2)
char.grid(row=1,column=2)
alpha.grid(row=2,column=2)
password.grid(row=3,column=2)

def on_click():

    password.delete(0, 'end')

    pass_list = []

    n = int(num.get())     # how many numbers
    c = int(char.get())   # how many letters
    s = int(alpha.get())   # how many symbols

    # Add numbers
    for _ in range(n):
        pass_list.append(random.choice(numbers))

    # Add letters
    for _ in range(c):
        pass_list.append(random.choice(letters))

    # Add special symbols
    for _ in range(s):
        pass_list.append(random.choice(special_symbols))

    # Shuffle password
    random.shuffle(pass_list)

    # Convert list to string
    passw = ''.join(pass_list)


    if len(pass_list)<8 or len(pass_list)>11:
        messagebox.showinfo("Warning", "Password at least 8 character OR you enter more than 11 char for Password")
    else:

        password.insert(0, passw)



def user_defined_pass():

    password.delete(0, 'end')


    n = num.get()  # how many numbers
    c =  char.get()  # how many letters
    s =  alpha.get()
    all_ = n+c+s

    password.insert(0,all_)


if Button(command=on_click):

    ran_button = Button(text="Random password ",command=on_click)
    ran_button.grid(row=5,column=2)

if Button(command=user_defined_pass):

    #messagebox.showinfo("Warning", "Enter password what you want")
    user_button = Button(text="own password ", command=user_defined_pass)
    user_button.grid(row=4, column=2)






window.mainloop()




