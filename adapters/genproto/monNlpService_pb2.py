# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: adapters/genproto/monNlpService.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%adapters/genproto/monNlpService.proto\x12\x06monNlp\"\x1f\n\x0fTokenizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\"\n\x10TokenizeResponse\x12\x0e\n\x06tokens\x18\x01 \x03(\t2N\n\rMonNlpService\x12=\n\x08tokenize\x12\x17.monNlp.TokenizeRequest\x1a\x18.monNlp.TokenizeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'adapters.genproto.monNlpService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TOKENIZEREQUEST']._serialized_start=49
  _globals['_TOKENIZEREQUEST']._serialized_end=80
  _globals['_TOKENIZERESPONSE']._serialized_start=82
  _globals['_TOKENIZERESPONSE']._serialized_end=116
  _globals['_MONNLPSERVICE']._serialized_start=118
  _globals['_MONNLPSERVICE']._serialized_end=196
# @@protoc_insertion_point(module_scope)
