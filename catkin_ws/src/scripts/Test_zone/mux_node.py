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
        self.move_base = True
        self.joystick = False
        # Track the last input control
        self.last_joystick = self.joystick
        self.last_move_base = self.move_base
        # Subscribe to the control topics and set a callback for each
        rospy.Subscriber('joystick_cmd_vel', Twist, self.joystick_cb)
        rospy.Subscriber('move_cmd_vel', Twist, self.move_base_cb)

        # Wait for the mux select service
        rospy.loginfo("Waiting for mux select service...")
        rospy.wait_for_service('mux_cmd_vel/select', 60) 
        # Create a proxy for the mux select service
        mux_select = rospy.ServiceProxy('mux_cmd_vel/select', MuxSelect)
        rospy.loginfo("Connected to mux select service.")
        rospy.loginfo("Ready for input.")
        # Main loop to switch inputs if user move joystick 
        while not rospy.is_shutdown():
            if self.joystick and self.joystick != self.last_joystick:
                mux_select('joystick_cmd_vel')
            elif self.move_base and self.move_base != self.last_move_base:
                mux_select('move_cmd_vel') 
            self.last_joystick = self.joystick
            self.last_move_base = self.move_base
            r.sleep()
                
    # If the joystick is moved, get the message here
    def joystick_cb(self, msg):
        self.lock.acquire()
        self.joystick = True
        self.move_base = False
        self.lock.release()
        
    # If move_base is active, get the message here 64
    def move_base_cb(self, msg):
        self.lock.acquire()
        self.joystick = False
        self.move_base = True
        self.lock.release()

if __name__ == '__main__':
    SelectCmdVel()
    rospy.spin()
