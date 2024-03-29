# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waves/node/grpc/accounts_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves import amount_pb2 as waves_dot_amount__pb2
from waves import transaction_pb2 as waves_dot_transaction__pb2
from waves import recipient_pb2 as waves_dot_recipient__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='waves/node/grpc/accounts_api.proto',
  package='waves.node.grpc',
  syntax='proto3',
  serialized_options=b'\n\032com.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\252\002\017Waves.Node.Grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"waves/node/grpc/accounts_api.proto\x12\x0fwaves.node.grpc\x1a\x12waves/amount.proto\x1a\x17waves/transaction.proto\x1a\x15waves/recipient.proto\x1a\x1egoogle/protobuf/wrappers.proto\"!\n\x0e\x41\x63\x63ountRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"+\n\x0b\x44\x61taRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\t\"2\n\x0f\x42\x61lancesRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61ssets\x18\x04 \x03(\x0c\"\xfe\x01\n\x0f\x42\x61lanceResponse\x12?\n\x05waves\x18\x01 \x01(\x0b\x32..waves.node.grpc.BalanceResponse.WavesBalancesH\x00\x12\x1e\n\x05\x61sset\x18\x02 \x01(\x0b\x32\r.waves.AmountH\x00\x1a\x7f\n\rWavesBalances\x12\x0f\n\x07regular\x18\x01 \x01(\x03\x12\x12\n\ngenerating\x18\x02 \x01(\x03\x12\x11\n\tavailable\x18\x03 \x01(\x03\x12\x11\n\teffective\x18\x04 \x01(\x03\x12\x10\n\x08lease_in\x18\x05 \x01(\x03\x12\x11\n\tlease_out\x18\x06 \x01(\x03\x42\t\n\x07\x62\x61lance\"Y\n\x11\x44\x61taEntryResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x33\n\x05\x65ntry\x18\x02 \x01(\x0b\x32$.waves.DataTransactionData.DataEntry\"K\n\nScriptData\x12\x14\n\x0cscript_bytes\x18\x01 \x01(\x0c\x12\x13\n\x0bscript_text\x18\x02 \x01(\t\x12\x12\n\ncomplexity\x18\x03 \x01(\x03\"\x92\x01\n\rLeaseResponse\x12\x0f\n\x07leaseId\x18\x01 \x01(\x0c\x12\x1b\n\x13originTransactionId\x18\x02 \x01(\x0c\x12\x0e\n\x06sender\x18\x03 \x01(\x0c\x12#\n\trecipient\x18\x04 \x01(\x0b\x32\x10.waves.Recipient\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x03\x12\x0e\n\x06height\x18\x06 \x01(\x03\x32\xa4\x03\n\x0b\x41\x63\x63ountsApi\x12S\n\x0bGetBalances\x12 .waves.node.grpc.BalancesRequest\x1a .waves.node.grpc.BalanceResponse0\x01\x12I\n\tGetScript\x12\x1f.waves.node.grpc.AccountRequest\x1a\x1b.waves.node.grpc.ScriptData\x12T\n\x0fGetActiveLeases\x12\x1f.waves.node.grpc.AccountRequest\x1a\x1e.waves.node.grpc.LeaseResponse0\x01\x12T\n\x0eGetDataEntries\x12\x1c.waves.node.grpc.DataRequest\x1a\".waves.node.grpc.DataEntryResponse0\x01\x12I\n\x0cResolveAlias\x12\x1c.google.protobuf.StringValue\x1a\x1b.google.protobuf.BytesValueBs\n\x1a\x63om.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\xaa\x02\x0fWaves.Node.Grpcb\x06proto3'
  ,
  dependencies=[waves_dot_amount__pb2.DESCRIPTOR,waves_dot_transaction__pb2.DESCRIPTOR,waves_dot_recipient__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ACCOUNTREQUEST = _descriptor.Descriptor(
  name='AccountRequest',
  full_name='waves.node.grpc.AccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='waves.node.grpc.AccountRequest.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=155,
  serialized_end=188,
)


_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='waves.node.grpc.DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='waves.node.grpc.DataRequest.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='waves.node.grpc.DataRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=190,
  serialized_end=233,
)


_BALANCESREQUEST = _descriptor.Descriptor(
  name='BalancesRequest',
  full_name='waves.node.grpc.BalancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='waves.node.grpc.BalancesRequest.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assets', full_name='waves.node.grpc.BalancesRequest.assets', index=1,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=235,
  serialized_end=285,
)


_BALANCERESPONSE_WAVESBALANCES = _descriptor.Descriptor(
  name='WavesBalances',
  full_name='waves.node.grpc.BalanceResponse.WavesBalances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='regular', full_name='waves.node.grpc.BalanceResponse.WavesBalances.regular', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generating', full_name='waves.node.grpc.BalanceResponse.WavesBalances.generating', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available', full_name='waves.node.grpc.BalanceResponse.WavesBalances.available', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effective', full_name='waves.node.grpc.BalanceResponse.WavesBalances.effective', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lease_in', full_name='waves.node.grpc.BalanceResponse.WavesBalances.lease_in', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lease_out', full_name='waves.node.grpc.BalanceResponse.WavesBalances.lease_out', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=404,
  serialized_end=531,
)

_BALANCERESPONSE = _descriptor.Descriptor(
  name='BalanceResponse',
  full_name='waves.node.grpc.BalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='waves', full_name='waves.node.grpc.BalanceResponse.waves', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='waves.node.grpc.BalanceResponse.asset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BALANCERESPONSE_WAVESBALANCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='balance', full_name='waves.node.grpc.BalanceResponse.balance',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=288,
  serialized_end=542,
)


_DATAENTRYRESPONSE = _descriptor.Descriptor(
  name='DataEntryResponse',
  full_name='waves.node.grpc.DataEntryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='waves.node.grpc.DataEntryResponse.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entry', full_name='waves.node.grpc.DataEntryResponse.entry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=544,
  serialized_end=633,
)


_SCRIPTDATA = _descriptor.Descriptor(
  name='ScriptData',
  full_name='waves.node.grpc.ScriptData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='script_bytes', full_name='waves.node.grpc.ScriptData.script_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script_text', full_name='waves.node.grpc.ScriptData.script_text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='complexity', full_name='waves.node.grpc.ScriptData.complexity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=635,
  serialized_end=710,
)


_LEASERESPONSE = _descriptor.Descriptor(
  name='LeaseResponse',
  full_name='waves.node.grpc.LeaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaseId', full_name='waves.node.grpc.LeaseResponse.leaseId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='originTransactionId', full_name='waves.node.grpc.LeaseResponse.originTransactionId', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='waves.node.grpc.LeaseResponse.sender', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='waves.node.grpc.LeaseResponse.recipient', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.node.grpc.LeaseResponse.amount', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='waves.node.grpc.LeaseResponse.height', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=713,
  serialized_end=859,
)

_BALANCERESPONSE_WAVESBALANCES.containing_type = _BALANCERESPONSE
_BALANCERESPONSE.fields_by_name['waves'].message_type = _BALANCERESPONSE_WAVESBALANCES
_BALANCERESPONSE.fields_by_name['asset'].message_type = waves_dot_amount__pb2._AMOUNT
_BALANCERESPONSE.oneofs_by_name['balance'].fields.append(
  _BALANCERESPONSE.fields_by_name['waves'])
_BALANCERESPONSE.fields_by_name['waves'].containing_oneof = _BALANCERESPONSE.oneofs_by_name['balance']
_BALANCERESPONSE.oneofs_by_name['balance'].fields.append(
  _BALANCERESPONSE.fields_by_name['asset'])
_BALANCERESPONSE.fields_by_name['asset'].containing_oneof = _BALANCERESPONSE.oneofs_by_name['balance']
_DATAENTRYRESPONSE.fields_by_name['entry'].message_type = waves_dot_transaction__pb2._DATATRANSACTIONDATA_DATAENTRY
_LEASERESPONSE.fields_by_name['recipient'].message_type = waves_dot_recipient__pb2._RECIPIENT
DESCRIPTOR.message_types_by_name['AccountRequest'] = _ACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['BalancesRequest'] = _BALANCESREQUEST
DESCRIPTOR.message_types_by_name['BalanceResponse'] = _BALANCERESPONSE
DESCRIPTOR.message_types_by_name['DataEntryResponse'] = _DATAENTRYRESPONSE
DESCRIPTOR.message_types_by_name['ScriptData'] = _SCRIPTDATA
DESCRIPTOR.message_types_by_name['LeaseResponse'] = _LEASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountRequest = _reflection.GeneratedProtocolMessageType('AccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTREQUEST,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.AccountRequest)
  })
_sym_db.RegisterMessage(AccountRequest)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)

BalancesRequest = _reflection.GeneratedProtocolMessageType('BalancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _BALANCESREQUEST,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.BalancesRequest)
  })
_sym_db.RegisterMessage(BalancesRequest)

BalanceResponse = _reflection.GeneratedProtocolMessageType('BalanceResponse', (_message.Message,), {

  'WavesBalances' : _reflection.GeneratedProtocolMessageType('WavesBalances', (_message.Message,), {
    'DESCRIPTOR' : _BALANCERESPONSE_WAVESBALANCES,
    '__module__' : 'waves.node.grpc.accounts_api_pb2'
    # @@protoc_insertion_point(class_scope:waves.node.grpc.BalanceResponse.WavesBalances)
    })
  ,
  'DESCRIPTOR' : _BALANCERESPONSE,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.BalanceResponse)
  })
_sym_db.RegisterMessage(BalanceResponse)
_sym_db.RegisterMessage(BalanceResponse.WavesBalances)

DataEntryResponse = _reflection.GeneratedProtocolMessageType('DataEntryResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATAENTRYRESPONSE,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.DataEntryResponse)
  })
_sym_db.RegisterMessage(DataEntryResponse)

ScriptData = _reflection.GeneratedProtocolMessageType('ScriptData', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTDATA,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.ScriptData)
  })
_sym_db.RegisterMessage(ScriptData)

LeaseResponse = _reflection.GeneratedProtocolMessageType('LeaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEASERESPONSE,
  '__module__' : 'waves.node.grpc.accounts_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.LeaseResponse)
  })
_sym_db.RegisterMessage(LeaseResponse)


DESCRIPTOR._options = None

_ACCOUNTSAPI = _descriptor.ServiceDescriptor(
  name='AccountsApi',
  full_name='waves.node.grpc.AccountsApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=862,
  serialized_end=1282,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBalances',
    full_name='waves.node.grpc.AccountsApi.GetBalances',
    index=0,
    containing_service=None,
    input_type=_BALANCESREQUEST,
    output_type=_BALANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetScript',
    full_name='waves.node.grpc.AccountsApi.GetScript',
    index=1,
    containing_service=None,
    input_type=_ACCOUNTREQUEST,
    output_type=_SCRIPTDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetActiveLeases',
    full_name='waves.node.grpc.AccountsApi.GetActiveLeases',
    index=2,
    containing_service=None,
    input_type=_ACCOUNTREQUEST,
    output_type=_LEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataEntries',
    full_name='waves.node.grpc.AccountsApi.GetDataEntries',
    index=3,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATAENTRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResolveAlias',
    full_name='waves.node.grpc.AccountsApi.ResolveAlias',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTSAPI)

DESCRIPTOR.services_by_name['AccountsApi'] = _ACCOUNTSAPI

# @@protoc_insertion_point(module_scope)
