from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
import parser
import requests
#Preset webtext to the home page
webtext = "Welcome to iMuffin Visual Alpha!"
#This is the web library of 0.4.2, a little modified to incorperate some built in functions
def get_website():
  try:
    body = requests.get(search.get(1.0, "end-1c"))
    website_text = parser.the_parse(body.text) + "\nList\n__________________________________\n" + parser.link_list(body.text)
    website_body_text.delete('1.0', END)
    webtext = website_text
    website_body_text.insert(tk.END, webtext)
  except:
    msgbox.showinfo("Uh Oh....",  "An error occured while trying to get the website.") 


#Starting out dimension
window = Tk()
window.title("iMuffin")
window.geometry('350x200')

#Submit Button
button = Button(window,
	text = 'Go',
	command = get_website,
  width = 2,
  height = 1,
)  
#Search Button
search = tk.Text(window, 
                   height = 1, 
                   width = 40) 

#Website Text and Scrollbar setup
scroll_bar = tk.Scrollbar(window)
website_body_text = tk.Text(window, height=10, width=100)
#Pack all parts of the application
button.pack()  
search.pack()
website_body_text.pack(side = tk.LEFT)
website_body_text.insert(tk.END, webtext)
window.mainloop()
