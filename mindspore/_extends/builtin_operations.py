# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""builtin_operations"""
import functools
import numpy as np
from mindspore.common.tensor import Tensor
from mindspore.common.dtype import dtype_to_nptype, get_py_obj_dtype


def scalar_add(x, y):
    """Implement `scalar_add`."""
    return x + y


def scalar_mul(x, y):
    """Implement `scalar_mul`."""
    return x * y


def scalar_mod(x, y):
    """Implement `scalar_mul`."""
    return x % y


def scalar_sub(x, y):
    """Implement `scalar_sub`."""
    return x - y


def scalar_usub(x):
    """Implement `scalar_usub`."""
    return -x


def tuple_getitem(x, index):
    """Implement `tuple_getitem`."""
    if isinstance(x, Tensor):
        x = x.asnumpy()
        y = x[index]
        return Tensor(y)
    return x[index]


def scalar_gt(x, y):
    """Implement `scalar_gt`."""
    return x > y


def scalar_ne(x, y):
    """Implement `scalar_ne`."""
    return x != y


def scalar_eq(x, y):
    """Implement `scalar_eq`."""
    return x == y


def scalar_le(x, y):
    """Implement `scalar_le`."""
    return x <= y


def scalar_lt(x, y):
    """Implement `scalar_lt`."""
    return x < y


def identity(x):
    """Implement `identity`."""
    return x


def zeros_like_tensor(x):
    """Implement `zeros_like_tensor`."""
    x = x.asnumpy()
    value = Tensor(np.zeros(x.shape))
    return value


def switch(c, x, y):
    """Implement `switch`."""
    return x if c else y


def list_getitem(data, item):
    """Implement `list_getitem`."""
    return data[item]


def bool_not(x):
    """Implement `bool_not`."""
    return not x


def bool_and(x, y):
    """Implement `bool_and`."""
    return x and y


def bool_or(x, y):
    """Implement `bool_or`."""
    return x or y


def make_list(*xs):
    """Implement `make_list`."""
    return list(xs)


def list_len(x):
    """Implement `list_len`."""
    return len(x)


# only used in PyNative modes
def partial(*args):
    """Implement `partial`."""
    func = args[0].__call__
    partial_func = functools.partial(func, *args[1:])
    return partial_func


# only used in PyNative modes
def depend(value, expr):
    return value


def scalar_cast(x, t):
    """Implement scalar_cast."""
    np_type = dtype_to_nptype(t)
    value = np_type(x)
    cast_value = np.ndarray.item(value)
    return cast_value


def typeof(x):
    """Implement typeof."""
    return get_py_obj_dtype(x)


def tuple_to_array(x):
    """Implement `tuple_to_array`."""
    return Tensor(np.array(x))


def stop_gradient(x):
    """Implement `stop_gradient`."""
    return x
