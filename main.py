import cv2
import matplotlib.pyplot as plt
import easyocr

img = cv2.imread("resim.png")


reader=easyocr.Reader(['tr','en'],gpu=True)
threshold=0.25
text= reader.readtext(img)


for i in range(len(text)):
    print(text[i][1])

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()