#!/usr/bin/env python

from read_write_fused_vis import read_fused

import struct
import argparse

def read_binary_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read(4)

        while data:
            value = struct.unpack("<I", data)[0]
            print(value)
            #data = file.read(4)
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a binary file with little-endian byte ordering.")
    parser.add_argument("--f1", help="Path to the binary file.")
    parser.add_argument("--f2", help="Path to the binary file.")

    args = parser.parse_args()
    #read_binary_file(args.file_path)
    point3d_df = read_fused(args.f1, args.f2)
    print("type(point3d_df): ", type(point3d_df))
    #print("point3d_df[1]: ", point3d_df[1])
    print("type(point3d_df[1]): ", type(point3d_df[1]))
    print("point3d_df[1].num_visible_images: ", point3d_df[1].num_visible_images)
    print("point3d_df[1].visible_image_idxs: ", point3d_df[1].visible_image_idxs)
