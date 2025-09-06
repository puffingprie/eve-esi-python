#!/usr/bin/env python3

from typing import List, Union
from enum import Enum
from pydantic import BaseModel, ValidationError


class TestEnum(str, Enum):
    KNOWN_VALUE = "known_value"
    ANOTHER_VALUE = "another_value"


class TestModel(BaseModel):
    # Test with just the enum (no Union)
    pure_enum_list: List[TestEnum]
    
    # Test with Union
    union_list: List[Union[TestEnum, str]]


# Test 1: Pure enum list with known values
print("=== Test 1: Pure enum list with known values ===")
try:
    data = {"pure_enum_list": ["known_value", "another_value"], "union_list": []}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.pure_enum_list}")
    print(f"Types: {[type(x) for x in result.pure_enum_list]}")
    print(f"Are they enum instances? {[isinstance(x, TestEnum) for x in result.pure_enum_list]}")
except ValidationError as e:
    print(f"❌ Failed: {e}")

print()

# Test 2: Pure enum list with unknown value (should fail)
print("=== Test 2: Pure enum list with unknown value ===")
try:
    data = {"pure_enum_list": ["known_value", "unknown_value"], "union_list": []}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.pure_enum_list}")
except ValidationError as e:
    print(f"❌ Expected failure: {e}")

print()

# Test 3: Union list behavior
print("=== Test 3: Union list with known values ===")
try:
    data = {"pure_enum_list": ["known_value"], "union_list": ["known_value", "another_value"]}
    result = TestModel.model_validate(data)
    print(f"✅ Success: {result.union_list}")
    print(f"Types: {[type(x) for x in result.union_list]}")
    print(f"Are they enum instances? {[isinstance(x, TestEnum) for x in result.union_list]}")
    
    # Compare the pure enum vs union behavior
    print(f"Pure enum type: {type(result.pure_enum_list[0])}")
    print(f"Union type: {type(result.union_list[0])}")
    print(f"Pure enum is TestEnum instance: {isinstance(result.pure_enum_list[0], TestEnum)}")
    print(f"Union is TestEnum instance: {isinstance(result.union_list[0], TestEnum)}")
    
except ValidationError as e:
    print(f"❌ Failed: {e}")