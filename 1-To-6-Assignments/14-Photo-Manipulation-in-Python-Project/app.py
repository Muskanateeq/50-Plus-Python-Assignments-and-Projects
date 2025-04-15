from PIL import Image, ImageEnhance
import cv2
import numpy as np

def open_image(image_path):
    """ Opens an image using Pillow """
    img = Image.open(image_path)
    img.show()
    return img

def convert_grayscale(image):
    """ Converts an image to grayscale """
    grayscale_img = image.convert("L")
    grayscale_img.show()
    return grayscale_img

def blur_image(image_path, intensity=5):
    """ Applies a blur effect to an image using OpenCV """
    img = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(img, (intensity, intensity), 0)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate_image(image, angle):
    """ Rotates an image by a given angle """
    rotated = image.rotate(angle)
    rotated.show()
    return rotated

def adjust_brightness(image, factor):
    """ Adjusts brightness (1.0 = original, >1.0 = brighter, <1.0 = darker) """
    enhancer = ImageEnhance.Brightness(image)
    brightened = enhancer.enhance(factor)
    brightened.show()
    return brightened

if __name__ == "__main__":
    image_path = "home_page.jpeg" 
    img = open_image(image_path)

    # Apply manipulations
    convert_grayscale(img)
    blur_image(image_path, intensity=15)
    rotate_image(img, 45)
    adjust_brightness(img, 1.5)
