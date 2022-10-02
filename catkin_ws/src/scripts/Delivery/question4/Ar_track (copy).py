#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist,Point
from ar_track_alvar_msgs.msg import AlvarMarkers

carrot = Point()

def getcarrot(msg):
    global carrot
    if len(msg.markers) ==1:
        carrot = msg.markers[0].pose.pose.position
    else:
        carrot = Point()
        
rospy.init_node("carrot_navigation")

marker = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, getcarrot)
move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

r = rospy.Rate(1)

speed = Twist()
while not rospy.is_shutdown:
    speed.linear.x = -carrot.y/10
    speed.angular.z = -carrot.x/2
    
    print(speed)
    
    move.publish(speed)
    
    r.sleep()
