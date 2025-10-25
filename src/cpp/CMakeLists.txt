cmake_minimum_required (VERSION 3.20)
project(examples)
set (CMAKE_PROJECT_VERSION 3)
set (CMAKE_PROJECT_VERSION_MAJOR 3)
set (CMAKE_PROJECT_VERSION_MINOR 0)
set (CMAKE_PROJECT_VERSION_PATCH 2)
set (CMAKE_PROJECT_VERSION_PATH 0)
set (CMAKE_SKIP_RULE_DEPENDENCY TRUE)
set (CMAKE_EXPORT_COMPILE_COMMANDS 1)
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/Modules)
enable_language(CUDA)


# Build Number Generation
#-------------------------------------------------------------------------------
SET(BUILD_NUMBER 0)
ADD_DEFINITIONS(-DVERSION_MAJOR=${CMAKE_PROJECT_VERSION_MAJOR})
ADD_DEFINITIONS(-DVERSION_MINOR=${CMAKE_PROJECT_VERSION_MINOR})
ADD_DEFINITIONS(-DVERSION_PATCH=${CMAKE_PROJECT_VERSION_PATCH})
#-------------------------------------------------------------------------------


# CXX Configuration
#-------------------------------------------------------------------------------
set(OPT_FLAGS
    -std=c++17
    -fopenmp
    -mpopcnt
    -msse4
    -fPIC
    -m64
    -Wno-sign-compare
    -g
    -O3
    -Wall
    -Wextra
    -DFINTEGER=int
)
string(REPLACE ";" " " CXX_FLAGS_STR "${CMAKE_CXX_FLAGS} ${OPT_FLAGS}")
set(CMAKE_CXX_FLAGS "${CXX_FLAGS_STR}")
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)

#-------------------------------------------------------------------------------

# CUDA Configuration
#-------------------------------------------------------------------------------
find_package(CUDAToolkit REQUIRED)
if(NOT DEFINED CMAKE_CUDA_STANDARD)
    set(CMAKE_CUDA_STANDARD 14)
    set(CMAKE_CUDA_STANDARD_REQUIRED ON)
endif()

if(CUDAToolkit_VERSION_MAJOR EQUAL "12")
    set(CUDA_ARCH
        -gencode=arch=compute_60,code=sm_60
        -gencode=arch=compute_61,code=sm_61
        -gencode=arch=compute_70,code=sm_70
        -gencode=arch=compute_75,code=sm_75
        -gencode=arch=compute_80,code=sm_80
        -gencode=arch=compute_86,code=sm_86
        -gencode=arch=compute_87,code=sm_87
        -gencode=arch=compute_89,code=sm_89
        -gencode=arch=compute_90,code=sm_90
    )
else()
    message("CUDA version not supported" ${CUDAToolkit_VERSION_MAJOR})
    exit()
endif()


set(CUDA_OPTS
    -O3
    -g
    -Xptxas '-dlcm=cg'
    -Xcompiler '-O3'
    -Xcompiler '-fPIC'
    -Xcompiler '-fopenmp'
    -Xcompiler '-msse4'
    -Xcompiler '-m64'
    -Xcompiler '-mpopcnt'
    -Xcompiler '-g'
    -Xlinker 'muldefs'
)
string (REPLACE ";" " " NVCC_FLAGS_STR "${CUDA_ARCH} ${CUDA_OPTS}")
set(CMAKE_CUDA_FLAGS "${NVCC_FLAGS_STR}")
#-------------------------------------------------------------------------------

# OpenMP configuration
#-------------------------------------------------------------------------------
find_package(OpenMP REQUIRED)
#-------------------------------------------------------------------------------

# FAISS Configuration
#-------------------------------------------------------------------------------
find_package(FAISS REQUIRED)
if(NOT ${GPU_FAISS_FOUND})
    message("-- GPU FAISS not installed. Please install FAISS for GPU.")
endif()
include_directories(${FAISS_INCLUDE_DIR})

# Project Setup
#-------------------------------------------------------------------------------
include_directories(
    ${CUDA_INCLUDE_DIRS}
)
link_directories(
    ${CUDA_LIBRARIES}
    ${CUDA_CUBLAS_LIBRARIES}
)

add_executable(MAIN main.cpp)
target_link_libraries(MAIN PRIVATE faiss)


target_link_libraries(MAIN PRIVATE
    CUDA::cudart
    CUDA::cublas
    CUDA::cufft
    CUDA::cufftw
    CUDA::cusparse
    OpenMP::OpenMP_CXX
    pthread
    -Wl,--allow-multiple-definition
    ${FAISS_LIBRARIES}
)
