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
    alert.data = f"{bt:.1f}"
    pub.publish(alert)

def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
