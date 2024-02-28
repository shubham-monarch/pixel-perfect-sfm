The three main steps involved are => 
0. Initial Project Setup
1. Sparse reconstruction 
2. Rig Bundle Adjustment
3. Manually Scaling the model 
4. Dense reconstructions


Initial Project Setup => 
- Setup `COLMAP`

```git clone git@github.com:shubham-monarch/colmap.git
git checkout d4202d2438af52ea8dbf505bc069b786ea48d1a1
cd colmap 
mkdir build && cd build 
cmake .. -DCMAKE_CUDA_ARCHITECTURES=all -GNinja
ninja
sudo ninja install 
```


-  Mask the tractor hood in all the images.(refer `draw_box_around_tractor_hood` function in `stereo_dense.ipynb` notebook). 
-  Create folders named ``left` and `right` at the `images` location specified in `stereo_dense.ipynb` notebook and move/copy the corresponding images to the respective folders.
- Install colmap / pycolmap/ pixSFM/Hloc pointing to appropriate commit


Sparse Reconstruction => 
- Camera instrinsics optimization is locked. 
- Same camera is being shared for all the images in a folder.

Run the `stereo_dense.ipynb` notebook to generate the sparse model at the location specified in the `sfm.reconstruction` function. Currently it is set to `ref_dir_locked`. 


Rig Bundle Adjustment =>
Create a folder named `rig_bundle_adjustment`. Add a rig.json file inside the folder. 

Run the following through cli => 
`colmap rig_bundle_adjuster --input_path <path_to_sparse_folder> --output_path . --rig_config_path <path_to_rig.json file> 
--BundleAdjustment.refine_focal_length 0 --BundleAdjustment.refine_extra_params 0 --BundleAdjustment.refine_extrinsics 0`

This would run `rig_bundle_adjuster` on the sparse model and generate a new bundle-adjusted model at the `output` folder specified above.

Manually scaling the model =>
Running the above command would also scale the model with a hard-coded scale factor.

[TO-DO]: Need to a python binding for the same in pycolmap.


Dense reconstruction => 
- Create a folder named 'dense_reconstruction' and copy the `run-colmap-geometric.sh` script inside it. 
- [TO-DO] update the variables inside the script
- sudo chmod +x run-colmap-geometric.sh
- sudo ./run-colmap-geometric.sh

This would generate the dense pointcloud file named fused.ply inside the `dense_reconstruction` folder. 

