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

"""Contains utilities pertinent to creating a Scalable Vector Graphic.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import svg.elements as elements
import svg.errors as errors

HTML_EXTENSION = '.html'

HTML_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<body>
{}
</body>
</html>
'''

XML_EXTENSION = '.svg'

XML_CONTENT = '''<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"
 "http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd">

{}
'''

class Creator(elements.Svg):
    """A Scalable Vector Graphic creator.
    """

    def write_to(self, outfile_path):
        """Writes the contents of the creator to a file.

        Args:
          outfile_path: The file to which we are writing the creator's
                        contents.
        """

        if outfile_path.endswith(HTML_EXTENSION):
            self.html_write(outfile_path)
        elif outfile_path.endswith(XML_EXTENSION):
            self.xml_write(outfile_path)
        else:
            raise errors.UnknownExtensionError()

    def xml_write(self, outfile_path):
        """Writes the contents of the creator as html to a file.

        Args:
          outfile_path: The file to which we are writing the creator's
                        contents (as html).
        """

        with open(outfile_path, 'w+') as outfile:
            outfile.write(HTML_CONTENT.format(str(self)))

    def xml_write(self, outfile_path):
        """Writes the contents of the creator as xml to a file.

        Args:
          outfile_path: The file to which we are writing the creator's
                        contents (as xml).
        """

        with open(outfile_path, 'w+') as outfile:
            outfile.write(XML_CONTENT.format(str(self)))
