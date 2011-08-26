from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='raptus.mailcone.mailfilter',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
        'setuptools',
        'grok',
        'grokui.admin',
        'fanstatic',
        'zope.fanstatic',
        'grokcore.startup',
        'zc.catalog',
        'hurry.query',
        'megrok.resource',
        'js.jquery',
        'js.jqueryui',
        'zope.pluggableauth',
        'megrok.rdb',
        
      ],
      entry_points={
          'fanstatic.libraries': [
              'raptus.mailcone.mailfilter = raptus.mailcone.mailfilter.resource:library',
          ]})
