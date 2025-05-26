import tkinter
from tkinter import filedialog


def select_pdf():
    tkinter.messagebox.showinfo("Select PDF", "Please select a PDF file")
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path