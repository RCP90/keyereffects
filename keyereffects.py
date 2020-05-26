import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1=cv2.imread("homework2.png",1)
m2=np.full((612,1087), 255, np.uint8)
w1 = m1.shape[0]
h1 = m1.shape[1]

for w in range(w1):
    for h in range(h1):
        if m1[w][h][0] == 0 and m1[w][h][1] ==0 and m1[w][h][2]==255:
            m2[w][h]=0

cv2.imshow("m1",m1)
cv2.imshow("m2",m2)

cv2.waitKey(0)
cv2.destroyAllWindows()
