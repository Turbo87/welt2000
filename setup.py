import os

from setuptools import setup

about = {}
with open("welt2000/__about__.py") as fp:
    exec(fp.read(), about)


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def read_markdown(*paths):
    content = read(*paths)
    try:
        import pypandoc
        return pypandoc.convert(content, 'rst', format='md')
    except (IOError, ImportError):
        return content


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=read_markdown('README.md'),
    url=about['__uri__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__email__'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    install_requires=[
        'flask==0.10.1',
        'Flask-Script==0.6.6',
    ]
)
