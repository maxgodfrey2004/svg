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
        for kwarg in self.kwargs:
            self.kwargs[kwarg] = str(self.kwargs[kwarg])

        self._parse_kwargs()

    def __str__(self):
        """Returns an instance of this record as a string.
        """

        element_as_str = '<' + self.tag_name
        for kwarg in self.kwargs:
            element_as_str += ' ' + kwarg + '=' + self.kwargs[kwarg]
        element_as_str += '/>'

        return element_as_str

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

class Animate(Tag):
    """Represents an xml animation tag.
    """

    tag_name = 'animate'
    required_kwargs = ['attributeName', 'begin', 'dur', 'to', 'fill']

class AnimatableTag(Tag):
    """Represents an xml tag which may have animations applied to it.
    """

    tag_name = 'AnimatableTag'
    animations = []

    def __str__(self):
        """Returns an instance of this record as a string.
        """

        element_as_str = '<' + self.tag_name
        for kwarg in self.kwargs:
            element_as_str += ' {}={}'.format(kwarg, self.kwargs[kwarg])
        element_as_str += '>'

        for animation in self.animations:
            element_as_str += animation
        element_as_str += '</{}>'.format(self.tag_name)

        return element_as_str

    def add_animation(self, animation):
        """Adds an animation to the tag as a child element.

        Args:
          animation: The animation which we are adding as a child to the
                     current element.

        Usage:
          >>> c = elements.Circle(id='hello-there', cx=3, cy=4, r=7)
          >>> a = elements.Animate(attributeName='cx', begin='0.0s',
          ...                      dur='0.1s', to=4, fill='freeze')
          >>> c.add_animation(a)
        """

        self.animations.append(str(animation))

class Circle(AnimatableTag):
    """Represents an xml circle tag.
    """

    tag_name = 'circle'
    required_kwargs = ['id', 'cx', 'cy', 'r']

class Line(AnimatableTag):
    """Represents an xml line tag.
    """

    tag_name = 'line'
    required_kwargs = ['id', 'x1', 'y1', 'x2', 'y2']

class Rect(AnimatableTag):
    """Represents an xml rect tag.
    """

    tag_name = 'rect'
    required_kwargs = ['id', 'x', 'y', 'width', 'height']
