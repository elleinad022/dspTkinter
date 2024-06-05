import tkinter as tk
import tkinter.filedialog as fd
import testFiltersHP as hp
import pygame as pg
import IPython.display as ipd
import testFiltersLP as lp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def openFile():
    global filePath
    filePath = fd.askopenfilename(title="OPEN A WAV FILE. OKAY?", filetypes=(("Audio wav files", "*.wav"),))
    pathVar.set(filePath)
    print(filePath)
    return filePath

def playFile():
    try:
        pg.mixer.init()
        pg.mixer.music.load(filePath)
        pg.mixer.music.play(loops=0)

    except:
        tk.messagebox.showinfo("File Error", "No File is selected")
        print("No file was selected")
    

def stopFile():
    try:
        pg.mixer.music.stop()
    except:
        return

cutoff_frequency_lp = 3000 
cutoff_frequency_hp = 1000
    
def selectFilter():
    try:
        for widget in pltCanvas.winfo_children():
            widget.destroy()

        if(filter.get()==0):
            lpFig = lp.plot_lpfilter_response(cutoff_frequency_lp, filePath)
            canvas_agg = FigureCanvasTkAgg(lpFig, master=pltCanvas)
            canvas_agg.draw()
            canvas_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
        elif(filter.get()==1):
            hpFig = hp.plot_hpfilter_response(cutoff_frequency_hp, filePath)
            canvas_agg = FigureCanvasTkAgg(hpFig, master=pltCanvas)
            canvas_agg.draw()
            canvas_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    except:
        return
    

def applyFilter():
    try:
        if(filter.get()==0):
            lp.apply_lp_filter(filePath)
            print("Lowpass selected")
        elif(filter.get()==1):
            hp.apply_hp_filter(filePath)
            print("Highpass selected")
    except:
        tk.messagebox.showinfo("File Error", "Select audio file and filter to apply")
        print("No file was selected")
    
    
    

windowFour = tk.Tk()
windowFour.resizable(0,0)
windowFour.geometry("1000x750")
windowFour.title("HP/LP switchable")
windowFour.configure(background= '#E9DDD7')


label1 = tk.Label(windowFour, text="High pass and Low pass switchable filter", font=('Century Gothic Bold', 15))
label1.configure(background="#090C9B", foreground='white')
label1.pack(pady=15, expand='True', fill="both")

label2 = tk.Label(windowFour, text="Select a wav file to filter", font=('Century Gothic Bold', 15))
label2.configure(background="#E9DDD7")
label2.pack()



btnFrame = tk.Frame()
btnFrame.configure(background='#E9DDD7')
btnFrame.pack()
selectBtn = tk.Button(btnFrame, text="Open File", command=openFile, padx=15 , pady=15)
selectBtn.configure(background='#3066BE')

playBtn = tk.Button(btnFrame, text="Play File", command=playFile, padx=15 , pady=15)
stopBtn = tk.Button(btnFrame, text="Stop Playback", command=stopFile, padx=15 , pady=15)


playBtn.grid(row=0, column=0, padx=5)
selectBtn.grid(row=0, column=1, padx=5)
stopBtn.grid(row=0, column=2, padx=5)

label3 = tk.Label(windowFour, text="Selected file: ", font=('Century Gothic Bold', 15))
label3.configure(background="#E9DDD7")
label3.pack()

pathVar = tk.StringVar()
label4 = tk.Label(windowFour,textvariable= pathVar, font=('Century Gothic Bold', 15))
label4.configure(background="#E9DDD7")
label4.pack(pady=5)

label5 = tk.Label(windowFour, text="Choose Filter", font=('Century Gothic Bold', 15))
label5.configure(background="#E9DDD7")
label5.pack()

filter = tk.IntVar()

radioFrame = tk.LabelFrame(windowFour, text="FILTERS", padx=20, pady=20)
radioFrame.configure(background='#E9DDD7')
radioFrame.pack()

radBtnLp = tk.Radiobutton(radioFrame, text="Low pass Filter",value=0 , variable=filter,
                          command=selectFilter, 
                          font=('Century Gothic Bold', 15))
radBtnLp.configure(background='#E9DDD7')
radBtnHp = tk.Radiobutton(radioFrame, text="High pass Filter",value=1 , variable=filter,
                          command=selectFilter, 
                          font=('Century Gothic Bold', 15))
radBtnHp.configure(background='#E9DDD7')
pltCanvas = tk.Frame(radioFrame, width=600, height=300)
pltCanvas.grid(column=2, row=1, rowspan=2)
radBtnHp.grid(column=0, row=1)
radBtnLp.grid(column=0, row=2)

footerFrame = tk.Frame()
footerFrame.config(background='#E9DDD7')
footerFrame.pack()

backBtn = tk.Button(footerFrame ,text="Back to Menu", padx=20 , pady=20)
backBtn.configure(background='#B4C5E4')
backBtn.grid(row=0, column=1, pady=20, padx=40, sticky='E')
applyBtn = tk.Button(footerFrame ,text="Apply Filter", command=applyFilter, padx=20 , pady=20)
applyBtn.configure(background='#3066BE')
applyBtn.grid(row=0, column=0, pady=20, padx=40, sticky='W')



windowFour.mainloop()