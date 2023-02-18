from PIL import Image
import numpy as np
import sys
import getopt

def getPixelMatrix(image: Image):

    data_type = None

    # PNG Images have an alpha channel
    if(image.format == "PNG" ):
        data_type = np.dtype("int, int, int, int")
    else :
        data_type = np.dtype("int, int, int")
    

    # Get the flattened pixel data
    flat_array: list[tuple[int]] = list(image.getdata())
    
    # Reshape into a matrix 
    reshaped_array = np.array(
        flat_array, 
        dtype=data_type
        ).reshape(-1,image.size[0])    
  

    return reshaped_array

def getBrightnessMatrix(matrix):

    brightness_array = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i][j]) >= 4:
                (red, green, blue, alpha) = matrix[i][j]
            else:
                (red, green, blue) = matrix[i][j]
            average = round((red + green + blue) / 3, 2)
            brightness_array.append(average)
    
    reshaped_array = np.array(brightness_array).reshape(-1,len(matrix[0]))

    return reshaped_array            

def getAsciiMatrix(matrix):

    ascii_gradient = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    ascii_gradient_length = len(ascii_gradient)

    ascii_array = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            brightness_percentage = round(matrix[i][j] / 255, 2)
            
            ascii_charecter_index = int(round(ascii_gradient_length * brightness_percentage,0))

            ascii_array.append(ascii_gradient[ascii_charecter_index])

    reshaped_array = np.array(ascii_array).reshape(-1, len(matrix[0]))

    return reshaped_array

def create_output_file(content, filename):

    string = '\n'.join(' '.join(str(cell) for cell in row) for row in content)

    with open(filename, 'w') as file:
        file.write(string)
        file.close()


