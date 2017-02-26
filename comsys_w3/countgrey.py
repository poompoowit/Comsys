import sys
import os
import numpy as np
import cv2

def split_into_rgb_channels(image):
    '''Split the target image into its red, green and blue channels.
    image - a numpy array of shape (rows, columns, 3).
    output - three numpy arrays of shape (rows, columns) and dtype same as
    image, containing the corresponding channels. 
    '''
    red = image[:,:,2]
    green = image[:,:,1]
    blue = image[:,:,0]
    return red, green, blue

def count_grey_pixel(red, green, blue):
    grey_pixel = 0
    m = len(red)-1
    for i in range(0, m):
        n = len(red[i])-1
        for j in range(0, n):
            if( green[i][j] > 128 and red[i][j] > 128 and blue[i][j] > 128 ):
                grey_pixel += 1

    return grey_pixel

def main():
    ''' This function searches for a folder images/knowpapa subfolder, and splits
    all images found in that folder into its equivalent rgb channel. 
    It saves each image appending the terms 'red', 'green' and
    'blue' to the orginal filename.
    '''
    imagesdir = os.path.abspath(os.path.join(os.curdir, 'images'))
    print "Searching for images in {} Directory)".format(imagesdir)
    exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg', 
            '.jpe', '.jp2', '.tiff', '.tif', '.png']
    all_grey_pixel = 0
    for dirname, dirnames, filenames in os.walk(imagesdir):
        i = 1
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            img = cv2.imread(os.path.join(dirname, filename))
            red, green, blue = split_into_rgb_channels(img)
            num_grey_pixel = count_grey_pixel(red, green, blue)
            print str(i) + '. ' + 'Filename: ' + filename
            print 'Grey Pixel: ' + str(num_grey_pixel)
            print '================================'
            i += 1
            all_grey_pixel += num_grey_pixel

    print '\nTotal Grey Pixel: ' + str(all_grey_pixel)


if __name__ == "__main__":
    main()


