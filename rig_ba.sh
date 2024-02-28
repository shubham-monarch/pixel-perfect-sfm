#You must set $COLMAP_EXE_PATH to
#the directory containing the COLMAP executables
COLMAP_EXE_PATH=/usr/local/bin

$COLMAP_EXE_PATH/colmap rig_bundle_adjuster --input_path /home/skumar/stereo_colmap_cli_output/sparse --output_path . --rig_config_path /home/skumar/rig_stereo_colmap_cli_output/rig.json --BundleAdjustment.refine_focal_length 0 --BundleAdjustment.refine_extra_params 0 --BundleAdjustment.refine_extrinsics 0 
