# -*- coding: utf-8 -*-
#
# © 2013 Lyft, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.  You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

import os


# We use the version to construct the DOWNLOAD_URL.
VERSION = '0.0.1'

# URL to the repository on Github.
REPO_URL = 'https://github.com/lyft/pycollectd'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', VERSION))

setup(
    name='pycollectd',
    version=VERSION,
    author='Paul Lathrop',
    author_email='paul@tertiusfamily.net',
    maintainer='Paul Lathrop',
    maintainer_email='paul@tertiusfamily.net',
    description='Framework for writing collectd plugins in python.',
    long_description="""
    Framework for writing collectd plugins in python. These plugins are
    intended to be used with collectd's 'python' plugin.
    """,
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    license='Apache Software License',
    packages=find_packages(),
    install_requires=[
        'procfs',
        'pygerduty',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Monitoring',
    ],
)
