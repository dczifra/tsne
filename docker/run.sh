#!/bin/bash

# CPU flag, if set, set GPU to '', else set to '--gpus all'
if [ "$1" == "--cpu" ]; then
    GPU_FLAG=""
else
    GPU_FLAG="--gpus all"
fi

docker run \
    --rm $GPU_FLAG \
    --mount type=bind,source="$(pwd)",target=/workspace \
    -it doma945/nvidia_base bash

# --gpus all