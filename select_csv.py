import tkinter.filedialog   

def select_csv():
    tkinter.messagebox.showinfo("Select CSV", "Please select a CSV file")
    CSV_file_path = tkinter.filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    return CSV_file_path
