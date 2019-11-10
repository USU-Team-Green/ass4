import tkinter
from views import Signup, Login, Success

class MainLoopClass():
    top = tkinter.Tk()

    def __init__(self):
        self.top.geometry("800x480")
        self.go_signup()
        self.top.mainloop()

    def clear(self):
        if hasattr(self,'children'):
            self.children.clear()

    def go_signup(self):
        self.clear()
        self.children = Signup(self.top, self.go_success, self.go_login)

    def go_login(self):
        self.clear()
        self.children = Login(self.top, self.go_signup, self.go_success)

    def go_success(self):
        self.clear()
        self.children = Success(self.top, self.go_login)

if __name__ == '__main__':
    main = MainLoopClass()
