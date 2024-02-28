# You must set $COLMAP_EXE_PATH to 
# the directory containing the COLMAP executables.
COLMAP_EXE_PATH="/usr/local/bin"

$COLMAP_EXE_PATH/colmap patch_match_stereo \
  --workspace_path . \
  --workspace_format COLMAP \
  --PatchMatchStereo.max_image_size 2000 \
  --PatchMatchStereo.geom_consistency true
$COLMAP_EXE_PATH/colmap stereo_fusion \
  --workspace_path . \
  --workspace_format COLMAP \
  --input_type geometric \
  --output_path ./fused.ply
