from setuptools import setup, find_packages

setup(
   name='solver',
   version='1.0',
   description='My answer to the greatest task of all time!',
   author='Eugene Kokachev',
   url='https://github.com/ekokachev/homeschooling-shokunin/',
   author_email='Send me a hug rather',
   packages=find_packages("."),
   install_requires=['pytest'], #external packages as dependencies
)