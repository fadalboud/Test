#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist,Pose
from ar_track_alvar_msgs.msg import AlvarMarkers

#carrot = Point()
class getcarrot:
    def get_msg(self,msg):
        if len(msg.markers) ==1:
            self.carrot_x = msg.markers[0].pose.pose.position.x
            self.carrot_y = msg.markers[0].pose.pose.position.y
            self.carrot_z = msg.markers[0].pose.pose.position.z
            print(self.carrot_x)
            
    def __init__(self, Twist):
        self.carrot_x = 0
        self.carrot_y = 0
        self.carrot_z = 0
 
        #print(type(self.carrot['linear']['x']))
        rospy.init_node("carrot_navigation")
        self.marker = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, self.get_msg)
        self.move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.speed = Twist()
        self.rate = rospy.Rate(1)
            
    def run(self):
        while not rospy.is_shutdown():
            self.speed.linear.x = self.carrot_x/10
            #self.speed.angular.z = -self.carrot_x/2
            #self.speed.linear.x = 0.01
    
            #print(self.speed.linear.x)
    
            self.move.publish(self.speed)
    
            self.rate.sleep()

if __name__=='__main__':
    
    get_carrot = getcarrot(Twist)
    get_carrot.run()


