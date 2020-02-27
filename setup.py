from setuptools import setup

setup(
    version='0.0.2',
    name='epython',
    url='https://github.com/epython-dev/epython',
    description='A typed subset of Python to be used as an extension language',
 ssss='epython',
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
    python_requires='>=3.8',
)
