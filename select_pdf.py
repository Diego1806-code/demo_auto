import tkinter
from tkinter import filedialog


def select_pdf():
    tkinter.messagebox.showinfo("Select PDF", "Please select a PDF file")
    PDF_file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    return PDF_file_path