# -*- coding: utf-8 -*-
import numpy as np
import cv2
import glob

# 需要将下面三组数据替换成你计算出来的新数据
DIM=(1920, 1080)
K=np.array([[847.1189093859566, 0.0, 1003.1842217656019], [0.0, 841.0055737619359, 526.5010198089786], [0.0, 0.0, 1.0]])
D=np.array([[0.04546104968860118], [-0.2072673390197449], [0.2432519260920477], [-0.1288444975286356]])


def undistort(img):

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted_img", undistorted_img)
    cv2.imshow("img", img)
    cv2.waitKey(1)


if __name__ == '__main__':
    # images = glob.glob("./cam/*.jpg")
    # print(images)
    cap = cv2.VideoCapture(1)
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, -1)  # 相机 180° 翻转代码
        undistort(img)
