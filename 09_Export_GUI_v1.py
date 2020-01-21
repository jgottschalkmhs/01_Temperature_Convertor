from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        all_calc_list = []

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # History Button (row 1)
        self.history_button = Button(self.converter_frame,
                                     text="Calculation History",
                                     font="Arial 14", padx=10, pady=10,
                                     command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        get_history = History(self)
        

class History:
    def __init__(self, partner):

        background = "#a9ef99"     # Pale green


        # disable help button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.history_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                              partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up Help heading (row 0)
        self.history_heading = Label(self.history_frame, text="Calculation History",
                                     font="arial 19 bold", bg=background)
        self.history_heading.grid(row=0)

        # Instructions (row 1)
        self.history_instructions = Label(self.history_frame,
                                          text="Here are your most recent "
                                               "calculations.  Please use the "
                                               "export button to create a text "
                                               "file of all your calculations for "
                                               "this session", wrap=250,
                                          font="arial 10 italic",
                                          justify=LEFT, bg=background, fg="maroon",
                                          padx=10, pady=10)
        self.history_instructions.grid(row=1)

        self.all_calcs_frame = Frame(self.history_frame)
        self.all_calcs_frame.grid(row=2)

        # Calculations go here...

    def close_history(self, partner):
        # Put help button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
