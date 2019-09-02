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

"""Contains errors which may be raised by modules within this application.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class UnsatisfiedAttributesError(Exception):
    """Represents an xml tag not having all required attributes.
    """

    def __init__(self, message=None):
        """Initialises the error.
        """

        self.message = message
        if not self.message:
            self.message = 'Tag does not have all required attributes'

        super().__init__(self.message)
