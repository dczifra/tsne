FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# === Install ap packages ===
RUN apt -qq update && \
    DEBIAN_FRONTEND=noninteractive apt -qq install build-essential libopenblas-dev libgtest-dev libgflags-dev \
    wget g++ git -y \
    && rm -rf /var/lib/apt/lists/*

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
RUN conda install -c pytorch -c nvidia faiss-gpu=1.9.0


# === Install pip packages for tests ===
RUN conda install scikit-learn torchvision matplotlib pandas tqdm seaborn memory_profiler

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