from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
import parser
import requests
#Warning, this is some pretty messy code right now
#Preset webtext to the home page
webtext = "Welcome to iMuffin Visual Alpha! You are running version 0.5.1\nUpcoming Features\n___________________________________________________\nInternet Searching!\nCleaner parsing!\n"
#This is the web library of 0.4.2, a little modified to incorperate some built in functions
def get_website():
  try:
    window.title(search.get(1.0, "end-1c") + " - iMuffin")
    body = requests.get(search.get(1.0, "end-1c"))
    website_text = parser.the_parse(body.text) + "End Page\n__________________________________\nList of links\n__________________________________\n" + parser.link_list(body.text)
    website_body_text.delete('1.0', END)
    webtext = website_text
    website_body_text.insert(tk.END, webtext)
  except:
    window.title("Error - iMuffin")
    try:
      requests.get(search.get(1.0, "end-1c"))
      msgbox.showinfo("Uh Oh....",  "A software error occured.") 
    except:
      msgbox.showinfo("Aw, Snap!",  "Invalid URL. Does this website exist?") 

#Starting out dimension
window = Tk()
window.resizable(False, False)
window.title("Home - iMuffin")
window.geometry('700x450')

#Submit Button
gobutton = Button(window,
	text = "Let's Go!",
	command = get_website,
  width = 6,
  height = 1,
)  
optionbutton = Button(window,
  text = "Options",
  command = get_website,
  width = 6,
  height = 1,
)
#Search Button
search = tk.Text(window, 
                   height = 1, 
                   width = 45) 

#Website Text and Scrollbar setup
scroll_bar = tk.Scrollbar(window)
website_body_text = tk.Text(
  window, 
  height=20, 
  width=70, 
  )
#Pack all parts of the application
gobutton.grid(column=0, row=0)  
search.grid(column=1, row=0)
#optionbutton.grid(column=0,row=12)
website_body_text.grid(column=1, row=5)
website_body_text.insert(tk.END, webtext)
window.mainloop()
