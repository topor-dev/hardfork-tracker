from os.path import dirname, join

from setuptools import find_packages, setup

import hardfork

with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='hardfork tracker',
    version=hardfork.__version__,
    long_description_content_type='text/markdown',
    url='https://github.com/topor-dev/hardfork-tracker',
    author='Vadim Tokarev',
    license='MIT',
    packages=find_packages(),
    python_requires='~=3.6',
    entry_points={
        'console_scripts': [
            'hardfork-tracker=hardfork.__main__:main',
        ],
    },
)
