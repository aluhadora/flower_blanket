import cv2
import numpy
import os

# myimg = cv2.imread('images/Admiral.jpg')
# avg_color_per_row = numpy.average(myimg, axis=0)
# avg_color = numpy.average(avg_color_per_row, axis=0)
# print(avg_color)
# print(myimg[30, 34])


for filename in os.listdir('images'):
    myimg = cv2.imread('images/' + filename)
    b, g, r = myimg[30,34]
    # print(f"{filename:<25}: #{r:02x}{g:02x}{b:02}")
    print(f'    "{filename.replace(".jpg", "")}": ("#{r:02x}{g:02x}{b:02x}", 1),')