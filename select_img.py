import os
import shutil
import glob
import random

to_be_moved = random.sample(glob.glob("ship_o/*.tif"), 100)

for f in to_be_moved:
    dest = os.path.join("ship_dataset")
    if not os.path.exists(dest):
        os.makedirs(dest)
    shutil.copy(f, dest)