from setuptools import setup, find_packages

setup(
   name='app',
   version='0.1.0',
   description='Hello world',
   author='Pickle Cillo',
   author_email='fake@email.com',
   packages=find_packages(exclude=('tests',)),
)
