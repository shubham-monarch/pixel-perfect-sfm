#You must set $COLMAP_EXE_PATH to
#the directory containing the COLMAP executables
COLMAP_EXE_PATH=/usr/local/bin
USR_PATH=/home/skumar
INPUT_PATH=$USR_PATH/pixel-perfect-sfm/outputs/monarch-demo/ref_locked/

$COLMAP_EXE_PATH/colmap rig_bundle_adjuster --input_path $INPUT_PATH --output_path . --rig_config_path rig.json --BundleAdjustment.refine_focal_length 0 --BundleAdjustment.refine_extra_params 0 --BundleAdjustment.refine_extrinsics 0 
