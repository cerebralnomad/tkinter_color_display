#! /usr/bin/env python3.6

import tkinter as tk
from ColorList import color_list

root = tk.Tk()
root.title("Ubuntu Color Display for Tkinter")

frame = tk.Frame(root)
frame.configure(background = 'slate gray')
frame.pack(fill = 'both', expand = True, side = 'top')
'''
These two for loops configure the columns and rows to expand to
fill the space when the window is resized
'''
frame_row = 0
frame_column = 0
for i in range(30):
	frame.columnconfigure(frame_column, weight = 1)
	frame_column += 1
for i in range(19):
	frame.rowconfigure(frame_row, weight = 1)
	frame_row += 1

'''
The code for the tool tip style pop up which will display the
name of the color in each box when the mouse hovers over it
'''

class ToolTip():
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None 

    def show_tip(self, tip_text):
        
        # Display color name in a tooltip window
        
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")  # get size of widget
        x = x = self.widget.winfo_rootx() + 25      # calculate to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 50 # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget) # create new tip window
        tw.wm_overrideredirect(True)             # remove window manager decorations
        tw.wm_geometry("+%d+%d" % (x, y))   # create window size

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
            background="#ffffe0", relief=tk.SOLID, borderwidth=1,
            font=("tahome", "8", "normal"))
        label.configure(foreground = 'black')
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)      # Create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)  # Bind mouse events
    widget.bind('<Leave>', leave)

# End tool tip code block

'''
Create the 558 buttons colored with each color in the list
variable color_list using a for loop
'''

row = 0
column = 0
num = 1

for color in color_list:
	
	button = 'button' + str(num) # the incrementing button variable
	button = tk.Button(frame) # create the button using the incremented name
	button.configure(background = color, activebackground = color)
	button.grid(row = row, column = column, sticky = 'nsew')
	create_ToolTip(button, color)
	num += 1
	if column < 29: # continue on a row until 30 columns are reached
		row = row
		column += 1
	else:    # once 30 columns have displayed add a row and return to column 0
		row += 1
		column = 0

# The exit button located at the bottom of the window

button = tk.Button(frame, text = 'Exit', command = root.destroy,
    background = '#48483E', foreground = '#CFD0C2')
button.grid(row = 20, column = 0, columnspan = 29, pady = (10))

root.mainloop()