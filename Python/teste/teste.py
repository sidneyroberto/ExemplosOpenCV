import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('imagens/maca.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

verde_min = np.array([25, 100, 50], np.uint8)
verde_max = np.array([120, 255, 255], np.uint8)

mascara_inversa = cv2.inRange(img_hsv, verde_min, verde_max)
mascara = cv2.bitwise_not(mascara_inversa)

mascara_rgb = cv2.cvtColor(mascara, cv2.COLOR_GRAY2RGB)

imagem_mascarada = cv2.bitwise_and(img, mascara_rgb)

mascara_branco_substituido = cv2.addWeighted(imagem_mascarada, 1, cv2.cvtColor(mascara_inversa, cv2.COLOR_GRAY2RGB), 1, 0)
imagem_branco_substituido = cv2.cvtColor(mascara_branco_substituido, cv2.COLOR_BGR2RGB)

plt.imshow(imagem_branco_substituido)
plt.show()
'''
green = np.uint8([[[0,40,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
'''

