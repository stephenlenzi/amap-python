# Usage
```bash
amap /path/to/raw/data /path/to/output/directory -x 2 -y 2 -z 5
```

### Arguments
#### Mandatory
* Path to the directory of the images. 
Can also be a text file pointing to the files.  
 * Output directory for all intermediate and final 
results

**Either**
* `-x` or `--x-pixel-um` Pixel spacing of the data in the first dimension, 
specified in um.
* `-y` or `--y-pixel-um` Pixel spacing of the data in the second dimension, 
specified in um.
* `-z` or `--z-pixel-um` Pixel spacing of the data in the third dimension, 
specified in um.

**Or**
* `--metadata` Metadata file containing pixel sizes (any format supported 
by [micrometa](https://github.com/adamltyson/micrometa) can be used).
  If both pixel sizes and metadata are provided, the command line arguments 
  will take priority.

#### Additional options
* `-d` or `--downsample` Paths to N additional channels to downsample to the 
same coordinate space.
* `--no-save-downsampled` Dont save the downsampled brain before filtering.
* `--registration-config` To supply your own, custom registration configuration file
* `--sort-input-file` If set to true, the input text file will be sorted using 
natural sorting. This means that the file paths will be
sorted as would be expected by a human and 
not purely alphabetically

##### Input data options
 If the supplied data does not match the NifTI standard 
 orientation (origin is the most ventral, posterior, left voxel), 
 then the atlas can be flipped to match the input data:
 * `--flip-x` Flip the sample brain along the first dimension for 
 atlas registration
 * `--flip-y` Flip the sample brain along the second dimension for 
 atlas registration
 * `--flip-z` Flip the sample brain along the third dimension for 
 atlas registration
  * `--orientation` The orientation of the sample brain `coronal`, `saggital`
 or `horizontal`


##### Misc options
* `--n-free-cpus` The number of CPU cores on the machine to leave unused by the program to spare resources.

* `--debug` Debug mode. Will increase verbosity of logging and save all intermediate files for diagnosis of software issues.


##### Advanced options
**Affine registration**
* `--affine-n-steps` Registration starts with further downsampled versions of the original data to optimize the global fit of the result and prevent "getting stuck" in local minima of the similarity function. This parameter determines how many downsampling steps are being performed, with each step halving the data size along each dimension.

* `--affine-use-n-steps` Determines how many of the downsampling steps defined by `--affine-n-steps` will have their registration computed. The combination `--affine-n-steps 3 --affine-use-n-steps 2` will e.g. calculate 3 downsampled steps, each of which is half the size of the previous one but only perform the registration on the 2 smallest resampling steps, skipping the full resolution data. Can be used to save time if running the full resolution doesn't result in noticeable improvements.


**Freeform registration**
* `--freeform-n-steps` Registration starts with further downsampled versions of the original data to optimize the global fit of the result and prevent "getting stuck" in local minima of the similarity function. This parameter determines how many downsampling steps are being performed, with each step halving the data size along each dimension.

* `--freeform-use-n-steps` Determines how many of the downsampling steps defined by `--freeform-n-steps` will have their registration computed. The combination `--freeform-n-steps 3 --freeform-use-n-steps 2` will e.g. calculate 3 downsampled steps, each of which is half the size of the previous one but only perform the registration on the 2 smallest resampling steps, skipping the full resolution data. Can be used to save time if running the full resolution doesn't result in noticeable improvements.

* `--bending-energy-weight` Sets the bending energy, which is the coefficient of the penalty term, preventing the freeform registration from overfitting. The range is between 0 and 1 (exclusive) with higher values leading to more restriction of the registration.

* `--grid-spacing` Sets the control point grid spacing in x, y & z. Positive values are interpreted as real values in mm, negative values are interpreted as the (positive) distances in voxels. Smaller grid spacing allows for more local deformations but increases the risk of overfitting.

* `--smoothing-sigma-floating` Adds a gaussian smoothing to the floating image (the one being registered), with the sigma defined by the number. Positive values are interpreted as real values in mm, negative values are interpreted as distance in voxels.

* `--smoothing-sigma-reference` Adds a gaussian smoothing to the reference (the one being registered to) image, with the sigma defined by the number. Positive values are interpreted as real values in mm, negative values are interpreted as distance in voxels.

* `--histogram-n-bins-floating` Number of bins used for the generation of the histograms used for the calculation of Normalized Mutual Information on the floating image 

* `--histogram-n-bins-reference` Number of bins used for the generation of the histograms used for the calculation of Normalized Mutual Information on the reference image 

#### Visualisation options
* `--no-boundaries` Do not precompute the outline images 
(if you don't want to use amap_vis)


Full command-line arguments are available with `amap -h`