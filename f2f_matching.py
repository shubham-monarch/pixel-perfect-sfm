#!/usr/bin/env python

from pathlib import Path
from hloc.utils import viz
from hloc.utils.viz import plot_keypoints, save_plot
from hloc.visualization import read_image, plot_images, plot_matches
from hloc.utils.io import get_keypoints
import matplotlib.pyplot as plt
import numpy as np
import os
import h5py


class f2f():
    def __init__(self, images, ouputs, features, matches):  
        self.images = images
        self.outputs = outputs
        self.features = features
        self.matches = matches
        #masked_references
        self.m_ref = [str(p.relative_to(images)) for i, p in enumerate((images / 'masked_images/').iterdir())] 
        #trimming the list of masked references
        
    '''sorts the files in items by the temporal order of the file names'''
    def temporal_sort(self, item):
        assert isinstance(item, list), "input must be a list"
        assert all(isinstance(x, str) for x in item), "input must be a list of strings"
        return sorted(item, key = lambda x: int(((x.split("/")[-1]).split(".")[0]).split("_")[0]))


    def print_summary(self, name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name} (shape={obj.shape}, dtype={obj.dtype})")
        elif isinstance(obj, h5py.Group):
            print(f"Group: {name}")

    def get_matches(self):
        t_ref = self.m_ref[100:105]
        filename = self.matches
        en = len(t_ref)
        for i in range(en - 1):
            print(f"i: {i}")
            img_name = t_ref[i].split("/")[-1]
            p_key = "masked_images-" + img_name #parent_key
            j = i + 1
            img_name = t_ref[j].split("/")[-1]
            c_key = "masked_images-" + img_name #child key
            ids = [i,j]
            plot_images([read_image(self.images / t_ref[r]) for r in ids], dpi=50)
            p_kps = get_keypoints(self.features, t_ref[i]) #parent kps
            c_kps = get_keypoints(self.features, t_ref[j]) #child kps
            with h5py.File(filename, 'r') as f:
                matches_ = f[p_key][c_key]['matches0'][:]
                valid = matches_ > -1
                mkp1 = p_kps[valid]
                mkp2 = c_kps[matches_[valid]]
                plot_matches(mkp1, mkp2)
            plt.waitforbuttonpress()
            plt.close()
            
        
        return
        #frame_tensor = frame2tensor(frame, device)
        #pred = matching({**last_data, 'image1': frame_tensor})
        '''
        kpts0 = last_data['keypoints0'][0].cpu().numpy()
        kpts1 = pred['keypoints1'][0].cpu().numpy()
        matches = pred['matches0'][0].cpu().numpy()
        confidence = pred['matching_scores0'][0].cpu().numpy()
        timer.update('forward')
        
        valid = matches > -1
        mkpts0 = kpts0[valid]
        mkpts1 = kpts1[matches[valid]]
        '''
        cnt = 0 
        with h5py.File(filename, 'r') as f:
            g1 = "masked_images-102_left.jpg"
            g2 = "masked_images-101_left.jpg"
            matches = f[g1][g2]['matches0']
            valid = matches > -1
            mkp1 = kp1[valid]
            mkp2 = kp2[matches[valid]]
            plot_matches(mkp1, mkp2)
            '''
            for group in f[g1]:
                print(f"items: {group}")
                #print(f"items.shape: {f[g1][items].shape}")
                print(f"items.dtype: {type(f[g1][group])}")
                for item in f[g1][group]:
                    print(f"item: {item}")
                    print(f"item.shape: {f[g1][group][item].shape}")
                    data = f[g1][group][item][:]
                    #print(f"data: {data[0]}")
                    #print(f"item.dtype: {f[g1][group][item].dtype}")
                    #print(f"item: {f[g1][group][item]}")
                    print(f"item: {f[g1][group][item].__array__()}") 
                    #print(f"item: {f[g1][group][item].__array__().shape}") 
                    #print(f"item: {f[g1][group][item].__array__().dtype}") 
            '''        
    def run_pipeline(self):
        self.m_ref = self.temporal_sort(self.m_ref)
        return
        t_ref = self.m_ref[100:101]
        print(f"t_ref: {t_ref}")    
        #self.get_matches(self.matches)
        
        plot_images([read_image(images / r) for r in t_ref], dpi=50)
        kps_list_ = [] 
        for r in t_ref:
            kps = get_keypoints(features, r)
            print(f"kps.shape: {kps.shape}")
            kps_list_.append(kps)   
        #plot_keypoints(kps_list_, colors = "red",  ps = 10)
        print(f"Printing kps_list_")
        for i in range(1, len(kps_list_)):
            print(f"i: {kps_list_[i].shape}")
            plot_matches(kps_list_[i], kps_list_[i-1])
        
        self.get_matches(self.matches, kps_list_[0], kps_list_[1])
        plt.waitforbuttonpress()
        

if __name__ == "__main__":

    images = Path('datasets/monarch/')
    outputs = Path('outputs/monarch-demo/')
    features = outputs / 'features.h5'
    matches = outputs / 'matches.h5'
    f2f_ = f2f(images, outputs, features, matches)
    f2f_.run_pipeline()
    f2f_.get_matches();



