# Orientation Mapping using Electron Channeling - Computer Vision Approach

This is a series of scripts to reproduce our work aligning and reconstructing 3D orientation maps from channeling image series on a stage-rocked specimen.  Align will load all of the images in the current directory and bring them on to a common coordinate frame using the SIFT implementation in openCV.  MakeBand will then load a keyed segementation from these images (msot often found using watershed) and produce a band map for every crystal in the polycrystalline sample.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Currently tested with:

```
python 3.5.3
openCV 3.30
multiprocess 0.70.5
numpy 1.11.3
scikit-learn 0.18.1
scikit-image 0.12.3
h5py 2.6.0
```

## Authors

* **Karl Hujsak** - *Initial work* - [khujsak](https://github.com/khujsak)


## Acknowledgments

* PyImageSearch
