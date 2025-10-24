FROM nvidia/cuda:11.3.1-devel-ubuntu20.04

# === Install ap packages ===
RUN apt -qq update && \
    DEBIAN_FRONTEND=noninteractive apt -qq install build-essential libopenblas-dev libgtest-dev libgflags-dev \
    wget g++ git -y \
    && rm -rf /var/lib/apt/lists/*

# === Install CMake 3.20.0 ===
RUN wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0-linux-x86_64.sh -O /tmp/cmake.sh && \
    bash /tmp/cmake.sh --skip-license --prefix=/usr/local && \
    rm /tmp/cmake.sh
RUN apt install  -y

# === Install miniconda ===
RUN mkdir -p /opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O /opt/conda/miniconda.sh \
 && bash /opt/conda/miniconda.sh -b -p /opt/miniconda
ENV PATH="/opt/miniconda/bin:$PATH"
ENV CMAKE_PREFIX_PATH=/opt/miniconda

# === Install FAISS ===
RUN conda init bash
RUN conda install python=3.8
RUN conda install -c pytorch -c nvidia faiss-gpu=1.6.5

# === Install pip packages for tests ===
RUN pip install scikit-learn torchvision matplotlib pandas tqdm seaborn

# === Install CannyLab's t-SNE ===
# COPY tsne-cuda /workspace/tsne-cuda
# RUN cd /workspace/tsne-cuda && \
#     mkdir build && cd build && \
#     cmake .. && make -j16 && \
#     cd python && pip install .

WORKDIR /workspace