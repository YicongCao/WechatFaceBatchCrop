from PIL import Image


def cropfit(img, newsize):
    curwidth, curheight = img.size
    curratio = curwidth / curheight
    tarratio = newsize[0] / newsize[1]
    # do crop
    if tarratio > curratio:
        tempsize = (curwidth, curwidth / tarratio)
        zeropoint = (0, (curheight - curwidth / tarratio) / 2)
    else:
        tempsize = (curheight * tarratio, curheight)
        zeropoint = ((curwidth - curheight * tarratio)/2, 0)
    tempimg = img.crop((
        zeropoint[0], zeropoint[1],
        zeropoint[0] + tempsize[0],
        zeropoint[1] + tempsize[1]))
    # do zoom
    finalimg = tempimg.resize(newsize, Image.ANTIALIAS)
    return finalimg
