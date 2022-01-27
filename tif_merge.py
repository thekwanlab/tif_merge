#!/usr/bin/env python3

# Merges TIF files from grayscale to rgb
# Copyright (C) 2022 Yaman Qalieh

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Configuration: Change as needed
r_suffix = "tdt"
g_suffix = "gfp"
b_suffix = "dapi"
merged_suffix = "merged"

# Imports
import sys
import os
import cv2

# Could be changed later to use a command-line parser instead
def get_folder():
    return sys.argv[1]

if __name__ == '__main__':
    folder = get_folder()

    # Construct the _set_ of all identifiers
    nums = {filename.split("_")[0] for filename in os.listdir(folder)}

    for num in nums:
        # Read each channel
        r = cv2.imread(os.path.join(folder, f"{num}_{r_suffix}.tif"), cv2.IMREAD_GRAYSCALE)
        g = cv2.imread(os.path.join(folder, f"{num}_{g_suffix}.tif"), cv2.IMREAD_GRAYSCALE)
        b = cv2.imread(os.path.join(folder, f"{num}_{b_suffix}.tif"), cv2.IMREAD_GRAYSCALE)

        # Merge and write
        merged = cv2.merge((b,g,r))
        filepath = os.path.join(folder, f"{num}_{merged_suffix}.tif")
        cv2.imwrite(filepath, merged)

        print("merged", num, "to", filepath)
