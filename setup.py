from setuptools import setup

setup(
    name='Test',
    packages=['website'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)