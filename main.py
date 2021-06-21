from bs4 import BeautifulSoup
import requests
import re
from tkinter import *
from tkinter import font

url = "https://opensea.io/collection/thewickedcraniums"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
details = soup.find_all('h3', class_='Blockreact__Block-sc-18q9hu0-0')
details = [str(i) for i in details]
data = []
for i in details:
    data.append(i[84:-5])

def quitwin(event):
    global root
    root.destroy()
    quit()
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,borderwidth=5)
        self.other1 = Label(self, background="white",font=('Avenir', 25, 'bold'), text=data[0])
        self.other2 = Label(self, background="white",font=('Avenir', 25, 'bold'), text=data[1])
        self.other3 = Label(self, background="white",font=('Avenir', 14), fg='#8a939b', text='items')
        self.other4 = Label(self, background="white",font=('Avenir', 14), fg='#8a939b', text='owners')
        self.other5 = Label(self, background="white",font=('Avenir', 25, 'bold'), text=data[2])
        self.other6 = Label(self, background="white",font=('Avenir', 25, 'bold'), text=data[3])
        self.other7 = Label(self, background="white",font=('Avenir', 14), fg='#8a939b', text='average price')
        self.other8 = Label(self, background="white",font=('Avenir', 14), fg='#8a939b', text='volume traded')
        self.other1.grid(row=0, column=0, sticky="nsew")
        self.other2.grid(row=0, column=1, sticky="nsew")
        self.other3.grid(row=1, column=0, sticky="nsew")
        self.other4.grid(row=1, column=1, sticky="nsew")
        self.other5.grid(row=0, column=2, sticky="nsew")
        self.other6.grid(row=0, column=3, sticky="nsew")
        self.other7.grid(row=1, column=2, sticky="nsew")
        self.other8.grid(row=1, column=3, sticky="nsew")

        for row in range(2):
            self.grid_rowconfigure(row, weight=1)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)


root = Tk()
root.bind('<F12>', quitwin)
Example(root).pack(fill="both", expand=True)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("650x150+{}+{}".format(positionRight, positionDown))
root.config(bg="white")
root.overrideredirect(True)

root.mainloop()
