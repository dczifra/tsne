docker run \
    --rm \
    --mount type=bind,source="$(pwd)",target=/workspace \
    -it doma945/nvidia_base bash

# --gpus all