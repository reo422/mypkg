# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("bodyalert")
pub = node.create_publisher(String, "bodyalertmessage", 10)

def cb(msg):
    bt = float(msg.data)
    btalert = String()
    if bt < 36.0:
        btalert.data = f"{bt:.1f}度:体を温めてください。"
    elif 36.0 <= bt < 37.0:
        btalert.data = f"{bt:.1f}度:健康です。"
    elif 37.0 <= bt:
        btalert.data = f"{bt:.1f}度:病院に行きましょう。"

    pub.publish(btalert)


def main():
    node.create_subscription(String, "temperaturealerts", cb, 10)
    rclpy.spin(node)
