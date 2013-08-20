#!/usr/bin/env python

from setuptools import setup
import re
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()

major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|workflow|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' %
        (major_version, minor_version, major_version, minor_version + 1))

setup(name='trytond_helloworld',
    version=info.get('version', '0.0.1'),
    description=info.get('description', ''),
    package_dir={'trytond.modules.helloworld': '.'},
    packages=[
        'trytond.modules.helloworld',
    ],
    package_data={
        'trytond.modules.helloworld': info.get('xml', []) \
                + ['tryton.cfg'] + info.get('translation', []),
    },
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    helloworld = trytond.modules.helloworld
    """,
)
