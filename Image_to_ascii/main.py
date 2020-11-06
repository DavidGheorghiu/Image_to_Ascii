from PIL import Image
import math

def convertImageToAscii(image):
    rgb_values = image.convert('RGB')

    # get the images width and height and scale it down 10 times and make it divisible by 10
    ascii_width = image.size[0] - image.size[0]%10
    ascii_height = image.size[1] - image.size[1]%10

    grayscale_cluster_values = ''
    
    for pixel_height in range(0, ascii_height, 10):
        grayscale_cluster_values += ' \n '
        for pixel_width in range(0, ascii_width, 10):
            current_cluster_value = 0
            for cluster in range(pixel_width, pixel_width+10):
                red, green, blue = rgb_values.getpixel((cluster, pixel_height))
                current_cluster_value += red + green + blue
            average_current_cluster_value = math.floor((current_cluster_value/3)/10)
            grayscale_cluster_values += assignAsciiCharacter(average_current_cluster_value) + ' '
    return grayscale_cluster_values

def assignAsciiCharacter(grayscale_value):
    ascii_characters = [' ', '.', '*', '!', '/', 'X', '%', 'B', '$', '#']
    index = round(grayscale_value/25.5) - 1
    return ascii_characters[index]

# open the image and store the image in a variable
image = Image.open('kanye.png')

# write ascii image to text file
file = open('ascii.txt', 'w')
grayscale = convertImageToAscii(image)
file.write(grayscale)
print(grayscale)
