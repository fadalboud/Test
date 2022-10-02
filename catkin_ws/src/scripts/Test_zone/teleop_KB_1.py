#!/usr/bin/env python

# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
from pynput.keyboard import Key, Listener

import rospy
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios
from geometry_msgs.msg import Twist

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

WAFFLE_MAX_LIN_VEL = 0.26
WAFFLE_MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

msg = """
Control Your TurtleBot3!
---------------------------
Moving around:
        w
   a    s    d
w/s : linear movement (Burger : ~ 0.22, Waffle and Waffle Pi : ~ 0.26)
a/d : angular movement (Burger : ~ 2.84, Waffle and Waffle Pi : ~ 1.82)
stop when key released
ESC to quit
"""

e = """
Communications Failed
"""

class Teleop:
    def __init__(self):
        print(msg)
        self.keys = set()
        self.status = 0
        self.target_linear_vel   = 0.0
        self.target_angular_vel  = 0.0

        with Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()

    def vels(self, target_linear_vel, target_angular_vel):
        return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel,target_angular_vel)

    def constrain(self, input, low, high):
        if input < low:
            input = low
        elif input > high:
            input = high
        else:
            input = input

        return input

    def checkLinearLimitVelocity(self, vel):
        if turtlebot3_model in ["waffle", "waffle_pi"]:
            max_lin_vel = WAFFLE_MAX_LIN_VEL
        else:
            max_lin_vel = BURGER_MAX_LIN_VEL

        vel = self.constrain(vel, -max_lin_vel, max_lin_vel)
        return vel

    def checkAngularLimitVelocity(self, vel):
        if turtlebot3_model in ["waffle", "waffle_pi"]:
            max_ang_vel = WAFFLE_MAX_ANG_VEL
        else:
            max_ang_vel = BURGER_MAX_ANG_VEL

        vel = self.constrain(vel, -max_ang_vel, max_ang_vel)
        return vel

    def move(self):
        global pub
        try:
            keys = ''.join(self.keys)
            if keys.find('w') == -1 and keys.find('s') == -1 :
                self.target_linear_vel = 0.0
            else :
                sign = 1 if keys.find('w') > keys.find('s') else -1
                self.target_linear_vel = self.checkLinearLimitVelocity(self.target_linear_vel + sign * LIN_VEL_STEP_SIZE)

            if keys.find('a') == -1 and keys.find('d') == -1 :
                self.target_angular_vel = 0.0
            else :
                sign = 1 if keys.find('a') > keys.find('d') else -1
                self.target_angular_vel = self.checkAngularLimitVelocity(self.target_angular_vel + sign * ANG_VEL_STEP_SIZE)

            self.status += 1
            print(self.vels(self.target_linear_vel, self.target_angular_vel))

            if self.status == 100 :
                print(msg)
                self.status = 0
        
            twist = Twist()
            twist.linear.x = self.target_linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = self.target_angular_vel
            pub.publish(twist)

        except Exception as err:
            print(e)
            print(err)


    def on_press(self, key):
        # to remove input buffer
        if os.name == 'nt':
            msvcrt.getch()
        else:
            tty.setraw(sys.stdin.fileno())
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

        if key == Key.esc:
            return False

        if not hasattr(key, 'char'):
            return True

        key = key.char
        if key not in 'wasd':
            return True

        if key == 'w' and 's' in self.keys:
            self.keys.remove('s')
        if key == 'a' and 'd' in self.keys:
            self.keys.remove('d')
        if key == 's' and 'w' in self.keys:
            self.keys.remove('w')
        if key == 'd' and 'a' in self.keys:
            self.keys.remove('a')
        
        self.keys.add(key)
        self.move()

    def on_release(self, key):
        if not hasattr(key, 'char'):
            return True

        key = key.char
        if key in self.keys:
            self.keys.remove(key)
            self.move()

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtle_teleop')
    turtlebot3_model = rospy.get_param("model", "burger")
    topic_type = rospy.get_param("topic_type", "turtlebot")

    if topic_type == 'turtlebot':
        topic_name = 'cmd_vel'
    else:
        topic_name = 'turtle1/cmd_vel'
    pub = rospy.Publisher('joystick_cmd_vel', Twist, queue_size=10)

    Teleop()

    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
