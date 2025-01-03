# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


rclpy.init()
node = Node("talker")
pub = node.create_publisher(String, "countup", 10)
counter = 0


def cb():
    global counter

    hours = counter // 3600
    minutes = (counter % 3600)  // 60
    seconds = counter % 60
    time_str = f"{hours:01}:{minutes:02}:{seconds:02}"


    msg = String()
    msg.data = time_str
    pub.publish(msg)
    counter += 1


def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
