from setuptools import setup, find_packages

setup(
    name='hello',
    version='0.01',
    description='hello world example using module.',
    author='adanba',
    packages=find_packages(),
    install_requires=[
                  'numpy >= 1.14.3',
                  'pyprg >= 0.1.1b7'
                        ]
)

