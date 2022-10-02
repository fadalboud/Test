// Auto-generated. Do not edit!

// (in-package mqtt_ros_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Vector3Time {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.vector = null;
      this.time = null;
    }
    else {
      if (initObj.hasOwnProperty('vector')) {
        this.vector = initObj.vector
      }
      else {
        this.vector = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = new std_msgs.msg.UInt64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Vector3Time
    // Serialize message field [vector]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.vector, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = std_msgs.msg.UInt64.serialize(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Vector3Time
    let len;
    let data = new Vector3Time(null);
    // Deserialize message field [vector]
    data.vector = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = std_msgs.msg.UInt64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mqtt_ros_bridge/Vector3Time';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'df93b39e31bd03890a20bf8ae7643eeb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    ================================================================================
    MSG: std_msgs/UInt64
    uint64 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Vector3Time(null);
    if (msg.vector !== undefined) {
      resolved.vector = geometry_msgs.msg.Vector3.Resolve(msg.vector)
    }
    else {
      resolved.vector = new geometry_msgs.msg.Vector3()
    }

    if (msg.time !== undefined) {
      resolved.time = std_msgs.msg.UInt64.Resolve(msg.time)
    }
    else {
      resolved.time = new std_msgs.msg.UInt64()
    }

    return resolved;
    }
};

module.exports = Vector3Time;
