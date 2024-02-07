#pragma once

#include <ceres/ceres.h>
//#include <colmap/base/cost_functions.h>
//#include <colmap/base/projection.h>

#include <colmap/estimators/cost_functions.h>
#include <colmap/scene/projection.h>
#include <colmap/util/types.h>

#include "base/src/projection.h"

namespace pixsfm {

/*******************************************************************************
Initialization Wrappers: (resolving camera model templates)
*******************************************************************************/

ceres::CostFunction* CreateGeometricCostFunctor(
    int camera_model_id, const Eigen::Vector2d& point2D) {
  switch (camera_model_id) {
#define CAMERA_MODEL_CASE(CameraModel)                                        \
  case static_cast<int>(colmap::CameraModel::model_id):                                         \
    return colmap::ReprojErrorCostFunction<colmap::CameraModel>::Create( \
        point2D);                                                             \
    break;
    CAMERA_MODEL_SWITCH_CASES
#undef CAMERA_MODEL_CASE
  }
}

ceres::CostFunction* CreateGeometricConstantPoseCostFunctor(
    int camera_model_id, const Eigen::Vector4d& qvec,
    const Eigen::Vector3d& tvec, const Eigen::Vector2d& point2D) {
      Eigen::Quaterniond rotation_(qvec);
      colmap::Rigid3d cam_from_world_(rotation_, tvec);
  switch (camera_model_id) {
#define CAMERA_MODEL_CASE(CameraModel)                       \
  case static_cast<int>(colmap::CameraModel::model_id):                        \
    return colmap::ReprojErrorConstantPoseCostFunction< \
        colmap::CameraModel>::Create(cam_from_world_, point2D);   \
    break;
    CAMERA_MODEL_SWITCH_CASES
#undef CAMERA_MODEL_CASE
  }
}

}  // namespace pixsfm