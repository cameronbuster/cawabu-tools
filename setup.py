from setuptools import find_packages, setup

setup(
    name='cawabu-tools',
    packages=find_packages(include=['cawabu_tools']),
    version='0.0.1',
    description='A library for mathematical expression',
    author='Cawabu',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
