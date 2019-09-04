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

"""Tests modules and routines in svg.elements.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import svg.elements as elements
import svg.errors

def test_tag():
    """Tests elements.Tag.
    """

    basetag = elements.Tag()
    assert str(basetag).startswith('<' + basetag.tag_name)

    basetag.required_kwargs = ['doesnotexist']
    try:
        basetag._parse_kwargs()
    except svg.errors.UnsatisfiedAttributesError:
        pass

def test_parenttag():
    """Tests elements.ParentTag.
    """

    parenttag = elements.ParentTag()
    rect = elements.Rect(id='rect', x=20, y=20, width=40, height=10)
    parenttag.add_child(rect)

    parenttag_str = str(parenttag)

    assert parenttag_str.startswith('<' + parenttag.tag_name)
    assert '<rect' in parenttag_str
    assert 'id="rect"' in parenttag_str
    assert '</rect>' in parenttag_str

def test_animate():
    """Tests elements.Animate.
    """

    animate = elements.Animate(attributeName='attr', begin='0.1s', dur='1s',
                               to='3', fill='freeze')
    animate_str = str(animate)

    assert animate_str.startswith('<animate')
    assert 'attributeName="attr"' in animate_str
    assert 'fill="freeze"' in animate_str

def test_circle():
    """Tests elements.Circle.
    """

    circle = elements.Circle(id='circle', cx=3, cy=20, r=30)
    circle_str = str(circle)

    assert circle_str.startswith('<circle')
    assert 'cx="3"' in circle_str
    assert 'id="circle"' in circle_str

def test_ellipse():
    """Tests elements.Ellipse.
    """

    ellipse = elements.Ellipse(id='ellipse', cx=100, cy=100, rx=90, ry=30)
    ellipse_str = str(ellipse)

    assert ellipse_str.startswith('<ellipse')
    assert 'cy="100"' in ellipse_str
    assert 'rx="90"' in ellipse_str

def test_line():
    """Tests elements.Line.
    """

    line = elements.Line(id='line', x1=30, y1=30, x2=50, y2=50,
                         style='stroke:red')
    line_str = str(line)

    assert line_str.startswith('<line')
    assert 'style="stroke:red"' in line_str
    assert 'x1="30"' in line_str

def test_path():
    """Tests elements.Path.
    """

    path = elements.Path(id='path', d='M150 0 L75 200 L225 200 Z')
    path_str = str(path)

    assert path_str.startswith('<path')
    assert 'd="M150 0 L75 200 L225 200 Z"' in path_str

def test_polygon():
    """Tests elements.Polygon.
    """

    polygon = elements.Polygon(id='polygon', points='0,0 30,0 30,30 0,30')
    polygon_str = str(polygon)

    assert polygon_str.startswith('<polygon')
    assert 'points="0,0 30,0 30,30 0,30"' in polygon_str

def test_polyline():
    """Tests elements.Polyline.
    """

    polyline = elements.Polyline(id='polyline', points='20,20 40,65 60,30')
    polyline_str = str(polyline)

    assert polyline_str.startswith('<polyline')
    assert 'points="20,20 40,65 60,30"' in polyline_str

def test_rect():
    """Tests elements.Rect.
    """

    rect = elements.Rect(id='rect', x=20, y=20, width=100, height=50)
    rect_str = str(rect)

    assert rect_str.startswith('<rect')
    assert 'x="20"' in rect_str
    assert 'height="50"' in rect_str

def test_svg():
    """Tests elements.Svg.
    """

    svg = elements.Svg(width=300, height=400)
    svg_str = str(svg)

    assert 'xmlns="{}"'.format(elements.SVG_XMLNS_DEFAULT) in svg_str
    assert 'width="300"' in svg_str

def test_text():
    """Tests elements.Text.
    """

    text = elements.Text('SVG!', id='text', x=100, y=100)

    child_animate = elements.Animate(attributeName='x', begin='0.1s', dur='1s',
                                     to=30, fill='freeze')
    text.add_child(child_animate)

    text_str = str(text)
    assert text_str.startswith('<text')
    assert text_str.endswith('</text>')
    assert '<animate' in text_str
    assert 'SVG!' in text_str
    assert 'x="100"' in text_str
