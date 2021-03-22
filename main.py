from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
import parser
import requests
#Warning, this is some pretty messy code right now
#Preset webtext to the home page
webtext = "Welcome to iMuffin Visual Alpha! You are running version 0.5.6\nNewest Features\n___________________________________________________\nwww.google.com now defaults to https\nAdress bar now larger to show how enter works.\nWebsite text more or less centered with buttons on left side and search bar and website text on right side.\n GUI changes" 
#This is the web library of 0.4.2, somewhat modified.
#This function gets the website and returns it in text
def get_website():
  try:
    #Get the users' query.
    #Automatically https if the user does not specify.
    if "https://" in str(search.get(1.0, "end-1c")):
      #print ("got here")
      body = requests.get(search.get(1.0, "end-1c"))
    if "https://" not in str(search.get(1.0, "end-1c")):
      if "http://" not in str(search.get(1.0, "end-1c")):
       body = requests.get("https://" + search.get(1.0, "end-1c"))      
    #This places the parsed html in the website text, plus an end of page, and list of links belowards.
    window.title(parser.get_title(body) + " - iMuffin")
    website_text = parser.the_parse(body.text) + "End Page\n__________________________________\nList of links\n__________________________________\n" + parser.link_list(body.text)
    #Delete all of the text from the previous website
    website_body_text.delete('1.0', END)
    #This is putting the text in the main textbox to view.
    webtext = website_text
    website_body_text.insert(tk.END, webtext)
  #Error handling
  except:
    window.title("Error - iMuffin")
    #If the url could be found, but an error still occured
    try:
      requests.get(search.get(1.0, "end-1c"))
      msgbox.showerror("Uh Oh",  "A software error occured.") 
    #If the URL is invalid.
    except:
      msgbox.showerror("Snap!",  "Invalid URL. Does this website exist?") 

#Starting out dimension
window = Tk()
window.resizable(False, False)
window.title("Home - iMuffin")
window.geometry('700x400')

#Submit Button
gobutton = Button(window,
	text = "Open URL",
	command = get_website,
  width = 6,
  height = 1,
)  
#Search Button
search = tk.Text(window, 
                   height = 2, 
                   width = 45) 

#Website Text
website_body_text = tk.Text(
  window, 
  height=20, 
  width=70, 
  )
#Pack all parts of the application
gobutton.grid(column=1, row=0)  
search.grid(column=0, row=0)
website_body_text.grid(column=0, row=7)
website_body_text.insert(tk.END, webtext)
window.mainloop()
