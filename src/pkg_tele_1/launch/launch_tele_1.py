from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pkg_tele_1',
            executable='node_keyboard',
            name='node_keyboard'
        ),
        Node(
            package='pkg_tele_1',
            executable='node_move',
            name='node_move'
        )
    ])
