// Generated by gencpp from file mqtt_ros_bridge/Vector3Time.msg
// DO NOT EDIT!


#ifndef MQTT_ROS_BRIDGE_MESSAGE_VECTOR3TIME_H
#define MQTT_ROS_BRIDGE_MESSAGE_VECTOR3TIME_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Vector3.h>
#include <std_msgs/UInt64.h>

namespace mqtt_ros_bridge
{
template <class ContainerAllocator>
struct Vector3Time_
{
  typedef Vector3Time_<ContainerAllocator> Type;

  Vector3Time_()
    : vector()
    , time()  {
    }
  Vector3Time_(const ContainerAllocator& _alloc)
    : vector(_alloc)
    , time(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _vector_type;
  _vector_type vector;

   typedef  ::std_msgs::UInt64_<ContainerAllocator>  _time_type;
  _time_type time;





  typedef boost::shared_ptr< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> const> ConstPtr;

}; // struct Vector3Time_

typedef ::mqtt_ros_bridge::Vector3Time_<std::allocator<void> > Vector3Time;

typedef boost::shared_ptr< ::mqtt_ros_bridge::Vector3Time > Vector3TimePtr;
typedef boost::shared_ptr< ::mqtt_ros_bridge::Vector3Time const> Vector3TimeConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator1> & lhs, const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator2> & rhs)
{
  return lhs.vector == rhs.vector &&
    lhs.time == rhs.time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator1> & lhs, const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mqtt_ros_bridge

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
{
  static const char* value()
  {
    return "df93b39e31bd03890a20bf8ae7643eeb";
  }

  static const char* value(const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdf93b39e31bd0389ULL;
  static const uint64_t static_value2 = 0x0a20bf8ae7643eebULL;
};

template<class ContainerAllocator>
struct DataType< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mqtt_ros_bridge/Vector3Time";
  }

  static const char* value(const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Vector3 vector\n"
"std_msgs/UInt64 time\n"
"\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"================================================================================\n"
"MSG: std_msgs/UInt64\n"
"uint64 data\n"
;
  }

  static const char* value(const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.vector);
      stream.next(m.time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Vector3Time_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mqtt_ros_bridge::Vector3Time_<ContainerAllocator>& v)
  {
    s << indent << "vector: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.vector);
    s << indent << "time: ";
    s << std::endl;
    Printer< ::std_msgs::UInt64_<ContainerAllocator> >::stream(s, indent + "  ", v.time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MQTT_ROS_BRIDGE_MESSAGE_VECTOR3TIME_H
