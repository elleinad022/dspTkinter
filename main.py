import tkinter as tk
import tkinter.filedialog as fd
import testFiltersHP as hp
import pygame as pg
import IPython.display as ipd
#import testFiltersLP as lp


def openFile():
    global filePath
    filePath = fd.askopenfilename(title="OPEN A WAV FILE. OKAY?", filetypes=(("Audio wav files", "*.wav"),))
    print(filePath)
    return filePath

def playFile():
    pg.mixer.init()
    pg.mixer.music.load(filePath)
    pg.mixer.music.play(loops=0)

def stopFile():
    pg.mixer.music.stop()

def applySelectedFilter(loadedFile):
    hp.apply_hp_filter(loadedFile)
    

windowFour = tk.Tk()
windowFour.resizable(0,0)
windowFour.geometry("700x350")
windowFour.title("HP/LP switchable")

label1 = tk.Label(windowFour, text="High pass and Low pass switchable filter", font=('Arial 20 underline'))
label1.pack(pady=20)

label2 = tk.Label(windowFour, text="Select a wav file to filter : ", font=('Arial 14'))
label2.pack()


btnFrame = tk.Frame()
btnFrame.pack()
selectBtn = tk.Button(btnFrame, text="Open File", command=openFile, padx=15 , pady=15)
playBtn = tk.Button(btnFrame, text="Play File", command=playFile, padx=15 , pady=15)
stopBtn = tk.Button(btnFrame, text="Stop Playback", command=stopFile, padx=15 , pady=15)


playBtn.grid(row=0, column=0, padx=5)
selectBtn.grid(row=0, column=1, padx=5)
stopBtn.grid(row=0, column=2, padx=5)


applyBtn = tk.Button(text="Apply Filter", command=applySelectedFilter, padx=20 , pady=20)
applyBtn.pack(pady=20)



windowFour.mainloop()