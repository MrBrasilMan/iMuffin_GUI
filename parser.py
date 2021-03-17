def rm_p(toparse):
  #Turn into list
  list_parse = list(toparse)
  #We want to add all text not in <>
  #Style and script info will still show, but that is a problem for another time
  add_to_string = True
  #The string to return
  toreturn = ""
  #For all chars in html body
  for letter in list_parse:
    #If within <> then ingnore
    if letter == ">":
      add_to_string = True
    elif letter == "<":
      add_to_string = False
    #Add chars if add to string is true (will ingore > because exception)
    elif add_to_string == True and letter != ">":
      toreturn = toreturn + letter
  return toreturn.replace("\n", "\t")
def link_list(possiblelinkbody):
  #This was a very complex function to write, and even I do not fully understand how it works. But it does (somewhat) and I am here to document it.
  #First, get a list of functions
  allchar = list(possiblelinkbody)
  #Create a list to add all text to.
  text_list = []
  #PPossible href is True when < appears, possibly conveying that <> contains a link
  possible_href = False
  #Where it is followed by an a, which leads it to assume it to be a link. It could not be, but 9/10 times, this will display a link.
  is_href = False
  #For all charecters in the body
  for char in allchar:
    #If the letter is a(processes before removing possible href)
    if char.lower() == "a" and possible_href == True:
      is_href = True
    #Only scans one line looking for a, shuts down if it is not on the second one.
    if possible_href == True:
      possible_href = False
    #If the charecter is equal to <, then flag it as a possible url.
    if char == "<":
      possible_href = True
    #If the line ends, stop.
    if char == ">" and is_href == True:
      is_href = False
      text_list.append("\n")
    #Otherwise display the link for the person.
    if is_href == True:
      text_list.append(char)
  str1 = ""
  return str1.join(text_list)


########################
###### FIND SCRIPT #####
########################


def is_script(forg_body):
  body = list (forg_body)
  blength = len(body)
  counter = -1
  ammount_found = 0
  #Has to be minus 1 to account for number lag
  while blength-1 != counter:
    counter += 1
    if body[counter] == "<":
      if body[counter + 1] != "/":
        if body[counter + 1] == "s":
          if body[counter + 2] == "c":
            ammount_found += 1
  return ammount_found

def remove_script(forg_body):
  #This function finially works after about a day. I will try to document this as best as I can
  #Turning into a list
  body = list (forg_body)
  #Must be offset because I screwed up a little somewhere.
  counter = -1
  #Getting the length
  blength = len(body)
  #Text to return in a list
  new_text = []
  #If the text is determined not to be any text
  if is_script(forg_body) != 0:
    #If the list is not over
    while blength-1 != counter:
      #Increase the counter
      counter += 1
      just_finished_sa = False
      #If this starting line is False
      if body[counter] == "<":
        if body[counter + 1] != "/":
          if body[counter + 1] == "s":
            if body[counter + 2] == "c":
              #Stop adding
              stop_adding = True
              while stop_adding:
                #Pass through them unless it's the end />, and then skip by eight to remove </script>
                counter += 1
                if body[counter] == "<":
                  if body[counter + 1] == "/":
                    stop_adding = False
                    counter = counter + 8
                    just_finished_sa = True
      #If this is not a recent removal of js
      if just_finished_sa != True:
        #Just add the charecter to a list
        new_text.append(body[counter])
    #Return it to a string
    str1 = ""
    return str1.join(new_text)
  #Otherwise, return the body of the console
  else:
    return forg_body
########################
#### FIND STYLE ########
########################
def is_style(forg_body):
  body = list (forg_body)
  blength = len(body)
  counter = -1
  ammount_found = 0
  #Has to be minus 1 to account for number lag
  while blength-1 != counter:
    counter += 1
    if body[counter] == "<":
      if body[counter + 1] != "/":
        if body[counter + 1] == "s":
          if body[counter + 2] == "t":
            ammount_found += 1
  return ammount_found
def remove_style(forg_body):
  #This function finially works after about a day. I will try to document this as best as I can
  #Turning into a list
  body = list (forg_body)
  #Must be offset because I screwed up a little somewhere.
  counter = -1
  #Getting the length
  blength = len(body)
  #Text to return in a list
  new_text = []
  #If the text is determined not to be any text
  #If the list is not over
  while blength-1 != counter:
      #Increase the counter
      counter += 1
      just_finished_sa = False
      #If this starting line is False
      if body[counter] == "<":
        if body[counter + 1] != "/":
          if body[counter + 1] == "s":
            if body[counter + 2] == "t":
              #Stop adding
              stop_adding = True
              while stop_adding:
                #Pass through them unless it's the end />, and then skip by eight to remove </script>
                counter += 1
                if body[counter] == "<":
                  if body[counter + 1] == "/":
                    stop_adding = False
                    counter = counter + 7
                    just_finished_sa = True
      #If this is not a recent removal of js
      if just_finished_sa != True:
        #Just add the charecter to a list
        new_text.append(body[counter])
    #Return it to a string
  str1 = ""
  return str1.join(new_text)
####################
### PARSING TEXT ###
####################

def the_parse(forg_body):
    parsed_of_js = remove_script(forg_body)
    #Do all tag related items last, rm_p removes tags but not text
    parsed_of_css = remove_style(parsed_of_js)
    parsed_of_htm = rm_p(parsed_of_css)
    final = parsed_of_htm
    return final
###############################
######## GET TITLE ############
###############################
def get_title(thebody):
  body = list(thebody)
  lbody = len(body)
  counter = -1
  while counter-1 != lbody:
    counter = counter + 1
    if body[coutner] == "<":
      if body[counter + 1] == "t":
        if body[counter + 2] == "i":
          if body[counter + 3] == "t":
            if body[counter + 4] == "l":
              counter = counter + 7
              title_not_collected = True
              while title_not_collected:
                counter = counter + 1
                if body[counter] == "/":
                  if body[counter -1] == "<":
                    title_not_collected = False
                    pass