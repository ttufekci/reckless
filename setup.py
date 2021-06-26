from setuptools import find_packages, setup
setup(
    name='reckless',
    packages=find_packages(include=['reckless']),
    version='0.1.1',
    description='Python Indicator Library for Automated Trading',
    author='onbirkod',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)