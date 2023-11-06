#照片去背
from rembg import remove
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
from  matplotlib import pyplot as plt

input_path = 'IMG_4358.JPG'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
# plt.imshow(output)

img = cv2.imread('output.png')
cv2_imshow(img)
