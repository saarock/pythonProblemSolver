import cv2

path = 'F:\Pythonproblemsolver\pythonbeautifulprojects\image.jpg'
image = cv2.imread(path, cv2.IMREAD_UNCHANGED)


if (image is not None):
    new_width = int(image.shape[1] * 50 / 100)
    new_height = int(image.shape[0] * 50 / 100)
    out = cv2.resize(image, (new_width, new_height))
    read = cv2.imwrite('newimage.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('SOmethings wrong')
