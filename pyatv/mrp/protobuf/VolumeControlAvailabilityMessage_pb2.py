# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/VolumeControlAvailabilityMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/VolumeControlAvailabilityMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n9pyatv/mrp/protobuf/VolumeControlAvailabilityMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"^\n VolumeControlAvailabilityMessage\x12\x1e\n\x16volumeControlAvailable\x18\x01 \x01(\x08\x12\x1a\n\x12volumeCapabilities\x18\x02 \x01(\x05:]\n volumeControlAvailabilityMessage\x12\x10.ProtocolMessage\x18\x16 \x01(\x0b\x32!.VolumeControlAvailabilityMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


VOLUMECONTROLAVAILABILITYMESSAGE_FIELD_NUMBER = 22
volumeControlAvailabilityMessage = _descriptor.FieldDescriptor(
  name='volumeControlAvailabilityMessage', full_name='volumeControlAvailabilityMessage', index=0,
  number=22, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_VOLUMECONTROLAVAILABILITYMESSAGE = _descriptor.Descriptor(
  name='VolumeControlAvailabilityMessage',
  full_name='VolumeControlAvailabilityMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volumeControlAvailable', full_name='VolumeControlAvailabilityMessage.volumeControlAvailable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumeCapabilities', full_name='VolumeControlAvailabilityMessage.volumeCapabilities', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['VolumeControlAvailabilityMessage'] = _VOLUMECONTROLAVAILABILITYMESSAGE
DESCRIPTOR.extensions_by_name['volumeControlAvailabilityMessage'] = volumeControlAvailabilityMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VolumeControlAvailabilityMessage = _reflection.GeneratedProtocolMessageType('VolumeControlAvailabilityMessage', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMECONTROLAVAILABILITYMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.VolumeControlAvailabilityMessage_pb2'
  # @@protoc_insertion_point(class_scope:VolumeControlAvailabilityMessage)
  })
_sym_db.RegisterMessage(VolumeControlAvailabilityMessage)

volumeControlAvailabilityMessage.message_type = _VOLUMECONTROLAVAILABILITYMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(volumeControlAvailabilityMessage)

# @@protoc_insertion_point(module_scope)
