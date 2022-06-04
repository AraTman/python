import numpy as np
from PIL import Image, ImageDraw, ImageFont  # Import PIL functions

# Open the input image as numpy array, convert to RGB
img = Image.open("images/images1.jpeg").convert("RGB")
npImage = np.array(img)
h, w = img.size

# Create same size alpha layer with circle
alpha = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0, 0, h, w], 0, 360, fill=255)

# Convert alpha Image to numpy array
npAlpha = np.array(alpha)

# Add alpha layer to RGB
npImage = np.dstack((npImage, npAlpha))
Image.fromarray(npImage).save('convert/result.png')


class myTemplate():  # Your template
    def __init__(self, name, description, image):
        self.name = name  # Saves Name input as a self object
        self.description = description  # Saves Description input as a self object
        self.image = image  # Saves Image input as a self object

    def draw(self):
        """
        Draw Function
        ------------------ 
        Draws the template
        """
        img = Image.open(r'template/template1.png',
                         'r').convert('RGBA')  # Opens Template Image
        if self.image != '':
            pasted = Image.open(self.image).convert(
                "RGBA")  # Opens Selected Image
            # Resize image to width fit black area's width
            pasted = pasted.resize(
                (700, int(pasted.size[1]*(700/pasted.size[0]))))
           # pasted=pasted.crop([0,0,350,350]) #Crop height
            img.paste(pasted, (170, 170),pasted)  # Pastes image into template
            imgdraw = ImageDraw.Draw(img)  # Create a canvas
          
        font = ImageFont.truetype("calibril.ttf", 68)  # Loads font
        imgdraw.text((238, 947), self.name, (255,105,0), font=font)  # Draws name
      #  imgdraw.text((654,231), self.description, (0,0,0), font=font) #Draws description

        img.save(r'download/tests.png')  # Saves output


amaztemp = myTemplate('Gaziantep Baklava Günleri', '', r'convert/result.png')
amaztemp.draw()
print('Images created to successfully')
