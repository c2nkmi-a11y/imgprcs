import PIL.Image as Image

class ImageDisplay:
    def __init__(self, image_path):
        self.image_path = image_path    

    def display_image(self):
        image = Image.open(self.image_path)
        image.show()
        
    def display_image(image_path):
        image = Image.open(image_path)
        image.show()
    
if __name__ == "__main__":
    image_display = ImageDisplay('input_image.jpg')
    image_display.display_image()
