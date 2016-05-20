import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "empty_python",
    version = "0.0.1",
    author = "Ben van Werkhoven",
    author_email = "b.vanwerkhoven@esciencecenter.nl",
    description = ("An empty Python project"),
    license = "Apache 2.0",
    keywords = "Python",
    url = "https://github.com/benvanwerkhoven/empty_python",
    packages=['empty_python'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
)

