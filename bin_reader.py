#!/usr/bin/env python

from pathlib import Path 
import struct 
from PIL import Image, ExifTags


if __name__ == "__main__": 
    '''
    file_path = Path("outputs/monarch-demo/ref/cameras.bin")
    try:
        with open(file_path, 'rb') as file:
            # Read the number of cameras in the file
            num_cameras = struct.unpack('i', file.read(4))[0]

            # Loop over each camera in the file
            for i in range(num_cameras):
                # Read the camera ID and image size
                camera_id, width, height = struct.unpack('iii', file.read(12))

                # Read the camera parameters
                params = struct.unpack('ffffffffffff', file.read(48))

                # Print the camera parameters
                print(f"Camera {camera_id}:")
                print(f"  Image size: {width} x {height}")
                print(f"  Focal length: {params[0]}")
                print(f"  Principal point: ({params[2]}, {params[3]})")
                print(f"  Skew: {params[4]}")
                print(f"  Distortion coefficients: {params[5:]}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError as e:
        print(f"An error occurred: {e}")
    '''
    
# Open the image file
    image_path = Path("datasets/monarch/masked_images/0_left.jpg")
    try:
        with Image.open(image_path) as image:
            # Get the EXIF metadata
            exif_data = image._getexif()

            # Print the EXIF metadata
            for tag_id, value in exif_data.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                print(f"{tag}: {value}")
    except FileNotFoundError:
        print(f"File '{image_path}' not found.")
    except IOError as e:
        print(f"An error occurred: {e}")