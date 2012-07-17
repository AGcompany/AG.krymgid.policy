from setuptools import setup, find_packages
import os

version = '1.0'

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

setup(name='AG.krymgid.policy',
      version=version,
      description="Plone krymgid site policy",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        ],
      keywords='',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='https://github.com/AGcompany/AG.krymgid.policy',
      license='gpl',
      packages=find_packages('src',exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['AG', 'AG.krymgid'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plonetheme.discovery',
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
