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

import svg.errors as errors

SVG_XMLNS_DEFAULT = 'http://www.w3.org/2000/svg'

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
            element_as_str += ' {}="{}"'.format(kwarg, self.kwargs[kwarg])
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

class ParentTag(Tag):
    """Represents an xml tag which may have child tags added to it.
    """

    tag_name = 'ParentTag'
    children = []

    def __str__(self):
        """Returns an instance of this record as a string.
        """

        element_as_str = '<' + self.tag_name
        for kwarg in self.kwargs:
            element_as_str += ' {}="{}"'.format(kwarg, self.kwargs[kwarg])
        element_as_str += '>'

        for child in self.children:
            element_as_str += child
        element_as_str += '</{}>'.format(self.tag_name)

        return element_as_str

    def add_child(self, animation):
        """Adds a child element to the tag.

        Args:
          child: The tag which we are adding as a child to the current element.

        Usage:
          >>> c = elements.Circle(id='hello-there', cx=3, cy=4, r=7)
          >>> a = elements.Animate(attributeName='cx', begin='0.0s',
          ...                      dur='0.1s', to=4, fill='freeze')
          >>> c.add_child(a)
        """

        self.children.append(str(animation))

class Circle(ParentTag):
    """Represents an xml circle tag.
    """

    children = []
    tag_name = 'circle'
    required_kwargs = ['id', 'cx', 'cy', 'r']

class Ellipse(ParentTag):
    """Represents an xml ellipse tag.
    """

    children = []
    tag_name = 'ellipse'
    required_kwargs = ['id', 'cx', 'cy', 'rx', 'ry']

class Line(ParentTag):
    """Represents an xml line tag.
    """

    children = []
    tag_name = 'line'
    required_kwargs = ['id', 'x1', 'y1', 'x2', 'y2']

class Path(ParentTag):
    """Represents an xml path tag.
    """

    children = []
    tag_name = 'path'
    required_kwargs = ['id', 'd']

class Polygon(ParentTag):
    """Represents an xml polygon tag.
    """

    children = []
    tag_name = 'polygon'
    required_kwargs = ['id', 'points']

class Polyline(ParentTag):
    """Represents an xml polyline tag.
    """

    children = []
    tag_name = 'polyline'
    required_kwargs = ['id', 'points']

class Rect(ParentTag):
    """Represents an xml rect tag.
    """

    children = []
    tag_name = 'rect'
    required_kwargs = ['id', 'x', 'y', 'width', 'height']

class Svg(ParentTag):
    """Represents an xml svg tag.
    """

    children = []
    tag_name = 'svg'
    required_kwargs = ['width', 'height']

    def __init__(self, **kwargs):
        """Initialises the svg tag.

        Args:
          **kwargs: All attributes assigned to this tag.

        Raises:
          UnsatisfiedAttributesError: The required keyword arguments have not
                                      been satisfied.
        """

        super().__init__(**kwargs)

        self.kwargs = kwargs
        for kwarg in self.kwargs:
            self.kwargs[kwarg] = str(self.kwargs[kwarg])
        if 'xmlns' not in kwargs:
            kwargs['xmlns'] = SVG_XMLNS_DEFAULT

        self._parse_kwargs()

class Text(ParentTag):
    """Represents an xml text tag.
    """

    children = []
    tag_name = 'text'
    required_kwargs = ['id', 'x', 'y']

    def __init__(self, text='', **kwargs):
        """Initialises the text tag.

        Args:
          text: The text to render when the tag is converted to xml/html.
          **kwargs: All attributes assigned to this tag.
        
        Raises:
          UnsatisfiedAttributesError: The required keyword arguments have not
                                      been satisfied.
        """

        super().__init__(**kwargs)

        self.text = text
        self.kwargs = kwargs
        for kwarg in self.kwargs:
            self.kwargs[kwarg] = str(self.kwargs[kwarg])


    def __str__(self):
        """Returns an instance of this record as a string.
        """

        element_as_str = '<' + self.tag_name
        for kwarg in self.kwargs:
            element_as_str += ' {}="{}"'.format(kwarg, self.kwargs[kwarg])
        element_as_str += '>'

        element_as_str += self.text

        for child in self.children:
            element_as_str += child
        element_as_str += '</{}>'.format(self.tag_name)

        return element_as_str
