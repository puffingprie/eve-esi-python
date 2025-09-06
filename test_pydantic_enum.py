#!/usr/bin/env python3

from typing import List, Union
from enum import Enum
from pydantic import BaseModel, ValidationError


class TestEnum(str, Enum):
    KNOWN_VALUE = "known_value"
    ANOTHER_VALUE = "another_value"


class TestModel(BaseModel):
    enum_list: List[Union[TestEnum, str]]


# Test 1: All known values
print("=== Test 1: All known values ===")
try:
    data = {"enum_list": ["known_value", "another_value"]}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.enum_list}")
    print(f"Types: {[type(x) for x in result.enum_list]}")
    print(f"First item equals enum: {result.enum_list[0] == TestEnum.KNOWN_VALUE}")
    print(f"First item equals string: {result.enum_list[0] == 'known_value'}")
except ValidationError as e:
    print(f"❌ Failed: {e}")

print()

# Test 2: Mix of known and unknown values
print("=== Test 2: Mix of known and unknown values ===")
try:
    data = {"enum_list": ["known_value", "unknown_value"]}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.enum_list}")
    print(f"Types: {[type(x) for x in result.enum_list]}")
    print(f"First item (known): {result.enum_list[0]} (type: {type(result.enum_list[0])})")
    print(f"Second item (unknown): {result.enum_list[1]} (type: {type(result.enum_list[1])})")
except ValidationError as e:
    print(f"❌ Failed: {e}")

print()

# Test 3: All unknown values
print("=== Test 3: All unknown values ===")
try:
    data = {"enum_list": ["completely_unknown", "also_unknown"]}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.enum_list}")
    print(f"Types: {[type(x) for x in result.enum_list]}")
except ValidationError as e:
    print(f"❌ Failed: {e}")