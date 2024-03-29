# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waves/invoke_script_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves import transaction_pb2 as waves_dot_transaction__pb2
from waves import amount_pb2 as waves_dot_amount__pb2
from waves import recipient_pb2 as waves_dot_recipient__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='waves/invoke_script_result.proto',
  package='waves',
  syntax='proto3',
  serialized_options=b'\n&com.wavesplatform.protobuf.transactionZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\252\002\005Waves',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n waves/invoke_script_result.proto\x12\x05waves\x1a\x17waves/transaction.proto\x1a\x12waves/amount.proto\x1a\x15waves/recipient.proto\"\xdc\x0c\n\x12InvokeScriptResult\x12\x32\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32$.waves.DataTransactionData.DataEntry\x12\x34\n\ttransfers\x18\x02 \x03(\x0b\x32!.waves.InvokeScriptResult.Payment\x12/\n\x06issues\x18\x03 \x03(\x0b\x32\x1f.waves.InvokeScriptResult.Issue\x12\x33\n\x08reissues\x18\x04 \x03(\x0b\x32!.waves.InvokeScriptResult.Reissue\x12-\n\x05\x62urns\x18\x05 \x03(\x0b\x32\x1e.waves.InvokeScriptResult.Burn\x12=\n\rerror_message\x18\x06 \x01(\x0b\x32&.waves.InvokeScriptResult.ErrorMessage\x12:\n\x0csponsor_fees\x18\x07 \x03(\x0b\x32$.waves.InvokeScriptResult.SponsorFee\x12/\n\x06leases\x18\x08 \x03(\x0b\x32\x1f.waves.InvokeScriptResult.Lease\x12<\n\rlease_cancels\x18\t \x03(\x0b\x32%.waves.InvokeScriptResult.LeaseCancel\x12\x35\n\x07invokes\x18\n \x03(\x0b\x32$.waves.InvokeScriptResult.Invocation\x1a\x39\n\x07Payment\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x1d\n\x06\x61mount\x18\x02 \x01(\x0b\x32\r.waves.Amount\x1a\x91\x01\n\x05Issue\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x05\x12\x12\n\nreissuable\x18\x06 \x01(\x08\x12\x0e\n\x06script\x18\x07 \x01(\x0c\x12\r\n\x05nonce\x18\x08 \x01(\x03\x1a\x42\n\x07Reissue\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x15\n\ris_reissuable\x18\x03 \x01(\x08\x1a(\n\x04\x42urn\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x1a,\n\nSponsorFee\x12\x1e\n\x07min_fee\x18\x01 \x01(\x0b\x32\r.waves.Amount\x1a]\n\x05Lease\x12#\n\trecipient\x18\x01 \x01(\x0b\x32\x10.waves.Recipient\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\r\n\x05nonce\x18\x03 \x01(\x03\x12\x10\n\x08lease_id\x18\x04 \x01(\x0c\x1a\x1f\n\x0bLeaseCancel\x12\x10\n\x08lease_id\x18\x01 \x01(\x0c\x1a*\n\x0c\x45rrorMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x1a\xf1\x02\n\x04\x43\x61ll\x12\x10\n\x08\x66unction\x18\x01 \x01(\t\x12\x16\n\nargs_bytes\x18\x02 \x03(\x0c\x42\x02\x18\x01\x12\x35\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\'.waves.InvokeScriptResult.Call.Argument\x1a\x87\x02\n\x08\x41rgument\x12\x17\n\rinteger_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0c\x62inary_value\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x17\n\rboolean_value\x18\x04 \x01(\x08H\x00\x12\x12\n\x08\x63\x61se_obj\x18\x05 \x01(\x0cH\x00\x12<\n\x04list\x18\n \x01(\x0b\x32,.waves.InvokeScriptResult.Call.Argument.ListH\x00\x1a>\n\x04List\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.waves.InvokeScriptResult.Call.ArgumentB\x07\n\x05value\x1a\x9a\x01\n\nInvocation\x12\x0c\n\x04\x64\x41pp\x18\x01 \x01(\x0c\x12,\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x1e.waves.InvokeScriptResult.Call\x12\x1f\n\x08payments\x18\x03 \x03(\x0b\x32\r.waves.Amount\x12/\n\x0cstateChanges\x18\x04 \x01(\x0b\x32\x19.waves.InvokeScriptResultBk\n&com.wavesplatform.protobuf.transactionZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\xaa\x02\x05Wavesb\x06proto3'
  ,
  dependencies=[waves_dot_transaction__pb2.DESCRIPTOR,waves_dot_amount__pb2.DESCRIPTOR,waves_dot_recipient__pb2.DESCRIPTOR,])




_INVOKESCRIPTRESULT_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='waves.InvokeScriptResult.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='waves.InvokeScriptResult.Payment.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.InvokeScriptResult.Payment.amount', index=1,
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
  serialized_start=678,
  serialized_end=735,
)

_INVOKESCRIPTRESULT_ISSUE = _descriptor.Descriptor(
  name='Issue',
  full_name='waves.InvokeScriptResult.Issue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='waves.InvokeScriptResult.Issue.asset_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='waves.InvokeScriptResult.Issue.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='waves.InvokeScriptResult.Issue.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.InvokeScriptResult.Issue.amount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decimals', full_name='waves.InvokeScriptResult.Issue.decimals', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reissuable', full_name='waves.InvokeScriptResult.Issue.reissuable', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script', full_name='waves.InvokeScriptResult.Issue.script', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='waves.InvokeScriptResult.Issue.nonce', index=7,
      number=8, type=3, cpp_type=2, label=1,
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
  serialized_start=738,
  serialized_end=883,
)

_INVOKESCRIPTRESULT_REISSUE = _descriptor.Descriptor(
  name='Reissue',
  full_name='waves.InvokeScriptResult.Reissue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='waves.InvokeScriptResult.Reissue.asset_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.InvokeScriptResult.Reissue.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_reissuable', full_name='waves.InvokeScriptResult.Reissue.is_reissuable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=885,
  serialized_end=951,
)

_INVOKESCRIPTRESULT_BURN = _descriptor.Descriptor(
  name='Burn',
  full_name='waves.InvokeScriptResult.Burn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='waves.InvokeScriptResult.Burn.asset_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.InvokeScriptResult.Burn.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=953,
  serialized_end=993,
)

_INVOKESCRIPTRESULT_SPONSORFEE = _descriptor.Descriptor(
  name='SponsorFee',
  full_name='waves.InvokeScriptResult.SponsorFee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_fee', full_name='waves.InvokeScriptResult.SponsorFee.min_fee', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=995,
  serialized_end=1039,
)

_INVOKESCRIPTRESULT_LEASE = _descriptor.Descriptor(
  name='Lease',
  full_name='waves.InvokeScriptResult.Lease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient', full_name='waves.InvokeScriptResult.Lease.recipient', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='waves.InvokeScriptResult.Lease.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='waves.InvokeScriptResult.Lease.nonce', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lease_id', full_name='waves.InvokeScriptResult.Lease.lease_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=1041,
  serialized_end=1134,
)

_INVOKESCRIPTRESULT_LEASECANCEL = _descriptor.Descriptor(
  name='LeaseCancel',
  full_name='waves.InvokeScriptResult.LeaseCancel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lease_id', full_name='waves.InvokeScriptResult.LeaseCancel.lease_id', index=0,
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
  serialized_start=1136,
  serialized_end=1167,
)

_INVOKESCRIPTRESULT_ERRORMESSAGE = _descriptor.Descriptor(
  name='ErrorMessage',
  full_name='waves.InvokeScriptResult.ErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='waves.InvokeScriptResult.ErrorMessage.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='waves.InvokeScriptResult.ErrorMessage.text', index=1,
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
  serialized_start=1169,
  serialized_end=1211,
)

_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST = _descriptor.Descriptor(
  name='List',
  full_name='waves.InvokeScriptResult.Call.Argument.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='waves.InvokeScriptResult.Call.Argument.List.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1512,
  serialized_end=1574,
)

_INVOKESCRIPTRESULT_CALL_ARGUMENT = _descriptor.Descriptor(
  name='Argument',
  full_name='waves.InvokeScriptResult.Call.Argument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='integer_value', full_name='waves.InvokeScriptResult.Call.Argument.integer_value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='binary_value', full_name='waves.InvokeScriptResult.Call.Argument.binary_value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='waves.InvokeScriptResult.Call.Argument.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='waves.InvokeScriptResult.Call.Argument.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='case_obj', full_name='waves.InvokeScriptResult.Call.Argument.case_obj', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list', full_name='waves.InvokeScriptResult.Call.Argument.list', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='waves.InvokeScriptResult.Call.Argument.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1320,
  serialized_end=1583,
)

_INVOKESCRIPTRESULT_CALL = _descriptor.Descriptor(
  name='Call',
  full_name='waves.InvokeScriptResult.Call',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='function', full_name='waves.InvokeScriptResult.Call.function', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args_bytes', full_name='waves.InvokeScriptResult.Call.args_bytes', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='waves.InvokeScriptResult.Call.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INVOKESCRIPTRESULT_CALL_ARGUMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1214,
  serialized_end=1583,
)

_INVOKESCRIPTRESULT_INVOCATION = _descriptor.Descriptor(
  name='Invocation',
  full_name='waves.InvokeScriptResult.Invocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dApp', full_name='waves.InvokeScriptResult.Invocation.dApp', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call', full_name='waves.InvokeScriptResult.Invocation.call', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payments', full_name='waves.InvokeScriptResult.Invocation.payments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stateChanges', full_name='waves.InvokeScriptResult.Invocation.stateChanges', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1586,
  serialized_end=1740,
)

_INVOKESCRIPTRESULT = _descriptor.Descriptor(
  name='InvokeScriptResult',
  full_name='waves.InvokeScriptResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='waves.InvokeScriptResult.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transfers', full_name='waves.InvokeScriptResult.transfers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='waves.InvokeScriptResult.issues', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reissues', full_name='waves.InvokeScriptResult.reissues', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='burns', full_name='waves.InvokeScriptResult.burns', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='waves.InvokeScriptResult.error_message', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sponsor_fees', full_name='waves.InvokeScriptResult.sponsor_fees', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leases', full_name='waves.InvokeScriptResult.leases', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lease_cancels', full_name='waves.InvokeScriptResult.lease_cancels', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invokes', full_name='waves.InvokeScriptResult.invokes', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INVOKESCRIPTRESULT_PAYMENT, _INVOKESCRIPTRESULT_ISSUE, _INVOKESCRIPTRESULT_REISSUE, _INVOKESCRIPTRESULT_BURN, _INVOKESCRIPTRESULT_SPONSORFEE, _INVOKESCRIPTRESULT_LEASE, _INVOKESCRIPTRESULT_LEASECANCEL, _INVOKESCRIPTRESULT_ERRORMESSAGE, _INVOKESCRIPTRESULT_CALL, _INVOKESCRIPTRESULT_INVOCATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=1740,
)

_INVOKESCRIPTRESULT_PAYMENT.fields_by_name['amount'].message_type = waves_dot_amount__pb2._AMOUNT
_INVOKESCRIPTRESULT_PAYMENT.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_ISSUE.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_REISSUE.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_BURN.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_SPONSORFEE.fields_by_name['min_fee'].message_type = waves_dot_amount__pb2._AMOUNT
_INVOKESCRIPTRESULT_SPONSORFEE.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_LEASE.fields_by_name['recipient'].message_type = waves_dot_recipient__pb2._RECIPIENT
_INVOKESCRIPTRESULT_LEASE.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_LEASECANCEL.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_ERRORMESSAGE.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST.fields_by_name['items'].message_type = _INVOKESCRIPTRESULT_CALL_ARGUMENT
_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST.containing_type = _INVOKESCRIPTRESULT_CALL_ARGUMENT
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['list'].message_type = _INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST
_INVOKESCRIPTRESULT_CALL_ARGUMENT.containing_type = _INVOKESCRIPTRESULT_CALL
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['integer_value'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['integer_value'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['binary_value'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['binary_value'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['string_value'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['string_value'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['boolean_value'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['boolean_value'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['case_obj'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['case_obj'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value'].fields.append(
  _INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['list'])
_INVOKESCRIPTRESULT_CALL_ARGUMENT.fields_by_name['list'].containing_oneof = _INVOKESCRIPTRESULT_CALL_ARGUMENT.oneofs_by_name['value']
_INVOKESCRIPTRESULT_CALL.fields_by_name['args'].message_type = _INVOKESCRIPTRESULT_CALL_ARGUMENT
_INVOKESCRIPTRESULT_CALL.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_INVOCATION.fields_by_name['call'].message_type = _INVOKESCRIPTRESULT_CALL
_INVOKESCRIPTRESULT_INVOCATION.fields_by_name['payments'].message_type = waves_dot_amount__pb2._AMOUNT
_INVOKESCRIPTRESULT_INVOCATION.fields_by_name['stateChanges'].message_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT_INVOCATION.containing_type = _INVOKESCRIPTRESULT
_INVOKESCRIPTRESULT.fields_by_name['data'].message_type = waves_dot_transaction__pb2._DATATRANSACTIONDATA_DATAENTRY
_INVOKESCRIPTRESULT.fields_by_name['transfers'].message_type = _INVOKESCRIPTRESULT_PAYMENT
_INVOKESCRIPTRESULT.fields_by_name['issues'].message_type = _INVOKESCRIPTRESULT_ISSUE
_INVOKESCRIPTRESULT.fields_by_name['reissues'].message_type = _INVOKESCRIPTRESULT_REISSUE
_INVOKESCRIPTRESULT.fields_by_name['burns'].message_type = _INVOKESCRIPTRESULT_BURN
_INVOKESCRIPTRESULT.fields_by_name['error_message'].message_type = _INVOKESCRIPTRESULT_ERRORMESSAGE
_INVOKESCRIPTRESULT.fields_by_name['sponsor_fees'].message_type = _INVOKESCRIPTRESULT_SPONSORFEE
_INVOKESCRIPTRESULT.fields_by_name['leases'].message_type = _INVOKESCRIPTRESULT_LEASE
_INVOKESCRIPTRESULT.fields_by_name['lease_cancels'].message_type = _INVOKESCRIPTRESULT_LEASECANCEL
_INVOKESCRIPTRESULT.fields_by_name['invokes'].message_type = _INVOKESCRIPTRESULT_INVOCATION
DESCRIPTOR.message_types_by_name['InvokeScriptResult'] = _INVOKESCRIPTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InvokeScriptResult = _reflection.GeneratedProtocolMessageType('InvokeScriptResult', (_message.Message,), {

  'Payment' : _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_PAYMENT,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Payment)
    })
  ,

  'Issue' : _reflection.GeneratedProtocolMessageType('Issue', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_ISSUE,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Issue)
    })
  ,

  'Reissue' : _reflection.GeneratedProtocolMessageType('Reissue', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_REISSUE,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Reissue)
    })
  ,

  'Burn' : _reflection.GeneratedProtocolMessageType('Burn', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_BURN,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Burn)
    })
  ,

  'SponsorFee' : _reflection.GeneratedProtocolMessageType('SponsorFee', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_SPONSORFEE,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.SponsorFee)
    })
  ,

  'Lease' : _reflection.GeneratedProtocolMessageType('Lease', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_LEASE,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Lease)
    })
  ,

  'LeaseCancel' : _reflection.GeneratedProtocolMessageType('LeaseCancel', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_LEASECANCEL,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.LeaseCancel)
    })
  ,

  'ErrorMessage' : _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_ERRORMESSAGE,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.ErrorMessage)
    })
  ,

  'Call' : _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), {

    'Argument' : _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), {

      'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
        'DESCRIPTOR' : _INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST,
        '__module__' : 'waves.invoke_script_result_pb2'
        # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Call.Argument.List)
        })
      ,
      'DESCRIPTOR' : _INVOKESCRIPTRESULT_CALL_ARGUMENT,
      '__module__' : 'waves.invoke_script_result_pb2'
      # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Call.Argument)
      })
    ,
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_CALL,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Call)
    })
  ,

  'Invocation' : _reflection.GeneratedProtocolMessageType('Invocation', (_message.Message,), {
    'DESCRIPTOR' : _INVOKESCRIPTRESULT_INVOCATION,
    '__module__' : 'waves.invoke_script_result_pb2'
    # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult.Invocation)
    })
  ,
  'DESCRIPTOR' : _INVOKESCRIPTRESULT,
  '__module__' : 'waves.invoke_script_result_pb2'
  # @@protoc_insertion_point(class_scope:waves.InvokeScriptResult)
  })
_sym_db.RegisterMessage(InvokeScriptResult)
_sym_db.RegisterMessage(InvokeScriptResult.Payment)
_sym_db.RegisterMessage(InvokeScriptResult.Issue)
_sym_db.RegisterMessage(InvokeScriptResult.Reissue)
_sym_db.RegisterMessage(InvokeScriptResult.Burn)
_sym_db.RegisterMessage(InvokeScriptResult.SponsorFee)
_sym_db.RegisterMessage(InvokeScriptResult.Lease)
_sym_db.RegisterMessage(InvokeScriptResult.LeaseCancel)
_sym_db.RegisterMessage(InvokeScriptResult.ErrorMessage)
_sym_db.RegisterMessage(InvokeScriptResult.Call)
_sym_db.RegisterMessage(InvokeScriptResult.Call.Argument)
_sym_db.RegisterMessage(InvokeScriptResult.Call.Argument.List)
_sym_db.RegisterMessage(InvokeScriptResult.Invocation)


DESCRIPTOR._options = None
_INVOKESCRIPTRESULT_CALL.fields_by_name['args_bytes']._options = None
# @@protoc_insertion_point(module_scope)
