# Visualisation

amap has a built in visualisation function (built using [napari](https://github.com/napari/napari)).

#### Usage
```bash
amap_vis /path/to/amap/output/directory
```

#### Mandatory
* Path to amap output directory


#### Additional options
* `-r` or `--raw`. Rather than viewing the downsampled data, view the raw data 
at full resolution. This will stream image planes as required, and so may be 
slow.
* `-c` or `--raw-channels` Paths to N additional channels to view. 
Will only work if using the raw image viewer.

N.B. If you have a high-resolution monitor, the scaling of the viewer may not work,
this is a [known napari issue](https://github.com/napari/napari/issues/367).

![amap_viewer](https://raw.githubusercontent.com/SainsburyWellcomeCentre/amap-python/master/resources/amap_vis.gif)
