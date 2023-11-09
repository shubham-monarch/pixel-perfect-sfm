from open3d import visualization, io    
from pathlib import Path

def main():
    file = Path("outputs/mvs/fused.ply")
    cloud = io.read_point_cloud(str(file)) # Read point cloud
    visualization.draw_geometries([cloud])    # Visualize point cloud      

if __name__ == "__main__":
    main()