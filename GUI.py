import tkinter as tk
import select_pdf
import select_csv

def run_gui():
    root = tk.Tk()

    root.geometry("300x200")
    root.title("slect files")

    # first button to select pdf file
    PDF_button = tk.Button(root,
                       text="Select PDF",
                       command=select_pdf.select_pdf
                       )
    PDF_button.pack(padx=20, pady=20, side=tk.TOP)

    # button2 to select csv file
    CSV_button = tk.Button(root,
                       text="Select CSV",
                       command=select_csv.select_csv
                       )
    CSV_button.pack(padx=20, pady=20, side=tk.TOP)

    # exit button
    cancel = tk.Button(root,
                       text="Exit",
                       command=exit
                       )
    cancel.pack(padx=20, pady=20, side=tk.BOTTOM)

    root.mainloop()