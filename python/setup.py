#!/usr/bin/env python

'''
Copyright 2012-2014 Ministerie van Sociale Zaken en Werkgelegenheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import glob
import os
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession
from qualitylib import VERSION


setup(name='quality_report',
      version=VERSION,
      description='Software quality report generator',
      author='ICTU',
      author_email='frank.niessink@ictu.nl',
      url='https://github.com/ICTU/quality-report',
      license='Apache License, Version 2.0',
      packages=find_packages(),
      scripts=['quality_report.py'],
      data_files=[(os.path.join('qualitylib', 'formatting', folder),
                   glob.glob(os.path.join('..', folder, files))) for folder,
                  files in (('img', '*.png'), ('js', '*.js'), 
                            ('html', '*.html'), ('css', '*.css'))],
      install_requires=[str(requirement.req) for requirement in
                        parse_requirements('requirements.txt', 
                                           session=PipSession())],
      test_suite='unittests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: Dutch',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: JavaScript',
          'Programming Language :: Unix Shell',
          'Topic :: Software Development :: Quality Assurance'])

