# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dlink.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='dlink.proto',
    package='dgiot',
    syntax='proto3',
    serialized_options=b'\n\026io.grpc.examples.dlinkB\nDlinkProtoP\001\242\002\005dlink',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0b\x64link.proto\x12\x05\x64giot\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\"\xa0\x01\n\x13HealthCheckResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.dgiot.HealthCheckResponse.ServingStatus\"O\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x12\x13\n\x0fSERVICE_UNKNOWN\x10\x03\x32\xbf\x01\n\x05\x44link\x12\x34\n\x08SayHello\x12\x13.dgiot.HelloRequest\x1a\x11.dgiot.HelloReply\"\x00\x12>\n\x05\x43heck\x12\x19.dgiot.HealthCheckRequest\x1a\x1a.dgiot.HealthCheckResponse\x12@\n\x05Watch\x12\x19.dgiot.HealthCheckRequest\x1a\x1a.dgiot.HealthCheckResponse0\x01\x42.\n\x16io.grpc.examples.dlinkB\nDlinkProtoP\x01\xa2\x02\x05\x64linkb\x06proto3'
)


_HEALTHCHECKRESPONSE_SERVINGSTATUS = _descriptor.EnumDescriptor(
    name='ServingStatus',
    full_name='dgiot.HealthCheckResponse.ServingStatus',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='SERVING', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='NOT_SERVING', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='SERVICE_UNKNOWN', index=3, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=204,
    serialized_end=283,
)
_sym_db.RegisterEnumDescriptor(_HEALTHCHECKRESPONSE_SERVINGSTATUS)


_HELLOREQUEST = _descriptor.Descriptor(
    name='HelloRequest',
    full_name='dgiot.HelloRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='dgiot.HelloRequest.name', index=0,
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
    serialized_start=22,
    serialized_end=50,
)


_HELLOREPLY = _descriptor.Descriptor(
    name='HelloReply',
    full_name='dgiot.HelloReply',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='message', full_name='dgiot.HelloReply.message', index=0,
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
    serialized_start=52,
    serialized_end=81,
)


_HEALTHCHECKREQUEST = _descriptor.Descriptor(
    name='HealthCheckRequest',
    full_name='dgiot.HealthCheckRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='service', full_name='dgiot.HealthCheckRequest.service', index=0,
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
    serialized_start=83,
    serialized_end=120,
)


_HEALTHCHECKRESPONSE = _descriptor.Descriptor(
    name='HealthCheckResponse',
    full_name='dgiot.HealthCheckResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status', full_name='dgiot.HealthCheckResponse.status', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _HEALTHCHECKRESPONSE_SERVINGSTATUS,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=123,
    serialized_end=283,
)

_HEALTHCHECKRESPONSE.fields_by_name['status'].enum_type = _HEALTHCHECKRESPONSE_SERVINGSTATUS
_HEALTHCHECKRESPONSE_SERVINGSTATUS.containing_type = _HEALTHCHECKRESPONSE
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['HealthCheckRequest'] = _HEALTHCHECKREQUEST
DESCRIPTOR.message_types_by_name['HealthCheckResponse'] = _HEALTHCHECKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
    'DESCRIPTOR': _HELLOREQUEST,
    '__module__': 'dlink_pb2'
    # @@protoc_insertion_point(class_scope:dgiot.HelloRequest)
})
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
    'DESCRIPTOR': _HELLOREPLY,
    '__module__': 'dlink_pb2'
    # @@protoc_insertion_point(class_scope:dgiot.HelloReply)
})
_sym_db.RegisterMessage(HelloReply)

HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), {
    'DESCRIPTOR': _HEALTHCHECKREQUEST,
    '__module__': 'dlink_pb2'
    # @@protoc_insertion_point(class_scope:dgiot.HealthCheckRequest)
})
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType('HealthCheckResponse', (_message.Message,), {
    'DESCRIPTOR': _HEALTHCHECKRESPONSE,
    '__module__': 'dlink_pb2'
    # @@protoc_insertion_point(class_scope:dgiot.HealthCheckResponse)
})
_sym_db.RegisterMessage(HealthCheckResponse)


DESCRIPTOR._options = None

_DLINK = _descriptor.ServiceDescriptor(
    name='Dlink',
    full_name='dgiot.Dlink',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=286,
    serialized_end=477,
    methods=[
        _descriptor.MethodDescriptor(
            name='SayHello',
            full_name='dgiot.Dlink.SayHello',
            index=0,
            containing_service=None,
            input_type=_HELLOREQUEST,
            output_type=_HELLOREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Check',
            full_name='dgiot.Dlink.Check',
            index=1,
            containing_service=None,
            input_type=_HEALTHCHECKREQUEST,
            output_type=_HEALTHCHECKRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Watch',
            full_name='dgiot.Dlink.Watch',
            index=2,
            containing_service=None,
            input_type=_HEALTHCHECKREQUEST,
            output_type=_HEALTHCHECKRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_DLINK)

DESCRIPTOR.services_by_name['Dlink'] = _DLINK

# @@protoc_insertion_point(module_scope)
