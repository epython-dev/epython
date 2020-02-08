from setuptools import setup

setup(
    name='epython',
    entry_points={
        'console_scripts': [
            'epython = epython:main',
        ],
    }
)
