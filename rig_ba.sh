#You must set $COLMAP_EXE_PATH to
#the directory containing the COLMAP executables
COLMAP_EXE_PATH=/usr/local/bin
INPUT_PATH=$HOME/pixel-perfect-sfm/outputs/monarch-demo/ref_locked/
OUTPUT_PATH=$PWD

$COLMAP_EXE_PATH/colmap rig_bundle_adjuster --input_path $INPUT_PATH --output_path $OUTPUT_PATH --rig_config_path rig.json --BundleAdjustment.refine_focal_length 0 --BundleAdjustment.refine_extra_params 0 --BundleAdjustment.refine_extrinsics 0 
