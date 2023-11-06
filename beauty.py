# 安装OpenCV库
!pip install opencv-python

import cv2
import numpy as np

# 上传你的图像到Colab，或提供图像的URL
# 如果上传图像，你可以使用以下代码读取图像：
# from google.colab import files
# uploaded = files.upload()
# image_path = next(iter(uploaded))
# image = cv2.imread(image_path)

# 如果提供了图像URL，可以使用以下代码读取图像：
# import urllib
# image_url = "YOUR_IMAGE_URL"
# image = cv2.imdecode(np.asarray(bytearray(urllib.request.urlopen(image_url).read()), dtype=np.uint8), -1)

# 或者加载本地图像（上传图像到Colab并使用文件路径）
image = cv2.imread('IMG_4358.JPG')

# 确保图像加载成功
if image is not None:
    # 转换图像为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用中值模糊以减少噪声
    gray = cv2.medianBlur(gray, 5)

    # 检测边缘并增强
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 创建卡通效果
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # 合并原始图像和卡通效果
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 显示原始图像和卡通图像
    from matplotlib import pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray'), plt.title('Original Image')
    plt.axis('off')
    plt.subplot(122), plt.imshow(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB), cmap='gray'), plt.title('Cartoon Effect')
    plt.axis('off')
    plt.show()
else:
    print('无法加载图像')
