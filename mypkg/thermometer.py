# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

rclpy.init()
node = Node("temperaturepublisher")
pub = node.create_publisher(String, "temperaturealerts", 10)


def cb():
    bt = random.uniform(35.5, 42.0)
    alert = String()

    if bt < 36.0: 
        alert.data = f"{bt:.2f}度。体を温めてください。"
    elif 36.0 <= bt < 37.0:
        alert.data = f"{bt:.2f}度。正常です。"
    elif 37.0 <= bt < 38.0:
        alert.data = f"{bt:.2f}度。安静が必要です。"
    else:
        alert.data = f"{bt:.2f}度。すぐ医師に相談してください。"
 
    pub.publish(alert)

def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
