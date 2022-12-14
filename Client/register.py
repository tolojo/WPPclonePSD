from tkinter import *
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def register(uname, passwd):
    print(uname)
    response = requests.get(url="http://192.168.1.75:3000/retrieveServerPK")

    with open('server_public_key.pem', 'wb') as f:
        f.write(response.content)
    f = open('server_public_key.pem', "r")
    while f.read() == "":
        f = open('server_public_key.pem', "r")

    with open("server_public_key.pem", 'rb') as p:
        publicKey = serialization.load_pem_public_key(
            p.read()
        )

    passwd = publicKey.encrypt(passwd.encode(), padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    passwd = passwd.decode('latin1')

    user_dict = {
        'uname': uname,
        'passwd': passwd
    }
    return user_dict

def close(tkWindow):
    tkWindow.destroy()


def regInt():
    # window
    tkWindow = Toplevel()
    tkWindow.geometry('400x150')
    tkWindow.title('Register')
    # uname label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    uname = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=uname).grid(row=0, column=1)
    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1, columnspan=2)
    # login button
    loginButton = Button(tkWindow, text="Register", command=(lambda: requests.post(url="http://127.0.0.1:3000/registerUser",
                                                                            json=register(uname.get(),
                                                                                          password.get())))).grid(
    row=4, column=0)

    tkWindow.mainloop()
