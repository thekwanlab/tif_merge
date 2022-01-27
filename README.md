# Usage:

1. First load the python3.X-anaconda module of your choice, which has the dependencies for
preloaded with opencv-python on the cluster. For example:

`ml python3.7-anaconda openv opencv-python/3`

2. Next, run the script:

`python3 tif_merge.py <relative-path-to-folder-from-current-location>`

Merges each group of tifs to `<relative-path-to-folder>/<id>_merged.tif`

By default, the following stains are used. This can be changed by modifying the start of tif_merge.py
r = tdt
g = gfp
b = dapi

NOTE: The relative-path-to-folder must only contain the tifs to be merged

# License
GPLv3
