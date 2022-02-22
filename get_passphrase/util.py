#!/usr/bin/env python

from typing import Type, Any, Dict

from .typehints import JSONDictType, JSONType
import json

def full_name_of_type(t: Type) -> str:
  module: str = t.__module__
  if module == 'builtins':
    result: str = t.__qualname__
  else:
    result = module + '.' + t.__qualname__
  return result

def full_type(o: Any) -> str:
  return full_name_of_type(o.__class__)

def copy_json_data(data: JSONType) -> JSONType:
  return json.loads(json.dumps(data))

def copy_context(context: Dict) -> Dict:
  return dict(context)
