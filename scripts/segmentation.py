#!/usr/bin/env python

from read_write_model import read_model,qvec2rotmat
import numpy as np
import cv2

class SegmentPointCloud:

    def __init__(self, folder_path):    
        self.cameras = None 
        self.images = None
        self.points3D = None
        self.cameras, self.images, self.points3D = read_model(folder_path)  

    def getP(self, camera, image): 
        K = np.array([[camera.params[0], 0, camera.params[2]], [0, camera.params[1], camera.params[3]], [0, 0, 1]])
        R = qvec2rotmat(image.qvec)
        t = image.tvec.reshape(3,1)
        P = np.matmul(K,np.hstack((R, t)))
        return P
    
if __name__ == "__main__":
    folder_path= "/home/skumar/colmap_output"
    #folder_path = "/home/skumar/pixel-perfect-sfm/outputs/monarch-demo/ref_dir_not_locked/hloc"
    #folder_path = "/home/skumar/pixel-perfect-sfm/outputs/mvs"
    cameras, images, points3D = read_model(folder_path)
    print("Number of cameras: ", len(cameras))
    print("Number of images: ", len(images))
    print("Number of 3D points: ", len(points3D))   

    print("type(cameras): ", type(cameras))
    camera = None
    
    for k,v in images.items():
        print("k: ", k)
        print("v: ", v)
        exit()

    '''for k,v in cameras.items(): 
        print("k: ", k)
        print("id: ", v.id)
        print("v.model: ", v.model)
        print("v.width: ", v.width) 
        print("v.height: ", v.height)
        print("v.params: ", v.params)
        camera = v

    for k,v in images.items(): 
        print("k: ", k)
        print("v", v)
        s = SegmentPointCloud(folder_path)
        print(s.getP(camera, v))
        exit(0)
    camera_dict = dict(cameras[1])
    print("camera_dict.keys(): ", camera_dict.keys())

    for x in cameras[1]:
        print(x)

    #print("type(images[1]): ", type(images[1]))
    print("type(cameras[0]): ", type(cameras[1]))
    print("type(images[0]): ", type(images[0]))
    #SegmentPointCloud.getP(cameras[0], images[0])  
    '''