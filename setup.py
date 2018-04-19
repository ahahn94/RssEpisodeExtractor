from setuptools import setup

setup(
    name='RssEpisodeExtractor',
    version='1.0',
    packages=['rssepisodeextractor'],
    package_data={'rssepisodeextractor': ['gui.glade', 'icon.png']},
    include_package_data=True,
    url='https://github.com/ahahn94/RssEpisodeExtractor',
    license='GNU GPL 2',
    author='ahahn94',
    author_email='ahahn94@outlook.com',
    description='Get a list of links to the episodes of a podcast which uses an rss feed with pagination.',
    install_requires=['gi', 'feedparser'],
)
