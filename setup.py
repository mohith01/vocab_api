from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'vocab_api'
LONG_DESCRIPTION = 'A package with vocabulary.com api.'

# Setting up
setup(
    name="vocab_api",
    version=VERSION,
    author="mohith01",
    author_email="<mohith01@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests','bs4'],
    keywords=['python', 'anki', 'api', 'words', 'vocab'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


