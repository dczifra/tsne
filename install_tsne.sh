# === Install faiss ===
#rm -rf tsne-cuda/build
mkdir src/external/tsne-cuda/build
cd src/external/tsne-cuda/build
cmake ..
make -j16
cd python
pip install -e .
cd ../../../FlowCytometryTools
pip install -e .