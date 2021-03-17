from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
import parser
import requests
#Warning, this is some pretty messy code right now
#Preset webtext to the home page
webtext = "Welcome to iMuffin Visual Alpha!\nVersion 0.5\nNews\niMuffin Terminal will be discontinued and this edition will become the new edition. The terminal edition will be left in 0.4.1, and may recieve further updates. This edition will be kept because of it in general being more accessable and easier to use\n\nSorry for any inconvience this causes."
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
window.resizable(False, False)
window.title("iMuffin")
window.geometry('700x400')

#Submit Button
button = Button(window,
	text = "Let's Go!",
	command = get_website,
  width = 6,
  height = 1,
)  
#Search Button
search = tk.Text(window, 
                   height = 1, 
                   width = 50) 

#Website Text and Scrollbar setup
scroll_bar = tk.Scrollbar(window)
website_body_text = tk.Text(window, height=20, width=70)
#Pack all parts of the application
button.grid(column=0, row=0)  
search.grid(column=1, row=0)
website_body_text.grid(column=1, row=5)
website_body_text.insert(tk.END, webtext)
window.mainloop()
