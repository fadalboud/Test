// Auto-generated. Do not edit!

// (in-package mqtt_ros_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Vector3Time = require('./Vector3Time.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ImuPackage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.time = null;
      this.linear_acceleration = null;
      this.angular_velocity = null;
    }
    else {
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = new std_msgs.msg.UInt64();
      }
      if (initObj.hasOwnProperty('linear_acceleration')) {
        this.linear_acceleration = initObj.linear_acceleration
      }
      else {
        this.linear_acceleration = [];
      }
      if (initObj.hasOwnProperty('angular_velocity')) {
        this.angular_velocity = initObj.angular_velocity
      }
      else {
        this.angular_velocity = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImuPackage
    // Serialize message field [time]
    bufferOffset = std_msgs.msg.UInt64.serialize(obj.time, buffer, bufferOffset);
    // Serialize message field [linear_acceleration]
    // Serialize the length for message field [linear_acceleration]
    bufferOffset = _serializer.uint32(obj.linear_acceleration.length, buffer, bufferOffset);
    obj.linear_acceleration.forEach((val) => {
      bufferOffset = Vector3Time.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [angular_velocity]
    // Serialize the length for message field [angular_velocity]
    bufferOffset = _serializer.uint32(obj.angular_velocity.length, buffer, bufferOffset);
    obj.angular_velocity.forEach((val) => {
      bufferOffset = Vector3Time.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImuPackage
    let len;
    let data = new ImuPackage(null);
    // Deserialize message field [time]
    data.time = std_msgs.msg.UInt64.deserialize(buffer, bufferOffset);
    // Deserialize message field [linear_acceleration]
    // Deserialize array length for message field [linear_acceleration]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.linear_acceleration = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.linear_acceleration[i] = Vector3Time.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [angular_velocity]
    // Deserialize array length for message field [angular_velocity]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.angular_velocity = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.angular_velocity[i] = Vector3Time.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 32 * object.linear_acceleration.length;
    length += 32 * object.angular_velocity.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mqtt_ros_bridge/ImuPackage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '87d2de22057b308bbb4c314993ad9d86';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/UInt64 time
    mqtt_ros_bridge/Vector3Time[] linear_acceleration
    mqtt_ros_bridge/Vector3Time[] angular_velocity
    ================================================================================
    MSG: std_msgs/UInt64
    uint64 data
    ================================================================================
    MSG: mqtt_ros_bridge/Vector3Time
    geometry_msgs/Vector3 vector
    std_msgs/UInt64 time
    
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImuPackage(null);
    if (msg.time !== undefined) {
      resolved.time = std_msgs.msg.UInt64.Resolve(msg.time)
    }
    else {
      resolved.time = new std_msgs.msg.UInt64()
    }

    if (msg.linear_acceleration !== undefined) {
      resolved.linear_acceleration = new Array(msg.linear_acceleration.length);
      for (let i = 0; i < resolved.linear_acceleration.length; ++i) {
        resolved.linear_acceleration[i] = Vector3Time.Resolve(msg.linear_acceleration[i]);
      }
    }
    else {
      resolved.linear_acceleration = []
    }

    if (msg.angular_velocity !== undefined) {
      resolved.angular_velocity = new Array(msg.angular_velocity.length);
      for (let i = 0; i < resolved.angular_velocity.length; ++i) {
        resolved.angular_velocity[i] = Vector3Time.Resolve(msg.angular_velocity[i]);
      }
    }
    else {
      resolved.angular_velocity = []
    }

    return resolved;
    }
};

module.exports = ImuPackage;
