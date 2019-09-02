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

"""Contains the programmatic representations of certain xml tags.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import errors

class Tag:
    """Represents an xml tag.
    """

    tag_name = 'BaseTag'
    required_kwargs = []

    def __init__(self, **kwargs):
        """Initialises the tag.

        Args:
          **kwargs: All attributes assigned to this tag.

        Raises:
          UnsatisfiedAttributesError: The required keyword arguments have not
                                      been satisfied.
        """

        self.kwargs = kwargs
        self._parse_kwargs()

    def _parse_kwargs(self):
        """Makes sure that all required keyword arguments have been specified.

        Note that keyword arguments cannot be repeated. We do not need to check
        for this because the Python interpreter does it for us.
        """

        if not isinstance(self.required_kwargs, set):
            self.required_kwargs = set(self.required_kwargs)

        for kwarg in self.kwargs:
            if kwarg in self.required_kwargs:
                self.required_kwargs.remove(kwarg)

        if self.required_kwargs:
            raise errors.UnsatisfiedAttributesError()

class Circle(Tag):
    """Represents an xml circle tag.
    """

    tag_name = 'circle'
    required_kwargs = ['id', 'x_center', 'y_center', 'radius']

class Line(Tag):
    """Represents an xml line tag.
    """

    tag_name = 'line'
    required_kwargs = ['id', 'x_start', 'y_start', 'x_end', 'y_end']

class Rect(Tag):
    """Represents an xml rect tag.
    """

    tag_name = 'rect'
    required_kwargs = ['id', 'x', 'y', 'width', 'height']
