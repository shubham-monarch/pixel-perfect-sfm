### Software Setup

##### COLMAP 

```
git clone --recursive git@github.com:shubham-monarch/colmap.git
git checkout rig-ba-setup
cd colmap 
mkdir build && cd build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=all -DCMAKE_INSTALL_PREFIX=/usr/local/ -GNinja  
ninja
sudo ninja install 
```

##### HLoc 
```
git clone --recursive git@github.com:shubham-monarch/Hierarchical-Localization.git
# matching script for stereo cameras
git checkout 40337cda64fa7c3ff3dac99082fcb287ebb2333d
cd Hierarchical-Localization/
python -m pip install -e .
```

##### PixSFM 
```
# install COLMAP following colmap.github.io/install.html#build-from-source, tag 3.8
sudo apt-get install libhdf5-dev
git clone git@github.com:shubham-monarch/pixel-perfect-sfm.git --recursive
git checkout rig_ba
cd pixel-perfect-sfm
pip install -r requirements.txt
```
> Build [pycolmap](https://github.com/colmap/pycolmap) (v0.4) and [pyceres](https://github.com/cvg/pyceres)(v1.0) from source.

Finally build and install the `pixsfm` package: 
``` 
pip install -e .
```

### Folder Setup
-  Create folders named `left` and `right` at the `images` location specified in [sparse_reconstruction.ipynb](sparse_reconstruction.ipynb) notebook and move/copy the corresponding **masked** images to the respective folders. It is important to make sure that the corresponding images/frames have the **same names** in the `left`/`right` folder.  
> Currently, `images` folder points to `pixel-perfect-sfm/datasets/monarch/` 
> If the tractor hood is **not masked** in the input images, one can use the `draw_box_around_tractor_hood` function in [sparse_reconstruction.ipynb](sparse_reconstruction.ipynb) to mask the images.

### Running Sparse Reconstruction

Run the [sparse_reconstruction.ipynb](sparse_reconstruction.ipynb) notebook to generate the sparse model. This would generate the **sparse** model at the specified output location i.e. `ref_dir_locked`
 
> The sparse model's **output location** is specified inside the `sfm.reconstruction` function. It is currently set to the `ref_dir_locked` variable.

> Camera instrinsics' optimization has been **locked**. 

> Same camera intrinsics is being **shared** for all the images in a **sub-folder** i.e. all the images in the `left` folder share the same camera intrinsics amongst each other and all the images in the `right` folder share the same camera intrinsics amongst each other.


### Running Rig Bundle Adjustment 
- Create a folder named `rig_ba_model` at the `HOME` location:
- Copy [rig.json](rig.json) and [rig_ba.sh](rig_ba.sh) to this folder.
```
cd $HOME
mkdir rig_ba_model && cd rig_ba_model
cp ~/pixel-perfect-sfm/rig.json .
cp ~/pixel-perfect-sfm/rig_ba.sh .
```
- Update the follwing variables in `rig_ba.sh`:
  - `COLMAP_EXE_PATH` (default to `/usr/bin/colmap`)
  - `INPUT_PATH` (provide the path to the **sparse model**, defaults to `$HOME/pixel-perfect-sfm/outputs/monarch-demo/ref-locked/`)
  - `OUTPUT_PATH` (defaults to the current folder i.e. `$PWD`)

- Finally execute the `rig_ba.sh` script from inside the `rig_ba_model` folder: 
```
sudo chmod +x rig_ba_script.sh
sudo ./rig_ba_script
```

This would call `COLMAP`'s `rig_bundle_adjuster` api on the previously generated **sparse model** and generate the **rig-bundle-adjusted-sparse** model at the `OUTPUT_PATH` specified in [rig_ba.sh](rig_ba.sh). 

We can now run the [rel_pose_calc.ipynb](rel_pose_calc.ipynb) notebook to **compare** the **relative** camera poses **before** and **after** running the `rig_bundle_adjuster`.

### Dense reconstruction  
- Create a folder named `dense_model` at the `HOME` location:
```
cd $HOME
mkdir dense_model
```
- **Undistort** input images by running the following commands in the terminal from the **HOME** location:
```
cd $HOME
export IMAGE_PATH=$HOME/pixel-perfect-sfm/datasets/monarch 
export INPUT_PATH=$HOME/rig_ba_model
export OUTPUT_PATH=$HOME/dense_model
colmap image_undistorter --image_path $IMAGE_PATH --input_path $INPUT_PATH --output_path $OUTPUT_PATH
```

- Replace the `run-colmap-geometric.sh` file inside the `$HOME/dense_model` folder with the [one](run-colmap-geometric.sh) inside the `~/pixel-perfect-sfm` folder

```
cp ~/pixel-perfect-sfm/run-colmap-geometric.sh ~/dense_model/
```
- Update `COLMAP_EXE_PATH` variable inside the script (default `COLMAP_EXE_PATH=/usr/bin/colmap`)
- Finally run the script:
```
cd $HOME/dense_model
sudo chmod +x run-colmap-geometric.sh
sudo ./run-colmap-geometric.sh
```

This would generate the **dense** pointcloud file named `fused.ply` inside the `dense_model` folder. 
