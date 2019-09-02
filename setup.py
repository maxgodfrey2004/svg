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

"""Allows svg to be installed through pip/pip3.

To do so, run the following command on your terminal:
  pip install -e .
Alternatively, if you use pip3, run:
  pip3 install -e .
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import setuptools

DESCRIPTION = 'Create Scalable Vector Graphics in Python.'

setuptools.setup(
    name='svg',
    version='0.1.0',
    description=DESCRIPTION,
    author='Max Godfrey',
    license='Apache License 2.0',
    url='https://github.com/maxgodfrey2004/svg',
    packages=setuptools.find_packages(),
)
