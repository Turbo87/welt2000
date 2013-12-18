import os

from setuptools import setup


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
    name='welt2000',
    version='0.1.0',
    description='a free airport and waypoint database',
    long_description=read_markdown('README.md'),
    url='http://github.com/Turbo87/welt2000/',
    license='MIT',
    author='Tobias Bieniek',
    author_email='tobias.bieniek@gmx.de',
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
    ]
)
