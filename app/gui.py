import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from .ocr import OCR

class AppGUI:
    def __init__(self):
        # create the main window
        self.root = tk.Tk()
        self.root.title("Kintamani OCR Scraping")

        # create the menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # create the canvas for displaying the image
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack(side=tk.LEFT)

        # create the text widget for displaying the OCR result
        self.text_widget = tk.Text(self.root, width=100, height=50)
        self.text_widget.pack(side=tk.RIGHT, padx=10, pady=10)

        # create the OCR object
        self.ocr = OCR()

        # set the initial image
        self.image = None
        self.photo = None

    def run(self):
        self.root.mainloop()

    def open_file(self):
        # open the file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # open the image file and display it on the canvas
            self.image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            # perform OCR on the image and display the result in the text widget
            ocr_result = self.ocr.process_image(file_path)
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, ocr_result)
