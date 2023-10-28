#!/usr/bin/env python

from pathlib import Path
from hloc.utils import viz
from hloc.utils.viz import plot_keypoints, save_plot
from hloc.visualization import read_image
from hloc.utils.io import get_keypoints
import matplotlib.pyplot as plt
import numpy as np
import os

class f2f():
    def __init__(self, images, ouputs, features, matches):  
        self.images = images
        self.outputs = outputs
        self.features = features
        self.matches = matches
        #masked_references
        self.m_ref = [str(p) for i, p in enumerate((images / 'masked_images/').iterdir())] 

    def temporal_sort(self, item):
        assert isinstance(item, list), "input must be a list"
        assert all(isinstance(x, str) for x in item), "input must be a list of strings"
        return sorted(item, key = lambda x: int(((x.split("/")[-1]).split(".")[0]).split("_")[0]))

    def run_pipeline(self):
        #viz.plot_images([read_image(images / r) for r in ref_trim_], dpi=50)
        print(f"references: {self.m_ref[0:10]}")
        self.m_ref = self.temporal_sort(self.m_ref)
        print(f"references: {self.m_ref[0:10]}")
        return




if __name__ == "__main__":

    images = Path('datasets/monarch/')
    outputs = Path('outputs/monarch-demo/')
    features = outputs / 'features.h5'
    matches = outputs / 'matches.h5'
    f2f_ = f2f(images, outputs, features, matches)
    f2f_.test_run()



