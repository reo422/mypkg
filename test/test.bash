#!/bin/bash
# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 70 ros2 launch mypkg time.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep '10 seconds have passed!'
cat /tmp/mypkg.log | grep '1 minute has passed!'
