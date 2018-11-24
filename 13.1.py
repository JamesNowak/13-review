import tkinter

# TODO 13.2 Using the tkinter Module

# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        tkinter.mainloop()


my_gui = MyGUI()


# create the class MyGUI2
class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
# TODO 13.3 Adding a label widget+
# add a label that prints your first and last name
        self.label = tkinter.Label(self.main_window,
                                   text='James Nowak')
# pack the label
        self.label.pack()
# enter the main loop
        tkinter.mainloop()


# create an instance of MyGUI2
my_gui2 = MyGUI2()
# TODO 13.4 Organizing Widgets with Frames
# Create a window in the MyGUI3 class that has two frames
# In the top Frame add a labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame,
                                    text='James Nowak')
        self.label2 = tkinter.Label(self.top_frame,
                                    text='Computer Science')
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        self.label3 = tkinter.Label(self.bottom_frame,
                                    text='Programming Logic')
        self.label4 = tkinter.Label(self.bottom_frame,
                                    text='College Composition')
        self.label5 = tkinter.Label(self.bottom_frame,
                                    text='College Algebra')
        self.label6 = tkinter.Label(self.bottom_frame,
                                    text='Sociology')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


my_gui3 = MyGUI3()
# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window,
                                        text='What do you call a fish with no eye?',
                                        command=self.activate)
        self.my_button.pack()
        tkinter.mainloop()

    def activate(self):
        tkinter.messagebox.showinfo('Punchline',
                                    'A fsh!')


my_gui4 = MyGUI4()
# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters


class InchConverterGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label = tkinter.Label(self.top_frame,
                                                          text='Enter a distance in inches:')
        self.inch_entry = tkinter.Entry(self.mid_frame,
                                        width=10)
        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to centemeters:')
        self.value = tkinter.StringVar
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)
