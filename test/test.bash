#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 launch mypkg temp.launch.py &

timeout 10 ros2 topic echo /bodyalertmessage > /tmp/mypkg.log

cat /tmp/mypkg.log | grep '体を温めてください。'
cat /tmp/mypkg.log | grep '健康です。'
cat /tmp/mypkg.log | grep '病院に行きましょう。'
