from PIL import Image, ImageSequence
import sys
import os
import shutil

fname_in  = sys.argv[1]
fname_out = "baizheshichen!.gif"

path="./images/"
img = Image.open(sys.argv[1])
iter = ImageSequence.Iterator(img)
i = 1

if not os.path.exists(path):
    os.makedirs(path)   
for frame in iter:
    print("image %d: mode %s, size %s" % (i, frame.mode, frame.size))
    frame.save("./images/img%d.png" % i)
    i += 1

imgs = [frame.copy() for frame in ImageSequence.Iterator(img)]
imgs.reverse()
imgs[0].save(fname_out, save_all=True, append_images=imgs[1:])
shutil.rmtree(path)