#!/usr/bin/env   python3

import numpy as np

from collections import namedtuple


image_width = 25
image_height = 6
image_size = image_width * image_height

PartI = namedtuple('PartI', ('id', 'zeros', 'crc'))


def parse(line):
    return list(map(int, line.strip()))



def createImages(data, num_image, image_height=image_height, image_width=image_width):
    return np.asarray(data, dtype=np.int32).reshape((num_image, image_height, image_width))



def partI_numpy(data, num_image):
    images = createImages(data, num_image)

    layers = []
    for image_id, image in enumerate(images):
        assert image.shape == (image_height, image_width)

        zeros = (image[image == 0]).shape[0]
        assert zeros <= image_size

        ones  = (image[image == 1]).shape[0]
        assert ones <= image_size

        twos  = (image[image == 2]).shape[0]
        assert twos <= image_size

        layers.append(PartI(image_id, zeros, ones * twos))

    layers.sort(key=lambda x: x.zeros)
    #print(*layers, sep='\n')
    return layers[0].crc



def partI(data, num_image):
    layers = []
    for image_id in range(num_image):
        image = data[image_id*image_size : (image_id+1)*image_size]
        assert len(image) <= image_size

        zeros = len(list(filter(lambda x: x==0, image)))
        assert zeros <= image_size

        ones  = len(list(filter(lambda x: x==1, image)))
        assert ones <= image_size

        twos  = len(list(filter(lambda x: x==2, image)))
        assert twos <= image_size

        layers.append(PartI(image_id, zeros, ones * twos))

    layers.sort(key=lambda x: x.zeros)
    #print(*layers, sep='\n')
    return layers[0].crc



def debug(data, num_image):
    images1 = np.asarray(data, dtype=np.int32).reshape((num_image, image_height, image_width))
    images2 = [ data[image_id*image_size : (image_id+1)*image_size] for image_id in range(num_image) ]
    for i1, i2 in zip(images1, images2):
        print(i1)
        print(i1.flatten().tolist())
        print(i2)



def combine(images):
    image = np.ones_like(images[0]) * 2
    for layer in images:
        image[image == 2] = layer[image == 2]
    return image

    images = images.transpose((1,2,0))
    image = []
    for row in images:
        for column in row: 
            pixels = list(filter(lambda p: p!=2, column))
            pixel = 2
            if len(pixels) > 0:
                pixel = pixels[0]
            image.append(pixel)

    return image



def partII(data, num_image):
    images = createImages(data, num_image)

    image = combine(images)
    for line in image:
        for p in line:
            print(' ' if p == 0 else '%', sep='', end='')
        print('')
    print('')







if __name__ == '__main__':
    with open('input', 'r') as f:
        data = parse(f.readlines()[0])
    num_image = int(len(data) / (image_width * image_height))

    #debug(data, num_image)

    answer = partI_numpy(data, num_image)
    #answer = partI(data, num_image)

    # Answer: 2975
    print('Answer PartI:', answer)

    # Answer: EHRUE
    partII(data, num_image)
