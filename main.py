import tkinter as tk
import tkinter.filedialog as fd
import testFiltersHP as hp
import pygame as pg
import IPython.display as ipd
import testFiltersLP as lp


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
        if(filter.get()==0):
            lp.plot_lpfilter_response(cutoff_frequency_lp, filePath)
            
        elif(filter.get()==1):
            hp.plot_hpfilter_response(cutoff_frequency_hp, filePath)
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
windowFour.geometry("700x500")
windowFour.title("HP/LP switchable")

label1 = tk.Label(windowFour, text="High pass and Low pass switchable filter", font=('Arial 20 underline'))
label1.pack(pady=20)

label2 = tk.Label(windowFour, text="Select a wav file to filter", font=('Arial 14'))
label2.pack()


btnFrame = tk.Frame()
btnFrame.pack()
selectBtn = tk.Button(btnFrame, text="Open File", command=openFile, padx=15 , pady=15)
playBtn = tk.Button(btnFrame, text="Play File", command=playFile, padx=15 , pady=15)
stopBtn = tk.Button(btnFrame, text="Stop Playback", command=stopFile, padx=15 , pady=15)


playBtn.grid(row=0, column=0, padx=5)
selectBtn.grid(row=0, column=1, padx=5)
stopBtn.grid(row=0, column=2, padx=5)

label3 = tk.Label(windowFour, text="Selected file: ", font=("Arial 14"))
label3.pack()

pathVar = tk.StringVar()
label4 = tk.Label(windowFour,textvariable= pathVar, font=('Arial 11'))
label4.pack()

label5 = tk.Label(windowFour, text="Choose Filter", font=('Arial 14'))
label5.pack()

filter = tk.IntVar()

radioFrame = tk.LabelFrame(windowFour, text="FILTERS", padx=20, pady=20)
radioFrame.pack()

radBtnLp = tk.Radiobutton(radioFrame, text="Low pass Filter",value=0 , variable=filter,
                          command=selectFilter, 
                          font=('Arial 11'))
radBtnHp = tk.Radiobutton(radioFrame, text="High pass Filter",value=1 , variable=filter,
                          command=selectFilter, 
                          font=('Arial 11'))

radBtnHp.grid(column=0, row=1)
radBtnLp.grid(column=0, row=2)


applyBtn = tk.Button(text="Apply Filter", command=applyFilter, padx=20 , pady=20)
applyBtn.pack(pady=20)



windowFour.mainloop()