
(cl:in-package :asdf)

(defsystem "mqtt_ros_bridge-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ImuPackage" :depends-on ("_package_ImuPackage"))
    (:file "_package_ImuPackage" :depends-on ("_package"))
    (:file "Vector3Time" :depends-on ("_package_Vector3Time"))
    (:file "_package_Vector3Time" :depends-on ("_package"))
  ))