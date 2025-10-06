import tkinter as tk
from tkinter import filedialog

def run_gui():
    root = tk.Tk()
    root.geometry("300x200")
    root.title("select files")

    selected_pdf = tk.StringVar()
    selected_csv = tk.StringVar()

    def update_continue_state():
        # Enable continue if both paths are non-empty
        if selected_pdf.get() and selected_csv.get():
            continue_button.config(state=tk.NORMAL)
        else:
            continue_button.config(state=tk.DISABLED)

    def select_pdf():
        path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF files", "*.pdf")]
        )
        if path:
            selected_pdf.set(path)

    def select_csv():
        path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv")]
        )
        if path:
            selected_csv.set(path)

    PDF_button = tk.Button(root, text="Select PDF", command=select_pdf)
    PDF_button.pack(padx=20, pady=10, side=tk.TOP)

    CSV_button = tk.Button(root, text="Select CSV", command=select_csv)
    CSV_button.pack(padx=20, pady=10, side=tk.TOP)

    continue_button = tk.Button(root, text="Continue", state=tk.DISABLED, command=root.quit)
    continue_button.pack(padx=20, pady=10, side=tk.TOP)

    cancel = tk.Button(root, text="Exit", command=root.quit)
    cancel.pack(padx=20, pady=10, side=tk.BOTTOM)

    # Trace changes to update continue button state
    selected_pdf.trace_add('write', update_continue_state)
    selected_csv.trace_add('write', update_continue_state)

    root.mainloop()
    return selected_pdf.get(), selected_csv.get()