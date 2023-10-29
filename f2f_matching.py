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
        self.m_ref = [str(p.relative_to(images)) for i, p in enumerate((images / 'masked_images/').iterdir())] 
        
    '''sorts the files in items by the temporal order of the file names'''
    def temporal_sort(self, item):
        assert isinstance(item, list), "input must be a list"
        assert all(isinstance(x, str) for x in item), "input must be a list of strings"
        return sorted(item, key = lambda x: int(((x.split("/")[-1]).split(".")[0]).split("_")[0]))

    ''' returns the matches between t_ref[i] and t_ref[j]'''
    def get_matches(self, t_ref, matches, i, j):
        p_name = t_ref[i].split("/")[-1]
        p_key = "masked_images-" + p_name #parent_key
        c_name = t_ref[j].split("/")[-1]
        c_key = "masked_images-" + c_name #child key
        p_kps = get_keypoints(self.features, t_ref[i]) #parent kps
        c_kps = get_keypoints(self.features, t_ref[j]) #child kps
        with h5py.File(matches, 'r') as f:
            matches_ = f[p_key][c_key]['matches0'][:]
            score_ = f[p_key][c_key]['matching_scores0'][:]
            #valid = (matches_ > -1 and score_ > 0.5)
            valid = np.logical_and(matches_ > -1, score_ > 0.8)
            mkp1 = p_kps[valid]
            mkp2 = c_kps[matches_[valid]]
            return mkp1, mkp2

    def run_pipeline(self):
        self.m_ref = self.temporal_sort(self.m_ref)
        t_ref = self.m_ref[100:105]
        en = len(t_ref)
    
        for i in range(1, en):
            plot_images([read_image(images / t_ref[r]) for r in [i,i-1]], dpi=50)
            kps1 = get_keypoints(features, t_ref[i])
            kps2 = get_keypoints(features, t_ref[i-1])
            mkp1, mkp2 = self.get_matches(t_ref, self.matches, i, i-1)
            plot_matches(mkp1, mkp2)
            plt.waitforbuttonpress()
            plt.close()

def print_summary(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(f"Dataset: {name} (shape={obj.shape}, dtype={obj.dtype})")
    elif isinstance(obj, h5py.Group):
        print(f"Group: {name}")


if __name__ == "__main__":

    images = Path('datasets/monarch/')
    outputs = Path('outputs/monarch-demo/')
    features = outputs / 'features.h5'
    matches = outputs / 'matches.h5'
    f2f_ = f2f(images, outputs, features, matches)
    f2f_.run_pipeline()
    #with h5py.File(matches, 'r') as f: 
     #   f.visititems(print_summary)
    #f2f_.get_matches();



