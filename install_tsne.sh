# === Install faiss ===
mkdir -p src/external/tsne-cuda/build
cd src/external/tsne-cuda/build
cmake ..
make -j16
cd python
pip install -e .