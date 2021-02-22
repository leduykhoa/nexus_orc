
# python orc.py --input=./lipsum.png --output=output.text --verbose

import sys, getopt
import logging
import cv2
import pytesseract

# create and configure main logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create console handler with a higher log level
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
logger.addHandler(handler)

# init __
inputfile = ''
outputfile = ''
verbose = False
# process argument
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:v", ["input=", "output=", "verbose"])
except getopt.GetoptError as err:
    logger.info(str('Error: '))
    logger.info(str(err))
    sys.exit(2)

for o, a in opts:
    if o in ("-i", "--input"):
        inputfile = a
    elif o in ("-o", "--output"):
        outputfile = a
    elif o in ("-v", "--verbose"):
        verbose = True

if verbose == True: 
    logger.info(str(sys.argv))
    logger.info(str('Input file is: '+ inputfile))
    logger.info(str('Output file is: '+ outputfile))

# load image 
img = cv2.imread(inputfile)
# Adding custom options
custom_config = r'--oem 3 --psm 6'
data = pytesseract.image_to_string(img, config=custom_config)
if verbose == True:
    logger.info('\n===============\n' + data + '\n===============\n')
# write data
f = open(outputfile, "a")
f.write(data)
f.close()