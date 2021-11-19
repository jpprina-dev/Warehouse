import enum
import matplotlib.pyplot as plt
import cv2


class ImgFormat(enum.Enum):
    GRAY = 0
    RGB = 1
    BGR = 2
    HSL = 3
    HSV = 4
    LAB = 5
    

def Display(image,
            figsize=None,
            image_format = ImgFormat.BGR
            ):
    plt.figure(figsize=figsize)
    if image_format == ImgFormat.GRAY:
        plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    elif image_format == ImgFormat.RGB:
        plt.imshow(image)
    elif image_format == ImgFormat.BGR:
        plt.imshow(image[..., ::-1])
    else:
        plt.imshow(image)

    plt.show()