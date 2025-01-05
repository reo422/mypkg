# SPDX-FileCopyrightText: 2024 Reo Isaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


rclpy.init()
node = Node("timepublisher")
pub = node.create_publisher(String, "timenotifications", 10)
counter = 0


def cb():
    global counter

    if counter == 10:
        alert = String()
        alert.data = "10秒経過しました! システムは正常に動いてます。"
        pub.publish(alert)

    if counter == 60:
        secondalert = String()
        secondalert.data = "1分が経過しました!システムはまだ実行中です。"
        pub.publish(secondalert)

    counter += 1


def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
