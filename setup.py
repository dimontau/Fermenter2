from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Fermenter2',
      version='0.1',
      description='Fermenter2',
      author=['Dmitriy'],
      author_email='intenal@mail.ru',
      url='',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'Fermenter2': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['Fermenter2'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
