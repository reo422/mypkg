#!/bin/bash
# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 30 ros2 launch mypkg temp.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep '度。'
cat /tmp/mypkg.log | grep '体を温めてください。'
cat /tmp/mypkg.log | grep '正常です。'
cat /tmp/mypkg.log | grep '安静が必要です。'
cat /tmp/mypkg.log | grep 'すぐ医師に相談してください。'
