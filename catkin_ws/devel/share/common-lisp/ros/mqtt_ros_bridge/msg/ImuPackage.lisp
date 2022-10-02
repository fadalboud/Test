; Auto-generated. Do not edit!


(cl:in-package mqtt_ros_bridge-msg)


;//! \htmlinclude ImuPackage.msg.html

(cl:defclass <ImuPackage> (roslisp-msg-protocol:ros-message)
  ((time
    :reader time
    :initarg :time
    :type std_msgs-msg:UInt64
    :initform (cl:make-instance 'std_msgs-msg:UInt64))
   (linear_acceleration
    :reader linear_acceleration
    :initarg :linear_acceleration
    :type (cl:vector mqtt_ros_bridge-msg:Vector3Time)
   :initform (cl:make-array 0 :element-type 'mqtt_ros_bridge-msg:Vector3Time :initial-element (cl:make-instance 'mqtt_ros_bridge-msg:Vector3Time)))
   (angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type (cl:vector mqtt_ros_bridge-msg:Vector3Time)
   :initform (cl:make-array 0 :element-type 'mqtt_ros_bridge-msg:Vector3Time :initial-element (cl:make-instance 'mqtt_ros_bridge-msg:Vector3Time))))
)

(cl:defclass ImuPackage (<ImuPackage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImuPackage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImuPackage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mqtt_ros_bridge-msg:<ImuPackage> is deprecated: use mqtt_ros_bridge-msg:ImuPackage instead.")))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <ImuPackage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mqtt_ros_bridge-msg:time-val is deprecated.  Use mqtt_ros_bridge-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'linear_acceleration-val :lambda-list '(m))
(cl:defmethod linear_acceleration-val ((m <ImuPackage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mqtt_ros_bridge-msg:linear_acceleration-val is deprecated.  Use mqtt_ros_bridge-msg:linear_acceleration instead.")
  (linear_acceleration m))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <ImuPackage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mqtt_ros_bridge-msg:angular_velocity-val is deprecated.  Use mqtt_ros_bridge-msg:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImuPackage>) ostream)
  "Serializes a message object of type '<ImuPackage>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'time) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'linear_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'linear_acceleration))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'angular_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'angular_velocity))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImuPackage>) istream)
  "Deserializes a message object of type '<ImuPackage>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'time) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'linear_acceleration) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'linear_acceleration)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'mqtt_ros_bridge-msg:Vector3Time))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'angular_velocity) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'angular_velocity)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'mqtt_ros_bridge-msg:Vector3Time))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImuPackage>)))
  "Returns string type for a message object of type '<ImuPackage>"
  "mqtt_ros_bridge/ImuPackage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImuPackage)))
  "Returns string type for a message object of type 'ImuPackage"
  "mqtt_ros_bridge/ImuPackage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImuPackage>)))
  "Returns md5sum for a message object of type '<ImuPackage>"
  "87d2de22057b308bbb4c314993ad9d86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImuPackage)))
  "Returns md5sum for a message object of type 'ImuPackage"
  "87d2de22057b308bbb4c314993ad9d86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImuPackage>)))
  "Returns full string definition for message of type '<ImuPackage>"
  (cl:format cl:nil "std_msgs/UInt64 time~%mqtt_ros_bridge/Vector3Time[] linear_acceleration~%mqtt_ros_bridge/Vector3Time[] angular_velocity~%================================================================================~%MSG: std_msgs/UInt64~%uint64 data~%================================================================================~%MSG: mqtt_ros_bridge/Vector3Time~%geometry_msgs/Vector3 vector~%std_msgs/UInt64 time~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImuPackage)))
  "Returns full string definition for message of type 'ImuPackage"
  (cl:format cl:nil "std_msgs/UInt64 time~%mqtt_ros_bridge/Vector3Time[] linear_acceleration~%mqtt_ros_bridge/Vector3Time[] angular_velocity~%================================================================================~%MSG: std_msgs/UInt64~%uint64 data~%================================================================================~%MSG: mqtt_ros_bridge/Vector3Time~%geometry_msgs/Vector3 vector~%std_msgs/UInt64 time~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImuPackage>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'time))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'linear_acceleration) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'angular_velocity) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImuPackage>))
  "Converts a ROS message object to a list"
  (cl:list 'ImuPackage
    (cl:cons ':time (time msg))
    (cl:cons ':linear_acceleration (linear_acceleration msg))
    (cl:cons ':angular_velocity (angular_velocity msg))
))
