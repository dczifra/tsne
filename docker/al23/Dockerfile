#FROM amazonlinux:2023
FROM tsnecuda_al23

# === Install ap packages ===
RUN yum -qqy update && \
    DEBIAN_FRONTEND=noninteractive yum -qqy install \
    gtest-devel gflags-devel openblas-devel \
    wget git tar make -y \
    && rm -rf /var/lib/apt/lists/*

RUN dnf group install -y "Development Tools"
RUN dnf install gcc-c++ -y

# === Install CMake 3.23.1 ===
RUN wget https://github.com/Kitware/CMake/releases/download/v3.23.1/cmake-3.23.1-linux-x86_64.sh -O /tmp/cmake.sh && \
    bash /tmp/cmake.sh --skip-license --prefix=/usr/local && \
    rm /tmp/cmake.sh

# === Install miniconda ===
RUN mkdir -p /opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O /opt/conda/miniconda.sh \
 && bash /opt/conda/miniconda.sh -b -p /opt/miniconda
ENV PATH="/opt/miniconda/bin:$PATH"
ENV CMAKE_PREFIX_PATH=/opt/miniconda

# === Install FAISS ===
RUN conda init bash
RUN conda install python=3.11
RUN conda install -c pytorch -c nvidia faiss-gpu=1.9.0 -y


# === Install pip packages for tests ===
RUN conda install scikit-learn torchvision matplotlib pandas tqdm seaborn memory_profiler

# === Install g++ 11, for <=cuda-12.8 ===
#RUN cd /usr/src && \
#    wget https://ftp.gnu.org/gnu/gcc/gcc-11.5.0/gcc-11.5.0.tar.xz && \
#    tar xf gcc-11.5.0.tar.xz && \
#    cd gcc-11.5.0 && ./contrib/download_prerequisites

#RUN mkdir /usr/src/gcc-11-build
#RUN cd /usr/src/gcc-11-build && \
#    ../gcc-11.5.0/configure \
#  --prefix=/opt/gcc-11 \
#  --enable-languages=c,c++ \
#  --disable-multilib && \
#  make -j$(nproc) && \
#  make install 

#ENV PATH="/opt/gcc-11/bin:$PATH"


# Lock cuda to version 12.8 ==> supports default gcc-14
RUN dnf install -y cuda-toolkit-12-8

ENV CUDA_HOME="/usr/local/cuda-12.8"
ENV PATH="$CUDA_HOME/bin:$PATH"
ENV LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"

# === Install CannyLab's t-SNE ===
COPY src/external/tsne-cuda /tsne-cuda
RUN cd /tsne-cuda && \
     mkdir -p build && cd build && \
     cmake .. -DCMAKE_CUDA_COMPILER=/usr/local/cuda-12.8/bin/nvcc && \
     make -j16 && \
     cd python && pip install .

COPY src/external/FlowCytometryTools /FlowCytometryTools
RUN cd /FlowCytometryTools && \
    pip install .

WORKDIR /workspace
