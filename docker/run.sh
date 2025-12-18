#!/bin/bash


if [ "$1" == "--ubuntu" ]; then
    OS_FLAG="ubuntu:22.04"
elif [ "$1" == "--al23" ]; then
    OS_FLAG="tsnecuda_al23"
else
    OS_FLAG="amazonlinux:2023"
fi

# CPU flag, if set, set GPU to '', else set to '--gpus all'
if [ "$2" == "--cpu" ]; then
    GPU_FLAG=""
else
    GPU_FLAG="--gpus all"
fi

docker run \
    --rm $GPU_FLAG \
    --runtime=nvidia \
    --mount type=bind,source="$(pwd)",target=/workspace \
    -it "doma945/nvidia_$OS_FLAG" bash

# --gpus all