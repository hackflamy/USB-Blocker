from tkinter import *

root = Tk()
text = ""

def OnButtonEvent(pas, ap, ro):
    if pas.get() == "none":
        ro.destroy()
        ap.destroy()

def showScreen(i):
    root.wm_overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(background='black')
    root.focus_set()
    root.bind("<Button-1>", lambda evt, j=i: showWidget(j))
    l = Label(root, text='Ask For Assistance', font=("'Malgun Gothic Semilight'", 75), bg='black', fg='white')
    l.pack(expand=True)

def showWidget(i):
    if i == 0:
        app = Tk()
        app.title("Password")
        lEnterPass = Label(app, text="Enter Password")
        lEnterPass.grid(sticky=E)
        passWidget = Entry(app, textvariable=text, show="\u2022")
        passWidget.grid(row=0, column=1, sticky=W)
        submitPass = Button(app, text="OK", command=(lambda e=passWidget, a=app, r=root: OnButtonEvent(e, a, r)))
        submitPass.grid(row=1, sticky=N+S+E+W)
        app.mainloop()
        i += 1
    else :
        app.focus_set()

if __name__ == '__main__':
    showWidget()

