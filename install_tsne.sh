# === Install faiss ===
#rm -rf tsne-cuda/build
mkdir tsne-cuda/build
cd tsne-cuda/build
cmake ..
make -j16
cd python
pip install -e .