from setuptools import setup, find_packages

setup(
    name="pythonic-toolbox",
    version='0.1',
    packages=['timing'],
    install_requires=[
        'Click',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['display-time=timing.conversion:cli']
    }
)
