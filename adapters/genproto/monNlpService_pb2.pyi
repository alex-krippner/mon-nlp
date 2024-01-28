from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenizeRequest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class TokenizeResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    def __init__(self, tokens: _Optional[_Iterable[_Union[Token, _Mapping]]] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ("text", "orth_", "lemma_", "norm_", "lower_", "shape_", "prefix_", "suffix_", "pos_", "tag_", "dep_", "lang_")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ORTH__FIELD_NUMBER: _ClassVar[int]
    LEMMA__FIELD_NUMBER: _ClassVar[int]
    NORM__FIELD_NUMBER: _ClassVar[int]
    LOWER__FIELD_NUMBER: _ClassVar[int]
    SHAPE__FIELD_NUMBER: _ClassVar[int]
    PREFIX__FIELD_NUMBER: _ClassVar[int]
    SUFFIX__FIELD_NUMBER: _ClassVar[int]
    POS__FIELD_NUMBER: _ClassVar[int]
    TAG__FIELD_NUMBER: _ClassVar[int]
    DEP__FIELD_NUMBER: _ClassVar[int]
    LANG__FIELD_NUMBER: _ClassVar[int]
    text: str
    orth_: str
    lemma_: str
    norm_: str
    lower_: str
    shape_: str
    prefix_: str
    suffix_: str
    pos_: str
    tag_: str
    dep_: str
    lang_: str
    def __init__(self, text: _Optional[str] = ..., orth_: _Optional[str] = ..., lemma_: _Optional[str] = ..., norm_: _Optional[str] = ..., lower_: _Optional[str] = ..., shape_: _Optional[str] = ..., prefix_: _Optional[str] = ..., suffix_: _Optional[str] = ..., pos_: _Optional[str] = ..., tag_: _Optional[str] = ..., dep_: _Optional[str] = ..., lang_: _Optional[str] = ...) -> None: ...
