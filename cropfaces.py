from PIL import Image
import os
import glob
import croputils
gifsize = (240, 240)
pngsize = (120, 120)
i = 0
for infile in glob.glob("./faces/*.JPG"):
    i += 1
    folder, fullname = os.path.split(infile)
    img = Image.open(infile)
    gif = croputils.cropfit(img, gifsize)
    png = croputils.cropfit(img, pngsize)
    # create thumbnail
    gif.save(folder + "/../faces_cropped/" + str(i) + ".gif", "GIF")
    png.save(folder + "/../faces_cropped/" + str(i) + ".png", "PNG")
    print("cropped count: " + str(i))
