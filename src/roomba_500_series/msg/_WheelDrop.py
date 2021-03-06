"""autogenerated by genpy from roomba_500_series/WheelDrop.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import roomba_500_series.msg
import std_msgs.msg

class WheelDrop(genpy.Message):
  _md5sum = "0ce131cedcae0c89b4efbe13237e4425"
  _type = "roomba_500_series/WheelDrop"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """RoombaSwitch left
RoombaSwitch right

================================================================================
MSG: roomba_500_series/RoombaSwitch
Header header
bool state

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['left','right']
  _slot_types = ['roomba_500_series/RoombaSwitch','roomba_500_series/RoombaSwitch']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left,right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WheelDrop, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.left is None:
        self.left = roomba_500_series.msg.RoombaSwitch()
      if self.right is None:
        self.right = roomba_500_series.msg.RoombaSwitch()
    else:
      self.left = roomba_500_series.msg.RoombaSwitch()
      self.right = roomba_500_series.msg.RoombaSwitch()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.left.header.seq, _x.left.header.stamp.secs, _x.left.header.stamp.nsecs))
      _x = self.left.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3I.pack(_x.left.state, _x.right.header.seq, _x.right.header.stamp.secs, _x.right.header.stamp.nsecs))
      _x = self.right.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.right.state))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.left is None:
        self.left = roomba_500_series.msg.RoombaSwitch()
      if self.right is None:
        self.right = roomba_500_series.msg.RoombaSwitch()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left.header.seq, _x.left.header.stamp.secs, _x.left.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.left.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.left.state, _x.right.header.seq, _x.right.header.stamp.secs, _x.right.header.stamp.nsecs,) = _struct_B3I.unpack(str[start:end])
      self.left.state = bool(self.left.state)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.right.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.right.state,) = _struct_B.unpack(str[start:end])
      self.right.state = bool(self.right.state)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.left.header.seq, _x.left.header.stamp.secs, _x.left.header.stamp.nsecs))
      _x = self.left.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3I.pack(_x.left.state, _x.right.header.seq, _x.right.header.stamp.secs, _x.right.header.stamp.nsecs))
      _x = self.right.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.right.state))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.left is None:
        self.left = roomba_500_series.msg.RoombaSwitch()
      if self.right is None:
        self.right = roomba_500_series.msg.RoombaSwitch()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left.header.seq, _x.left.header.stamp.secs, _x.left.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.left.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.left.state, _x.right.header.seq, _x.right.header.stamp.secs, _x.right.header.stamp.nsecs,) = _struct_B3I.unpack(str[start:end])
      self.left.state = bool(self.left.state)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.right.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.right.state,) = _struct_B.unpack(str[start:end])
      self.right.state = bool(self.right.state)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_B3I = struct.Struct("<B3I")
