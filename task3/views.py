import tkinter
import time

from hashPass import store_password, check_password


class View():
  children = []

  def clear(self):
    for child in self.children:
      child.destroy()


class Signup(View):
  def verify_password(self):
    self.errorText.set('')
    username = self.username.get()
    firstName = self.firstName.get()
    lastName = self.lastName.get()
    dob = self.dob.get()
    phoneNumber = self.phoneNumber.get()
    address = self.address.get()
    password1 = self.password1.get()
    password2 = self.password2.get()

    # passwords don't match error
    if password1 != password2:
      self.errorText.set('passwords do not match')
      return

    # empty field error
    if password1 == '' or username == '' or firstName == '' or lastName == '' or dob == '' or phoneNumber == '' or address == '':
      self.errorText.set('please fill out all areas')
      return

    # insecure password
    if phoneNumber.strip() in password1 or phoneNumber in password1:
      self.errorText.set('your password is not secure because your phone number is in it.')
      return

    if firstName.strip() in password1 or firstName in password1:
      self.errorText.set('your password is not secure because your first name is in it.')
      return

    if lastName.strip() in password1 or lastName in password1:
      self.errorText.set('your password is not secure because your last name is in it.')
      return

    if dob.strip() in password1 or dob in password1:
      self.errorText.set('your password is not secure because your first name is in it.')
      return

    if address.strip() in password1 or address in password1:
      self.errorText.set('your password is not secure because your first name is in it.')
      return

    if username.strip() in password1 or username in password1:
      self.errorText.set('your password is not secure because your first name is in it.')
      return

    # check if password is in either password list.
    with open('enhanchedPasswordList.txt') as f:
      wordList = f.readlines()
      for word in wordList:
        if word.strip('\n') == password1:
          self.errorText.set('your password is not secure because you are using a common password.')
          return

    with open('originalPasswordList.txt') as f:
      wordList = f.readlines()
      for word in wordList:
        if word.strip('\n') == password1:
          self.errorText.set('your password is not secure because you are using a common password.')
          return

    store_password(username, password1)
    self.go_success()

  def __init__(self, master, go_success, go_login):
    super().__init__()
    self.go_success = go_success
    self.username = tkinter.Entry(master)
    self.firstName = tkinter.Entry(master)
    self.lastName = tkinter.Entry(master)
    self.dob = tkinter.Entry(master)
    self.phoneNumber = tkinter.Entry(master)
    self.address = tkinter.Entry(master)
    self.password1 = tkinter.Entry(master)
    self.password2 = tkinter.Entry(master)
    self.errorText = tkinter.StringVar(master)
    self.errors = tkinter.Label(master, textvariable=self.errorText)

    self.children = [
      tkinter.Label(master, text="username"),
      self.username,
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
      tkinter.Button(master, text="Next", command=self.verify_password),
      tkinter.Button(master, text="Already have an account", command=go_login),
      self.errors
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

  def verify_password(self):
    password = self.password.get()
    username = self.username.get()
    if check_password(username, password):
      self.totalAttempts = 0
      self.recentAttempts = 0
      self.go_success()
    else:
      self.recentAttempts += 1
      self.totalAttempts += 1
      if self.recentAttempts == 3:
        time.sleep(60 * 2**(self.totalAttempts//3))
        self.recentAttempts = 0


  def __init__(self, master, go_signup, go_success):
    super().__init__()
    self.recentAttempts = 0
    self.totalAttempts = 0
    self.go_success = go_success

    self.username = tkinter.Entry(master)
    self.password = tkinter.Entry(master)
    self.children = [
      tkinter.Label(master, text="Username"),
      self.username,
      tkinter.Label(master, text="Password"),
      self.password,
      tkinter.Button(master, text="Next", command=self.verify_password),
      tkinter.Button(master, text="Signup", command=go_signup),
    ]
    for child in self.children:
      child.pack()

