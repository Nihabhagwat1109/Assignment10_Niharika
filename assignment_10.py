#Niharika
import tkinter as tkin
import webbrowser as web

root = tkin.Tk()

entry = tkin.Entry(root,font=("Times New Roman",16),width=20)
entry.grid(row=0,column=0)

lab1= tkin.Label(root,font=("Times new Roman",16))
lab1.grid(row=1,column=0)
def display():
    search =entry.get()
    print(search)
    if search:
        lab1.configure(text="navigating to google")
        web.open(f"https://www.google.com/search?q={search}")
    else:
        print("please write something")

def button_click():
    print("Button is clicked!")
search_button = tkin.Button(root, text="Search", font=("Times New Roman", 13),bg="purple", activebackground="white", command=display)
search_button.grid(row=3, column=0)
close_button = tkin.Button(root, text="Close", font=("Times New Roman", 12),bg="purple", activebackground="white", command=root.destroy)
close_button.grid(row=6, column=0)
button = tkin.Button(root, text="Click Me!", command=button_click)
root.mainloop()
#Niharika