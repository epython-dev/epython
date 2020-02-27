from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    version='0.0.4',
    name='epython',
    url='https://github.com/epython-dev/epython',
    description='A typed subset of Python to be used as an extension language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quansight Labs',
    author_email = 'labs@quansight.com',
    license='BSD-3',
    packages=['epython'],
    entry_points={
        'console_scripts': [
            'epython = epython.epython:main',
        ],
    },
   zip_safe=False,
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
