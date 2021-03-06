from setuptools import setup, find_packages

setup(
    name = "copyartifacts",
    version = "1.0-beta.1",
    description="beets plugin to copy non-music files to import path",
    author='Sami Barakat',
    author_email='sami@sbarakat.co.uk',
    url='https://github.com/sbarakat/beets-copyartifacts.git',
    download_url='https://github.com/sbarakat/beets-copyartifacts.git',
    license='MIT',

    packages=['beetsplug'],
    namespace_packages=['beetsplug'],
    install_requires = ['beets>=1.3.2']
)
