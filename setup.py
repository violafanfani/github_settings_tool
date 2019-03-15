import os
from setuptools import find_packages, setup

# determining the directory containing setup.py
setup_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_path, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

setup(
    # package information
    name = 'github_settings_tool',
    packages = find_packages(),
    version = '0.0.3',
    description = 'tool to test how to publish a package',
    long_description = readme,
    license = 'MIT',
    url='https://github.com/violafanfani/github_settings_tool.git',
    keywords='',

    # author information
    author = 'Viola Fanfani',
    author_email = 'viola.fanfani@gmail.com',

    # installation info and requirements
    install_requires=[],
    setup_requires=[],

    # test info and requirements
    test_suite='tests',
    tests_require=[],

    # package deployment info
    include_package_data=True,
    zip_safe=False,

    # all tools have cli interface
    entry_points={
        'console_scripts': [
            'github_settings_tool=github_settings_tool.cli:main',
        ],
    },
)
