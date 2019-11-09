import tkinter
from tkinter import filedialog

from key_gen import generate_keys, encrypt, decrypt


class View():
  children = []

  def clear(self):
    for child in self.children:
      child.destroy()


class Signup(View):
  def check_password(self):
    pass

  def __init__(self, master, go_success, go_login):
    super().__init__()
    self.go_success = go_success
    self.firstName = tkinter.Entry(master)
    self.lastName = tkinter.Entry(master)
    self.dob = tkinter.Entry(master)
    self.phoneNumber = tkinter.Entry(master)
    self.address = tkinter.Entry(master)
    self.password1 = tkinter.Entry(master)
    self.password2 = tkinter.Entry(master)

    self.children = [
      tkinter.Label(master, text="first name"),
      self.firstName,
      tkinter.Label(master, text="last name"),
      self.lastName,
      tkinter.Label(master, text="date of birth ('mm/dd/yyyy')"),
      self.dob,
      tkinter.Label(master, text="phone number ('xxx-xxx-xxxx')"),
      self.phoneNumber,
      tkinter.Label(master, text="address"),
      self.address,
      tkinter.Label(master, text="password"),
      self.password1,
      tkinter.Label(master, text="password, again"),
      self.password2,
      tkinter.Button(master, text="Next", command=self.check_password),
      tkinter.Button(master, text="Already have an account", command=go_login),
    ]
    for child in self.children:
      child.pack()


class Success(View):
  def __init__(self, master, go_l):
    super().__init__()
    self.children = [
      tkinter.Button(master, text="good job. start over.", command=go_l),
    ]
    for child in self.children:
      child.pack()


class Login(View):
  def encryptButton(self):
    self.m = self.entry.get()
    cipher = encrypt(self.m, self.n, self.e)
    self.resultText.insert(0, cipher)
    self.resultText.config(state='readonly')

  def readKey(self, rawstringpublic):
    self.n, self.e = rawstringpublic.split('$')
    self.n = int(self.n)
    self.e = int(self.e)

  def retrieve(self):
    filedirpub = filedialog.askopenfilename(title="Find Public Key File...")
    contentspub = ''
    with open('{}'.format(filedirpub), 'r') as f:
      contentspub = f.read()

    self.readKey(contentspub)

  def check_password(self):
    pass

  def __init__(self, master, go_signup, go_success):
    super().__init__()
    self.m = ''
    self.n = ''
    self.e = ''
    self.go_success = go_success

    self.username = tkinter.Entry(master)
    self.password = tkinter.Entry(master)
    self.children = [
      tkinter.Label(master, text="Username"),
      self.username,
      tkinter.Label(master, text="Password"),
      self.password,
      tkinter.Button(master, text="Next", command=self.check_password),
      tkinter.Button(master, text="Signup", command=go_signup),
    ]
    for child in self.children:
      child.pack()

