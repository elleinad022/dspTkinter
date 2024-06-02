import tkinter as tk
import tkinter.filedialog as fd

def openFile():
    filePath=fd.askopenfilename(title="OPEN A WAV FILE. OKAY?", filetypes=(("Audio wav files","*.wav"), ))
    print(filePath)

windowFour = tk.Tk()
windowFour.resizable(0,0)
windowFour.geometry("700x350")
windowFour.title("HP/LP switchable")

label1 = tk.Label(windowFour, text="High pass and Low pass switchable filter", font=('Arial 20 underline'))
label1.pack(pady=20)

label2 = tk.Label(windowFour, text="Select a wav file to filter : ", font=('Arial 14'))
label2.pack()

selectBtn = tk.Button(text="Open File", command=openFile, padx=30 , pady=30)
selectBtn.pack(pady=20)



windowFour.mainloop()