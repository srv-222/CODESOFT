from tkinter import*
import random
import string

root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x400")
root.resizable(FALSE,FALSE)
root.configure(bg="PapayaWhip")

pwdstr=StringVar()
pwdlen=IntVar()

def get_pwd():
    pwd_1=string.ascii_letters + string.digits + string.punctuation
    password=""
    
    for x in range(pwdlen.get()):
        password = password + random.choice(pwd_1)
        pwdstr.set(password)

Label(root, text="Enter length of the Password", font=("Comic Sans MS",12), bg="PapayaWhip").pack(pady=9)
Entry(root, textvariable=pwdlen).pack(pady=2)
Button(root, text="Generate", font=("Comic Sans MS",12), command=get_pwd).pack(pady=15)
Label(root, text="Generated Password is:", font=("Comic Sans MS", 12), bg="PapayaWhip").pack(pady=10)
Label(root, textvariable=pwdstr, font=("Comic Sans MS", 14, 'bold'), fg="blue", bg="PapayaWhip").pack(pady=5)

root.mainloop()