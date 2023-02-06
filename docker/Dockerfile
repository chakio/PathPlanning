# This is an auto generated Dockerfile for ros:ros-core
# generated from docker_images/create_ros_core_image.Dockerfile.em
FROM ubuntu:20.04
ARG USER=initial
ARG GROUP=initial
ARG UID=1000
ARG GID=${UID}
ARG SHELL=/bin/bash
ARG workspace=/
#FROM $base_image
RUN echo base image: ${base_image}

#######################################################################
##                            Speeding up                            ##
#######################################################################
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

#######################################################################
##                      install common packages                      ##
#######################################################################
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
   pkg-config \
   apt-utils \
   wget \
   git \
   build-essential \ 
   net-tools \
   gedit \
   terminator \
   nautilus \
   software-properties-common \
   apt-transport-https \
   libopencv-dev \
   ffmpeg \
   x264 \
   libx264-dev \
   zip \
   unzip \
   usbutils \
   sudo \
   python3-pip \
   libusb-1.0-0-dev

#######################################################################
##                           install font                            ##
#######################################################################
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections 
RUN apt-get install -y ttf-mscorefonts-installer \
   msttcorefonts -qq

RUN python3 -m pip install --upgrade pip
RUN apt-get install  -y python3-ruamel.yaml

#######################################################################
##                       install nvidia docker                       ##
#######################################################################
RUN apt-get install -y --no-install-recommends \
    libxau-dev \
    libxdmcp-dev \
    libxcb1-dev \
    libxext-dev \
    libx11-dev \
    mesa-utils \
    x11-apps

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

# Required for non-glvnd setups.
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}:/usr/local/nvidia/lib:/usr/local/nvidia/lib64


#######################################################################
##                            install ros                            ##
#######################################################################

RUN apt-get install -q -y \
    dirmngr \
    gnupg2 \
    lsb-release \
    curl



RUN apt-get install -y \
    python3-pil \
    python3-pil.imagetk \
    build-essential 
#######################################################################
##                   install additional packages                     ##
#######################################################################

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8



#######################################################################
##                   install additional packages                     ##
#######################################################################
RUN apt-get install -y \
    python3-tk \
    xdg-utils \
    chromium-browser
#######################################################################
##                     install python packages                       ##
#######################################################################
# install opencv
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pylint
RUN pip3 install autopep8
RUN pip3 install scipy
RUN pip3 install matplotlib==3.5.1
RUN pip3 install Pillow
RUN pip3 install opencv-python
RUN pip3 install ffmpeg-python
RUN pip3 install pytz
RUN pip3 install numpy==1.23.1
RUN pip3 install pyrr
#######################################################################
##                            clean up                               ##
#######################################################################

RUN rm -rf /var/lib/apt/lists/*

#######################################################################
##                         make sudoer user                          ##
#######################################################################
RUN echo "User!!! - " $USER
ARG USER
RUN echo $USER
ARG USER_ID
RUN groupadd -g 1000 developer && \
    useradd  -g      developer -G sudo -m -u $USER_ID -s /bin/bash ${USER} && \
    echo "${USER}:${USER}" | chpasswd

RUN echo "Defaults visiblepw" >> /etc/sudoers
RUN echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#######################################################################
##                    make user accessible to usb                    ##
#######################################################################
RUN adduser ${USER} dialout

# USER root
USER ${USER}
RUN echo "export PS1='\[\e[1;31;40m\]Path Plan\[\e[0m\] \u:\w\$ '">> ~/.bashrc
RUN echo "source /ros_setting.sh">> ~/.bashrc

WORKDIR ${workspace}
