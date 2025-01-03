#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 63 ros2 launch mypkg talk_listen.launch.py | tee - /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '0:01:03'
