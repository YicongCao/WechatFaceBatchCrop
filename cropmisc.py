from PIL import Image
import os
import glob
import croputils


def cropone(filepath, newsize, format):
    folder, fullname = os.path.split(filepath)
    filename, extension = os.path.splitext(fullname)
    img = Image.open(filepath)
    img = croputils.cropfit(img, newsize)
    if str(format) == "JPG":
        format_re = "JPEG"
    else:
        format_re = str(format)
    img.save("./misc_cropped/" + filename + "_cropped." +
             str(format).lower(), format_re)


if __name__ == "__main__":
    cropone("./misc/banner.jpg", (750, 400), "JPG")
    cropone("./misc/payguide.jpg", (750, 560), "PNG")
    cropone("./misc/thanks.jpg", (750, 750), "PNG")
    cropone("./misc/cover.png", (240, 240), "PNG")
    cropone("./misc/chatpanel.png", (50, 50), "PNG")
