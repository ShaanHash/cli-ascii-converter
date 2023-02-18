import sys
import getopt
from PIL import Image
from ImageProcessor import getAsciiMatrix, getBrightnessMatrix, getPixelMatrix, create_output_file

arg_input = ""
arg_output = "output.txt"
arg_resize = ""
arg_help = "-i --input <file path to image>\n-rw --resize-width <new image width to resize to>\n-o --output <output file name>"


def getOpts(argv):

    global arg_input
    global arg_output
    global arg_resize
    global arg_help
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:rw:o:", ["help", "input=", 
        "resize-width=", "output="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-rw", "--resize-width"):
            arg_resize = int(arg)
        elif opt in ("-o", "--output"):
            arg_output = arg

if __name__ == "__main__":

    getOpts(sys.argv)

    if arg_input == "":
        print("Please define an input file")
        sys.exit(1)

    example_image = Image.open(arg_input)

    if arg_resize != "":
        example_image.thumbnail((arg_resize,arg_resize))
    
    dimensions = example_image.size

    pixel_matrix = getPixelMatrix(example_image)

    brightness_matrix = getBrightnessMatrix(pixel_matrix)

    ascii_matrix = getAsciiMatrix(brightness_matrix)

    create_output_file(ascii_matrix, arg_output)

    example_image.close()