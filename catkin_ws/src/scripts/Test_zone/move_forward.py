#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
   # Starts a new node
   rospy.init_node('robot_cleaner', anonymous=True)
   velocity_publisher = rospy.Publisher('move_cmd_vel', Twist, queue_size=10)
   rospy.loginfo('voila')
   vel_msg = Twist()
   vel_msg.linear.x = 0.1
   #Since we are moving just in x-axis
   vel_msg.linear.y = 0
   vel_msg.linear.z = 0
   vel_msg.angular.x = 0
   vel_msg.angular.y = 0
   vel_msg.angular.z = 0
  
   while not rospy.is_shutdown():
  
      #Setting the current time for distance calculus
          #Force the robot to stop
      velocity_publisher.publish(vel_msg)
   
if __name__ == '__main__':
     try:
           #Testing our function
           move()
     except rospy.ROSInterruptException: pass
