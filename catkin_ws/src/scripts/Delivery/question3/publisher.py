#!/usr/bin/env python

from __future__ import print_function
from pynput.keyboard import Key, Listener

import random
import time
import json

from paho.mqtt import client as mqtt_client

import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

WAFFLE_MAX_LIN_VEL = 0.26
WAFFLE_MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

msg ="""
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
        self.client = connect_mqtt()
        self.client.loop_start()

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
        max_lin_vel = BURGER_MAX_LIN_VEL

        vel = self.constrain(vel, -max_lin_vel, max_lin_vel)
        return vel

    def checkAngularLimitVelocity(self, vel):
        max_ang_vel = BURGER_MAX_ANG_VEL

        vel = self.constrain(vel, -max_ang_vel, max_ang_vel)
        return vel

    def move(self):
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
                
            cmd_vel = self.prepare_json(self.target_linear_vel, self.target_angular_vel)
            self.publish(self.client, cmd_vel)

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
    
    def publish(self, client, cmd):
        #msg_count = 0
        time.sleep(1)
        #msg = f"messages: {msg_count}"
        message = cmd.encode()
        print(message)
        result = client.publish(topic, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
            #msg_count = msg
        
    def prepare_json(self, target_linear_vel, target_angular_vel):
        cmd_vel = { 
             "linear_x": target_linear_vel ,
             "linear_y": 0 ,
             "linear_z": 0 ,
             "angular_x": 0 ,
             "angular_y": 0 ,
             "angular_z": target_angular_vel
        }
        cmd_vel = json.dumps({"cmd_vel":cmd_vel})
        return cmd_vel
            
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client




def run():
    Teleop()
    
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    run()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
