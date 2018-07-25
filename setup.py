#!/usr/bin/env python

try:
    from setuptools import setup
    from phonetic2bengali import __version__
    print __version__

    setup(name='phonetic2bengali',
          version='1.0.0',
          description='convert bengali text written in english to bengali while keeping english ony text',
          long_description=open('README.rst', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://github.org/SubrataSarkar32/phonetic2bengali/',
          packages=['phonetic2bengali','phonetic2bengali.avro'],
          package_data = {'phonetic2bengali': ['*.rst', '/avro/resources/*.json','/avro/utils/resources/*.json']},
          include_package_data = True,
          install_requires=["simplejson >= 3.0.0","pyenchant >= 2.0.0"],
          license='Apache v2.0',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            ]
          )

except ImportError:
    print 'Install setuptools'
