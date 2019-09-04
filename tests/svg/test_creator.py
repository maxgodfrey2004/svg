# Copyright 2019 Max Godfrey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests modules and routines in svg.creator.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import svg.creator as creator
import svg.errors

def test_creator():
    """Tests creator.Creator.
    """

    c = creator.Creator(width=100, height=100)
    
    try:
        c.write_to('unknown_file.unknown_extension')
    except svg.errors.UnknownExtensionError:
        pass
    
    c_str = str(c)
    assert c_str.startswith('<svg')

    c.write_to('svg_output.html')
    c.write_to('svg_output.svg')
