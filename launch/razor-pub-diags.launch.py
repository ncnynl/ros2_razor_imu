# Copyright (c) 2019, Andreas Klintberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchIntrospector, LaunchService
from launch_ros import actions, get_default_launch_description


def generate_launch_description():
    """
    Launch file for visualizing and diagnosing Razor IMU data
    """
    config_path = os.path.join(get_package_share_directory("razor_imu_9dof"), "config",
                               "razor_diags.yaml")

    # display_3D_visualization_node = actions.Node(
    #     package='razor_imu_9dof', node_executable='display_3D_visualization_node', output='screen')

    # diagnostic_aggregator = actions.Node(
    #     package='diagnostic_aggregator', node_executable='aggregator_node', output='screen',
    #     parameter=[config_path])

    # rqt_robot_monitor = actions.Node(
    #     package='rqt_robot_monitor', node_executable='rqt_robot_monitor', output='screen')

    # return LaunchDescription(
    #     [display_3D_visualization_node, diagnostic_aggregator, rqt_robot_monitor])


# def main(argv):
#     ld = generate_launch_description()

#     print('Starting introspection of launch description...')
#     print('')

#     print(LaunchIntrospector().format_launch_description(ld))

#     print('')
#     print('Starting launch of launch description...')
#     print('')

#     ls = LaunchService()
#     ls.include_launch_description(get_default_launch_description())
#     ls.include_launch_description(ld)
#     return ls.run()


# if __name__ == '__main__':
#     main(sys.argv)
