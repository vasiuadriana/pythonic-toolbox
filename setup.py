from setuptools import setup, find_packages

setup(
    name="pythonic-toolbox",
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cdate=timing.conversion:cdate',
            'timestamp=timing.conversion:timestamp',
            'rm-pyc=files.cleanup:cleanup_pyc'
        ]
    }
)
