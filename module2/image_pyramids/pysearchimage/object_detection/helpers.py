import imutils

def pyramid(image, scale, minsize=(30, 30)):
    #yield the original image
    yield image

    #keep looping over the original pyramid
    while True:
        w = int(image.shape[1]/scale)
        image = imutils.resize(image, width=w)

        if image.shape[0] < minsize[1] or image.shape[1] < minsize[0]:
            break

        yield image