; Auto-generated. Do not edit!


(cl:in-package mqtt_ros_bridge-msg)


;//! \htmlinclude Vector3Time.msg.html

(cl:defclass <Vector3Time> (roslisp-msg-protocol:ros-message)
  ((vector
    :reader vector
    :initarg :vector
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (time
    :reader time
    :initarg :time
    :type std_msgs-msg:UInt64
    :initform (cl:make-instance 'std_msgs-msg:UInt64)))
)

(cl:defclass Vector3Time (<Vector3Time>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Vector3Time>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Vector3Time)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mqtt_ros_bridge-msg:<Vector3Time> is deprecated: use mqtt_ros_bridge-msg:Vector3Time instead.")))

(cl:ensure-generic-function 'vector-val :lambda-list '(m))
(cl:defmethod vector-val ((m <Vector3Time>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mqtt_ros_bridge-msg:vector-val is deprecated.  Use mqtt_ros_bridge-msg:vector instead.")
  (vector m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <Vector3Time>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mqtt_ros_bridge-msg:time-val is deprecated.  Use mqtt_ros_bridge-msg:time instead.")
  (time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Vector3Time>) ostream)
  "Serializes a message object of type '<Vector3Time>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vector) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'time) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Vector3Time>) istream)
  "Deserializes a message object of type '<Vector3Time>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vector) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'time) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Vector3Time>)))
  "Returns string type for a message object of type '<Vector3Time>"
  "mqtt_ros_bridge/Vector3Time")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Vector3Time)))
  "Returns string type for a message object of type 'Vector3Time"
  "mqtt_ros_bridge/Vector3Time")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Vector3Time>)))
  "Returns md5sum for a message object of type '<Vector3Time>"
  "df93b39e31bd03890a20bf8ae7643eeb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Vector3Time)))
  "Returns md5sum for a message object of type 'Vector3Time"
  "df93b39e31bd03890a20bf8ae7643eeb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Vector3Time>)))
  "Returns full string definition for message of type '<Vector3Time>"
  (cl:format cl:nil "geometry_msgs/Vector3 vector~%std_msgs/UInt64 time~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: std_msgs/UInt64~%uint64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Vector3Time)))
  "Returns full string definition for message of type 'Vector3Time"
  (cl:format cl:nil "geometry_msgs/Vector3 vector~%std_msgs/UInt64 time~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: std_msgs/UInt64~%uint64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Vector3Time>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vector))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'time))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Vector3Time>))
  "Converts a ROS message object to a list"
  (cl:list 'Vector3Time
    (cl:cons ':vector (vector msg))
    (cl:cons ':time (time msg))
))
