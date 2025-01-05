# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("alert")

def cb(msg):
    node.get_logger().info(f"{msg.data}")

def main():
    node.create_subscription(String, "timenotifications", cb, 10)
    rclpy.spin(node)
