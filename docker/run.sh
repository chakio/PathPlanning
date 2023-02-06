#!/bin/bash

cd `dirname $0`

xhost +local:user
nvidia-docker &> /dev/null
if [ $? -ne 0 ]; then
    echo $TAG
    echo "=============================" 
    echo "=nvidia docker not installed="
    echo "============================="
else
    echo "=========================" 
    echo "=nvidia docker installed="
    echo "========================="
    TAG="path_planning/${USER}"
    docker run -it \
    --privileged \
    --runtime=nvidia \
    --env=DISPLAY=$DISPLAY \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env="QT_X11_NO_MITSHM=1" \
    --rm \
    -v "/$(pwd)/global_ros_setting.sh:/ros_setting.sh" \
    -v "/$(pwd)/../workspace:/workspace/" \
    -v /etc/group:/etc/group:ro \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/localtime:/etc/localtime:ro \
    -v /media:/media \
    -v /dev:/dev \
    --net host \
    ${TAG}
fi
