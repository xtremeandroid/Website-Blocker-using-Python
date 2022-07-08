from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk. Tkinter is not the only GuiProgramming toolkit for Python. It is however the most commonly used one.

# ttk module provides access to the Tk themed widget set, introduced in Tk 8.5. If Python has not been compiled against Tk 8.5, this module can still be accessed if Tile has been installed.

hostsFile_path = r"C:\Windows\System32\drivers\etc\hosts"
localhost = "127.0.0.1"

# Host File is used To map a domain, add a line based on the examples in the HOSTS file.

# Start with the target IP address, then a space, then the domain name. If you want to block a website, redirect it to 127.0.0.1.

# Defining functions using def keyword

def Response():
    result = myText.get()
    displayText.configure(state='normal')
    displayText.insert(END, result + ",")
    displayText.configure(state='disabled')
    User_Input.delete(0,END)
    

def getSiteFromTextAndBlock():
    global sites
    sites = [x.strip() for x in displayText.get("1.0",END).split(',')] 
    try:        
        with open(hostsFile_path,"r+") as file:
                content = file.read()
                for site in sites:
                    if site in content:
                        pass
                    else:
                        file.write( "\n" + localhost + " " + site)
                mb.showinfo(title="info",message = "Blocking Successful")
    except:
        mb.showinfo(title="Exception",message ="Error (Error : Please Run as Adminstrator or ReRun)  ")
        
def unblockAll():
    with open(hostsFile_path,"r+") as file:
            contents = file.readlines()
            file.seek(0)
            for content in contents:
                if not any(website in content for website in sites):
                    file.write(content)
            file.truncate()
            displayText.configure(state='normal')
            displayText.delete('1.0', END)
            displayText.configure(state='disabled')
            mb.showinfo(title="unblock websites", message="Unblocked")

window = Tk()
window.title("Website Blocker using Python")
window.geometry("400x500")
# window.configure(bg='grey')
window['background']='grey'



myText = StringVar()
window.resizable(False, False)

User_Input = Entry(window, textvariable=myText, width=50, bg="white")
User_Input.place(x=40, y=370)
addButton = Button(window, text="ADD TO LIST", command=Response, bg="grey", height=2, width=10).place(x =250, y=420)
blockButton = Button(window, text="BLOCK SITE", command=getSiteFromTextAndBlock, bg="grey", height=2, width=10, ).place(x =150, y=420)
unblockButton = Button(window, text="UNBLOCK SITE", command=unblockAll, bg="grey", height=2, width=10).place(x =50, y=420)
displayText = Text(window, height=20, width=40, bg="grey")
displayText.pack()
displayText.configure(state='disabled')

window.mainloop()
