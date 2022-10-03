# Test Report
This git repository is a report for the iFollow Test.
## 1 Test Environment 
In this Test, ROS 1 Noetic was used under Ubuntu 20.04. 
To install ROS 1 Noetic under 20.04, please refer to : 
[Ubuntu install ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)

For the simulation, Turtlebot3 burger model was used. Please refer to : 
[Turtlebot3 Noetic](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/).

To install dependent ROS packages, run: 
``` 
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

To install Turtlebot3 packages, run:
```
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
```

You can download Turtlebot3 simulations package from source [Here](https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git).

First, launch a turtlebot3 burger model in empty world by executing the following: 
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

![Turtlebot3 burger empty world](https://imgur.com/a/Jb0FIhY)

Then launch the navigation from the navigation packages: 
```
roslaunch turtlebot3_nav navigation.launch 
```

This launch file uses the amcl and move_base links to properly navigate the turtlebot in the map. The map was obtained using the lidar of the turtlebot. All these files can be found in folder "nav_robot".

![Turtlebot3 navigation](https://imgur.com/iM9SYOK)

To run the teleoperation using the keyboard, use:
```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

To send navigation goals to the navigations goal stacks, you can use the 2D Nav Goal in Rviz or run:
```
```

## 2 Command Multiplexer 

## 3 Remote Teleoperation 

## 4 Ar Tags Track 

## Notes 


