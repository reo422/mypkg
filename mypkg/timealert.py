# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("timealert")

def cb(msg):
    information = f"時間通知: {msg.data}"
    node.get_logger().info(information)

def main():
    node.create_subscription(String, "timenotifications", cb, 10)
    rclpy.spin(node)
