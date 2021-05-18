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
def sliding_window(image, stepSize, windowSize):
    #slide a window accross the image
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield(x, y, image[y:y + windowSize[1], x:x + windowSize[0]])