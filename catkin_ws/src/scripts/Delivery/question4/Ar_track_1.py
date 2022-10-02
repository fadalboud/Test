#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist,Pose
from ar_track_alvar_msgs.msg import AlvarMarkers
from math import sqrt, atan2, sin, cos, pi
from tf.transformations import euler_from_quaternion
from tf2_msgs.msg import TFMessage

max_speed = 0.35
trigger_distance = 0.5
turn_multiplier = 1
accel = 0.005

class getcarrot:
    def callback(self, msg):
        # callback to pick up data from the robot transform
        pose = msg.transforms[0].transform.translation
        self.x = pose.x
        self.y = pose.y
        rot = msg.transforms[0].transform.rotation
        (roll, pitch, self.theta) = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
        
    def get_msg(self, msg):
        if len(msg.markers) ==1:
            self.carrot_x = msg.markers[0].pose.pose.position.x
            self.carrot_y = msg.markers[0].pose.pose.position.y
            self.carrot_z = msg.markers[0].pose.pose.position.z
            #rot = msg.markers[0].pose.pose.orientation
        #(roll, pitch, self.carrot_theta) = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
            #print(self.carrot)
            
    def __init__(self, Twist):
        self.x = 0.0  # Current robot position x
        self.y = 0.0  # Current robot position y
        self.theta = 0.0  # Current robot angle
        self.carrot_x = 0
        self.carrot_y = 0
        self.carrot_z = 0
        self.carrot_theta = 0
        self.longi_speed = 0.0
 
        #print(type(self.carrot['linear']['x']))
        rospy.init_node("carrot_navigation")
        sub = rospy.Subscriber("/tf", TFMessage, callback=self.callback)
        self.marker = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, self.get_msg)
        self.move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.speed = Twist()
        self.rate = rospy.Rate(1)
            
    def run(self):
        while not rospy.is_shutdown():
            # Calculate angle
                    dist_x = self.carrot_x
                    dist_y = self.carrot_y
                    angle_to_point = atan2(dist_y, dist_x)
                    turn = atan2(sin(angle_to_point), cos(angle_to_point))

                    # Calculate longitudinal speed
                    angle_robot_pt_fwd = turn
                    target_speed = max(0.0, max_speed - abs(angle_robot_pt_fwd))
                    if self.longi_speed < target_speed - 0.01:
                        self.longi_speed += accel
                    elif self.longi_speed > target_speed + 0.01:
                        self.longi_speed -= accel

                    # Create command
                    self.speed.angular.z = turn * turn_multiplier
                    self.speed.linear.x = self.longi_speed
    
                    self.move.publish(self.speed)
    
                    self.rate.sleep()

if __name__=='__main__':
    
    get_carrot = getcarrot(Twist)
    get_carrot.run()


