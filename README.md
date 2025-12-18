# t-SNE

**Compatible versions:**
* I.
    * CUDA         : 11.3
    * Python(Conda): 3.8
    * Faiss        : 1.6.5
* II.
    * CUDA         : 12.4
    * Python(Conda): 3.11
    * Faiss        : 1.7.4 (--> 1.9.0)

## How to install
I. Clone and init submodules
```
git clone https://github.com/dczifra/tsne.git
cd tsne
git submodule update --init --recursive
```

II./a Build and run docker container (Inside docker tsne is already installed)
* Use `--ubuntu` flag for the `nvidia/cuda:12.4.1-devel-ubuntu22.04` based image, else `amazonlinux:2023` will be the base image.
```
./docker/build.sh
./docker/run.sh
```

II./b Use conda
```
conda install -c pytorch -c nvidia faiss-gpu=1.9.0
conda install scikit-learn torchvision matplotlib pandas tqdm seaborn memory_profiler
./install_tsne.sh
```

III. Test
```
python src/random_test.py
```


# Documentation

## Unseful links for install
* [Reference doc](https://github.com/CannyLab/tsne-cuda/blob/main/INSTALL.md)
* [FAISS](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
    * Recommended to install with `conda`
    * Possible to install from source
* [Conda](https://mjtdev.medium.com/how-to-conda-miniconda-anaconda-in-docker-in-2022-5579cafc44fd)




# Notes

## Open questions:
* What exactly affects whether it goes into batch mode or not?
* (seems to be that nearest_neighbors variable, but how is that changing if we are always leaving it at default of 32)
* What is the current limit of data size, in your version where you made the FAISS fix ?
* We want to understand if batch mode affects the results or not (but we’re pretty sure it does not, since old tsne-cuda was using batch mode)
