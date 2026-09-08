# TODO 1: Create view_history().
def view_history():
    # TODO 2: Try to open transactions.txt in read mode.
    try:
 
    # TODO 3: Read all lines from the file.
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
 
    # TODO 4: Return the lines to the caller.
        return lines
 
    # TODO 5: Handle FileNotFoundError. If the file does not exist, return an empty list.
    except FileNotFoundError:
        return []

""" 
######### Learning Signature ######### 
Programmed by: Chanelle Go
Date Submitted: September 2, 2026
 
Program Description: 
This program takes the transactions.txt file and reads it. If the file can not be found, it will return empty.
Reflection:
I learned to handle errors within handling text files.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""   
 
