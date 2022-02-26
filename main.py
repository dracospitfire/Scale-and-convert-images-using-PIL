#!/usr/bin/env python3

import os
from PIL import Image

for image in os.listdir("images"):
    if image.endswith('p'):
        i = Image.open(os.path.join('images', image))
        file, ext = os.path.splitext(image)
        i = i.convert("RGB")
        i = i.resize((128, 128))
        i = i.rotate(270)                                # degrees counter-clockwise
        i.save('new_images/{}.jpg'.format(file))
