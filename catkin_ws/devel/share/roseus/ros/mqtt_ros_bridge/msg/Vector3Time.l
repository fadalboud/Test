;; Auto-generated. Do not edit!


(when (boundp 'mqtt_ros_bridge::Vector3Time)
  (if (not (find-package "MQTT_ROS_BRIDGE"))
    (make-package "MQTT_ROS_BRIDGE"))
  (shadow 'Vector3Time (find-package "MQTT_ROS_BRIDGE")))
(unless (find-package "MQTT_ROS_BRIDGE::VECTOR3TIME")
  (make-package "MQTT_ROS_BRIDGE::VECTOR3TIME"))

(in-package "ROS")
;;//! \htmlinclude Vector3Time.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass mqtt_ros_bridge::Vector3Time
  :super ros::object
  :slots (_vector _time ))

(defmethod mqtt_ros_bridge::Vector3Time
  (:init
   (&key
    ((:vector __vector) (instance geometry_msgs::Vector3 :init))
    ((:time __time) (instance std_msgs::UInt64 :init))
    )
   (send-super :init)
   (setq _vector __vector)
   (setq _time __time)
   self)
  (:vector
   (&rest __vector)
   (if (keywordp (car __vector))
       (send* _vector __vector)
     (progn
       (if __vector (setq _vector (car __vector)))
       _vector)))
  (:time
   (&rest __time)
   (if (keywordp (car __time))
       (send* _time __time)
     (progn
       (if __time (setq _time (car __time)))
       _time)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Vector3 _vector
    (send _vector :serialization-length)
    ;; std_msgs/UInt64 _time
    (send _time :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Vector3 _vector
       (send _vector :serialize s)
     ;; std_msgs/UInt64 _time
       (send _time :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Vector3 _vector
     (send _vector :deserialize buf ptr-) (incf ptr- (send _vector :serialization-length))
   ;; std_msgs/UInt64 _time
     (send _time :deserialize buf ptr-) (incf ptr- (send _time :serialization-length))
   ;;
   self)
  )

(setf (get mqtt_ros_bridge::Vector3Time :md5sum-) "df93b39e31bd03890a20bf8ae7643eeb")
(setf (get mqtt_ros_bridge::Vector3Time :datatype-) "mqtt_ros_bridge/Vector3Time")
(setf (get mqtt_ros_bridge::Vector3Time :definition-)
      "geometry_msgs/Vector3 vector
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
")



(provide :mqtt_ros_bridge/Vector3Time "df93b39e31bd03890a20bf8ae7643eeb")


