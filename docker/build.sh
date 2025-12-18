if [ "$1" == "--ubuntu" ]; then
    OS_FLAG="ubuntu:22.04"
elif [ "$1" == "--al23" ]; then
    OS_FLAG="tsnecuda_al23"
else
    OS_FLAG="amazonlinux:2023"
fi

rm -rf src/external/tsne-cuda/build
docker build . -t "doma945/nvidia_$OS_FLAG" -f "docker/$OS_FLAG/Dockerfile"