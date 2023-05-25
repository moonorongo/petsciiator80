from PIL import Image

import utils
import sys
import chargen

charRom = chargen.get_charrom()

# en este punto, el archivo tiene tener aplicado un filtro threshold
# y resizeado a 640 x 400
input_file = sys.argv[1]
output_file = sys.argv[2]

print(sys.argv)

im = Image.open(input_file)
outf = open(output_file, "wb")

for row in range(25):
    for col in range(80):
        (left, upper, right, lower) = (col * 8, row * 8 + row, col * 8 + 8, row * 8 + 8 + row)
        
        cropped_image = im.crop((left, upper, right, lower))
        currentCharBytes = utils.get_character_bytes(cropped_image)
        
        outf.write(utils.findBestMatch(currentCharBytes, charRom).to_bytes())
  
outf.close()
