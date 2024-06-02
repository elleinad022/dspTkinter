import tkinter as tk
import tkinter.filedialog as fd

windowFour = tk.Tk()
windowFour.geometry("800x500")
windowFour.title("HP/LP switchable")

label1 = tk.Label(windowFour, text="High pass and Low pass switchable filter", font=('Arial 20 underline'))
label1.pack(pady=20)

label2 = tk.Label(windowFour, text="Select a wav file to filter : ", font=('Arial 14'))
label2.pack()



windowFour.mainloop()