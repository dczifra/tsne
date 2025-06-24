# t-SNE

**Compatible versions:**
* I.
    * CUDA         : 11.3
    * Python(Conda): 3.8
    * Faiss        : 1.6.5
* II.

## How to install
```
git clone https://github.com/dczifra/tsne.git
cd tsne
git submodule update --init --recursive
./docker/build.sh
./docker/run.sh
./install_tsne.sh
```



# Documentation

## Test install CannyLab/t-SNE [OLD]:
```
./docker/build.sh
./docker/run.sh
cd tsne-cuda
git submodule init
git submodule update
mkdir build
cd build
cmake ..
make -j16
cd python
pip install -e .
python -c "import tsnecuda;tsnecuda.test()"
```


## Unseful links for install
* [Reference doc](https://github.com/CannyLab/tsne-cuda/blob/main/INSTALL.md)
* [FAISS](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
    * Recommended to install with `conda`
    * Possible to install from source
* [Conda](https://mjtdev.medium.com/how-to-conda-miniconda-anaconda-in-docker-in-2022-5579cafc44fd)

From source template:
```
RUN mkdir -p ${OPTIX_INSTALL_PATH}
WORKDIR ${OPTIX_INSTALL_PATH}
RUN cmake \
    -DCMAKE_LIBRARY_PATH=/usr/local/cuda/lib64/stubs \
    /src/optixlib && make -j8
```