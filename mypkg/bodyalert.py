# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("bodyalert")

def cb(msg):
    bt = float(msg.data)
    if bt < 36.0:
        node.get_logger().info(f"{bt:.1f}度:体を温めてください。")
    elif 36.0 <= bt < 37.0:
        node.get_logger().info(f"{bt:.1f}度:健康です。")
    elif 37.0 <= bt:
        node.get_logger().info(f"{bt:.1f}度:病院に行きましょう。")


def main():
    node.create_subscription(String, "temperaturealerts", cb, 10)
    rclpy.spin(node)
