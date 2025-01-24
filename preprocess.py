import cv2


def preprocess(img):

    # Convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur image
    img = cv2.GaussianBlur(img, (9, 9), 0)

    # Threshold image
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Invert image
    img = cv2.bitwise_not(img)

    # Get a rectangle kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # Morph image to remove noise
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # Dilate image to increase border size
    img = cv2.dilate(img, kernel, iterations=1)

    return img






