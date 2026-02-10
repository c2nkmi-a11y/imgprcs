import tkinter as tk
from tkinter import filedialog
from app import ImageProcessor

class ImageProcessorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Processor")

        self.label = tk.Label(master, text="Select an image to process:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            processor = ImageProcessor(file_path)
            processor.save_processed_image('processed_image.png')
            tk.messagebox.showinfo("Success", "Image processed and saved as 'processed_image.png'.")
        else:
            tk.messagebox.showwarning("No Selection", "No image selected.")
            
if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageProcessorGUI(root)
    root.mainloop()