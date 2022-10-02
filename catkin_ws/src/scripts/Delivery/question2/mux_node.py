#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from topic_tools.srv import MuxSelect
import _thread as thread

class SelectCmdVel:
    def __init__(self):
        rospy.init_node("select_cmd_vel")
        # The rate at which to update the input selection
        rate = rospy.get_param('~rate', 5)
        # Convert to a ROS rate
        r = rospy.Rate(rate)
        # Get a lock for updating the selected cmd_vel input
        self.lock = thread.allocate_lock()
        # Set the default input control
        self.cmd_local = True
        self.cmd_web = False
        # Track the last input control
        self.last_cmd_web = self.cmd_web
        self.last_cmd_local = self.cmd_local
        # Subscribe to the control topics and set a callback for each
        rospy.Subscriber('cmd_web', Twist, self.cmd_web_cb)
        rospy.Subscriber('cmd_local', Twist, self.cmd_local_cb)

        # Wait for the mux select service
        rospy.loginfo("Waiting for mux select service...")
        rospy.wait_for_service('mux_cmd_vel/select', 60) 
        # Create a proxy for the mux select service
        mux_select = rospy.ServiceProxy('mux_cmd_vel/select', MuxSelect)
        rospy.loginfo("Connected to mux select service.")
        rospy.loginfo("Ready for input.")
        # Main loop to switch inputs if user move cmd_web 
        while not rospy.is_shutdown():
            if self.cmd_web and self.cmd_web != self.last_cmd_web:
                mux_select('cmd_web')
            elif self.cmd_local and self.cmd_local != self.last_cmd_local:
                mux_select('cmd_local') 
            self.last_cmd_web = self.cmd_web
            self.last_cmd_local = self.cmd_local
            r.sleep()
                
    # If the cmd_web is on, get the message here
    def cmd_web_cb(self, msg):
        self.lock.acquire()
        self.cmd_web = True
        self.cmd_local = False
        self.lock.release()
        
    # If cmd_local is active, get the message here 64
    def cmd_local_cb(self, msg):
        self.lock.acquire()
        self.cmd_web = False
        self.cmd_local = True
        self.lock.release()

if __name__ == '__main__':
    SelectCmdVel()
    rospy.spin()
