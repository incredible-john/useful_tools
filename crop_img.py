import cv2
import os

w, h = 1920, 1080
x, y = 3300, 2460
rootdir = 'ship/'
imgs = os.listdir(rootdir)
times = 50
offset = 0
for idx, i in enumerate(imgs):
    img = cv2.imread(rootdir + i)
    # w,h,g = img.shape
    # print(w,h)
    dst = img[y-h//2 + offset: y+h//2 + offset, x-w//2: x+w//2]   # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("ship_o/" + i, dst)  # 写入图片
    if times:
        offset += 15
    if times > 0:
        times -= 1
    print(idx)