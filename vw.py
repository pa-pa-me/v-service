import facemorpher

imgpaths = facemorpher.list_imgpaths('images')

facemorpher.morpher(imgpaths, plot=True)
