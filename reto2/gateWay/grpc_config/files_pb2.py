# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='files.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66iles.proto\"\x16\n\x05\x46iles\x12\r\n\x05\x46iles\x18\x01 \x01(\t\"\x06\n\x04Nulo2Z\n\x08getFiles\x12\x15\n\x05Ready\x12\x05.Nulo\x1a\x05.Nulo\x12\x1a\n\tListFiles\x12\x05.Nulo\x1a\x06.Files\x12\x1b\n\tFindFiles\x12\x06.Files\x1a\x06.Filesb\x06proto3'
)




_FILES = _descriptor.Descriptor(
  name='Files',
  full_name='Files',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Files', full_name='Files.Files', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=37,
)


_NULO = _descriptor.Descriptor(
  name='Nulo',
  full_name='Nulo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=45,
)

DESCRIPTOR.message_types_by_name['Files'] = _FILES
DESCRIPTOR.message_types_by_name['Nulo'] = _NULO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Files = _reflection.GeneratedProtocolMessageType('Files', (_message.Message,), {
  'DESCRIPTOR' : _FILES,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:Files)
  })
_sym_db.RegisterMessage(Files)

Nulo = _reflection.GeneratedProtocolMessageType('Nulo', (_message.Message,), {
  'DESCRIPTOR' : _NULO,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:Nulo)
  })
_sym_db.RegisterMessage(Nulo)



_GETFILES = _descriptor.ServiceDescriptor(
  name='getFiles',
  full_name='getFiles',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=47,
  serialized_end=137,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ready',
    full_name='getFiles.Ready',
    index=0,
    containing_service=None,
    input_type=_NULO,
    output_type=_NULO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListFiles',
    full_name='getFiles.ListFiles',
    index=1,
    containing_service=None,
    input_type=_NULO,
    output_type=_FILES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindFiles',
    full_name='getFiles.FindFiles',
    index=2,
    containing_service=None,
    input_type=_FILES,
    output_type=_FILES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETFILES)

DESCRIPTOR.services_by_name['getFiles'] = _GETFILES

# @@protoc_insertion_point(module_scope)