FROM amazonlinux:2023

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

# === Install NVIDIA CUDA runtime and build environment ===
RUN dnf install 'dnf-command(config-manager)' -y
RUN dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/amzn2023/x86_64/cuda-amzn2023.repo
RUN dnf clean expire-cache
 
RUN dnf module enable -y nvidia-driver:open-dkms
RUN dnf install -y nvidia-open
RUN dnf install -y nvidia-xconfig


RUN if arch | grep -q x86; then ARCH=x86_64; else ARCH=sbsa; fi && \
    dnf install -y dnf-plugins-core && \
    dnf config-manager --add-repo \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel9/$ARCH/cuda-rhel9.repo

# Lock cuda to version 12.4
RUN dnf install -y cuda-toolkit-12-4


ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

# === Install CannyLab's t-SNE ===
COPY src/external/tsne-cuda /tsne-cuda
RUN cd /tsne-cuda && \
     mkdir -p build && cd build && \
     cmake .. && make -j16 && \
     cd python && pip install .

COPY src/external/FlowCytometryTools /FlowCytometryTools
RUN cd /FlowCytometryTools && \
    pip install .

WORKDIR /workspace
