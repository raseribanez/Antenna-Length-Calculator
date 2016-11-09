# Ben Woodfield
# Calculate vertical wavelength's across the popular size ratios (use for Radio frequencies)

#!/usr/bin/env/python

import Tkinter as tk
from Tkinter import * 

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        cvt_from = StringVar()
        cvt_to = StringVar()

        # Functions to handle the seperate calculations
        def calculate_full_feet():
            freq_val = float(cvt_from.get())
            qtr_wav = 1005/freq_val  # Full wave loop feet calculation
            cvt_to.set('%s Feet' % qtr_wav)

        def calculate_full_meter():
            freq_val2 = int(cvt_from.get())
            qtr_wave = 306.342/freq_val2  # Full wave loop meters calculation
            cvt_to.set('%s Meters' % qtr_wave)

        def calculate_qtr_feet():
            freq_val = float(cvt_from.get())
            qtr_wav = 234/freq_val  # 1/4 wave feet calculation
            cvt_to.set('%s Feet' % qtr_wav)

        def calculate_qtr_meter():
            freq_val2 = float(cvt_from.get())
            qtr_wave = 71.3232/freq_val2  # 1/4 wave meters calculation
            cvt_to.set('%s Meters' % qtr_wave)

        def calculate_half_feet():
            freq_val = float(cvt_from.get())
            qtr_wav = 468/freq_val  # 1/2 wave feet calculation
            cvt_to.set('%s Feet' % qtr_wav)

        def calculate_half_meter():
            freq_val2 = float(cvt_from.get())
            qtr_wave = 142.6464/freq_val2  # 1/2 wave meters calculation
            cvt_to.set('%s Meters' % qtr_wave)

        def calculate_five8_feet():
            freq_val = float(cvt_from.get())
            qtr_wav = 585/freq_val  # 5/8 wave feet calculation
            cvt_to.set('%s Feet' % qtr_wav)

        def calculate_five8_meter():
            freq_val2 = float(cvt_from.get())
            qtr_wave = 178.3080/freq_val2  # 5/8 wave meters calculation
            cvt_to.set('%s Meters' % qtr_wave)

        # Label to display instructions
        lbl_one = Label(self, text='Enter your Frequency \n in MHz', font='freesansbold')
        lbl_one.pack(fill=X)

        # Take the frequency from the user
        freq_input = Entry(self, textvariable=cvt_from, relief='sunken', justify='center', width=30, font=14)
        freq_input.pack()

        # Label to display instructions
        lbl_two = Label(self, text='Click the Wavelength Size \nyou want to calculate', font='freesansbold')
        lbl_two.pack(fill=X)

        # The Calculate Buttons          
        btn_one = Button(self, bg='DarkGrey', text='Full Wave Length', font='freesansbold', fg='Blue', command=calculate_full_meter)
        btn_one.pack(fill=X)
        btn_two = Button(self, bg='DarkGrey',text='Quater Wave Length', font='freesansbold', fg='Blue', command=calculate_qtr_meter)
        btn_two.pack(fill=X)
        btn_three = Button(self, bg='DarkGrey',text='Half Wave Length', font='freesansbold', fg='Blue', command=calculate_half_meter)
        btn_three.pack(fill=X)
        btn_four = Button(self, bg='DarkGrey',text='Five Eight Wave Length', font='freesansbold', fg='Blue', command=calculate_five8_meter)
        btn_four.pack(fill=X)
        
        lbl_result = Label(self, textvariable=cvt_to, relief='flat', bg='Grey', font='freesansbold', fg='Blue')
        lbl_result.pack(fill=BOTH, expand=1)

        lbl_three = Label(self, text='Results in Meters',  relief='flat', bg='Grey', font='freesansbold', fg='Blue')
        lbl_three.pack

        # The exit Button
        btn_exit = Button(self, text='Exit')
        btn_exit.pack(side=BOTTOM, fill=X)
                
   
# Configure the main window's settings
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Antenna Wavelength Calculator')
    root.minsize(350,400)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()
