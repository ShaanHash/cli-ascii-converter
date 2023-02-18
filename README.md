# cli-ascii-converter
A simple command line tool for converting images to ASCII art

## This Input
![lemur](https://github.com/shaanhash/cli-ascii-converter/blob/main/example.jpg?raw=true)

## Turns into this Output
*slight downscaling

![lemur](https://github.com/shaanhash/cli-ascii-converter/blob/main/output_example.png?raw=true)

### How to Use

```
python img2ascii -input <filepath to image>
```

#### Arguments

- -i, --input : **Mandatory** Filepath of the image to be converted : *--input=./example.jpg*
- -o, --output : **Optional** Filename of the output text file : *--output=output.txt*
- -rw, --resize-width : **Optional** Max width to resize the ascii art to (respects aspect ratio) : *--resize-width=300*
- -h, --help : **Optional** More Information : *--help*
