FROM w251/cuda:dev-tx2-4.3_b132
RUN apt-get update
RUN apt-get install -y software-properties-common

RUN apt-get update && apt-get install -y \
    build-essential\
    curl \
    git \
    python3.6 \
    python3-pip \
    vim \
    unzip\
    sudo \
    cmake 

RUN JETSON_BOARD="TX2" \
	JETSON_JETPACK="4.3" \
	JETSON_CUDA="10.0.326" \
	JETSON_L4T="32.3.1" \
	export JETSON_BOARD \
	export JETSON_CUDA \
	export JETSON_JETPACK \
	export JETSON_L4T

RUN apt-get update && apt-get install -y \
    build-essential\
    curl \
    git \
    python3.6 \
    python3-pip \
    vim \
    unzip\
    sudo \
    cmake \
    libhdf5-dev \
    python3-numpy \
    python3-setuptools \
    libgtk2.0-dev \
    python3-wheel\
    python3-dev\
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libdc1394-22-dev \
    unzip\
    pkg-config \
    libgtk-3-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    gfortran \
    libatlas-base-dev

#OpenCV 4.3
RUN cd \
    && git clone https://github.com/opencv/opencv.git \
    && git clone https://github.com/opencv/opencv_contrib.git \
    && cd opencv \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j8 \
    && make install \
    && cd

RUN cd \   
	&& git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose \
	&& cd openpose \
        && chmod +x scripts/ubuntu/install_deps.sh \ 
	&& ./scripts/ubuntu/install_deps.sh 

RUN apt-get purge -y cmake 
RUN apt-get install -y qtbase5-dev
RUN apt-get install -y wget \
	libssl-dev
#make sure cmake is >3.12
RUN wget https://cmake.org/files/v3.17/cmake-3.17.0.tar.gz  \
    && tar xzf cmake-3.17.0.tar.gz  \
    && rm -rf cmake-3.17.0.tar.gz  \
    && cd cmake-3.17.0  \
    && ./configure --qt-gui \
    && ./bootstrap \
    && make -j`nproc` \
    && make install -j`nproc` 

RUN cd \
        && cd openpose \
        && sed -i "s|CV_LOAD_IMAGE_GRAYSCALE|cv::IMREAD_GRAYSCALE |g" examples/tests/resizeTest.cpp \
        && mkdir build \
        && cd build \
        && cmake -DBUILD_EXAMPLES=ON  -DBUILD_PYTHON=ON  -DUSE_OPENCV=ON .. \
        && make -j4 \
        && make install \
#==== python build ==== 
# don't do make install command. because it installs openpose module to python 2.7 directory
        && cd python \
        && make -j4
RUN pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11

RUN pip3 install grpcio

RUN pip3 install -U pip testresources setuptools

RUN pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v43 tensorflow
RUN pip3 install keras
RUN apt-get install -y mosquitto-clients
RUN pip3 install paho-mqtt

RUN apt-get install -y libcanberra-gtk-module libcanberra-gtk3-module


COPY Efficientnet_model_weights_NEW4_trial4.h5 /root/openpose/models/
EXPOSE 1883

