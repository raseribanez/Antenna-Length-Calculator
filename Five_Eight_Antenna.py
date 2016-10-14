# Ben Woodfield
# 5/8 Wave-Length Vertical Antenna Calculator

from Tkinter import *

top = Tk()
top.minsize(450,350)
top.title(' 5/8 Wave Antenna Calculator')
top.configure(bg='DarkGrey')

cvt_from = StringVar()
cvt_to = StringVar()


def calculate_qtr_feet():
    freq_val = float(cvt_from.get())
    qtr_wav = 585/freq_val  # 5/8 wave feet calculation
    cvt_to.set('%s Feet > 5/8 WaveLength' % qtr_wav)
    
def calculate_qtr_meter():
    freq_val2 = float(cvt_from.get())
    qtr_wave = 178.3080/freq_val2  # 1/4 wave meters calculation
    cvt_to.set('%s Meters > 5/8 WaveLength' % qtr_wave)
    
lbl_info = Label(top, text='Enter Frequency in MHz', fg='blue', bg='DarkGrey', font='freesansbold,16') 
lbl_info.pack()

freq_input = Entry(top, font='freesansbold, 14', relief='raised', textvariable=cvt_from)
freq_input.pack()

lbl_2 = Label(top,text='Click "Calculate" to get results', fg='blue', bg='DarkGrey', font='freesansbold,16')
lbl_2.pack()

convert_btn = Button(top, text='Calculate Antenna (Meters)', fg='blue', font='freesansbold, 14', command=calculate_qtr_meter)
convert_btn.pack()

convert_btn = Button(top, text='Calculate Antenna (Feet)', fg='blue', font='freesansbold, 14', command=calculate_qtr_feet)
convert_btn.pack()

lbl_result = Label(top, textvariable=cvt_to, relief='ridge', font='freesansbold, 14', bg='Grey', fg='Blue')
lbl_result.pack(fill=BOTH, expand=1)

q = Button(top, text='Exit', command=quit, bg='DarkGrey', fg='red', font='freesansbold, 14') 
q.pack(side=BOTTOM, fill=X)

top.mainloop()
