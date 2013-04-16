from setuptools import setup, find_packages
import os

version = '1.0b1-dev'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

tests_require=[
    'Cheetah',
    'templer.core',
],

setup(name='templer.plonebuildout',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone buildout',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='https://github.com/collective/templer.plonebuildout',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
          'templer.buildout',
          'templer.zope',
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),      
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      plone3_buildout = templer.plonebuildout:Plone3Buildout
      plone4_buildout = templer.plonebuildout:Plone4Buildout
      """,
      )
