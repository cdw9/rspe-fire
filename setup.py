from setuptools import setup, find_packages

version = "0.1"

long_description = (open('README.txt').read())

setup(
    name='rspe',
    version=version,
    description="",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',
    author='Six Feet Up, Inc.',
    author_email='info@sixfeetup.com',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['rspe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'sixfeetup.utils>=2.8',
        'Plone',
        'plone.app.caching',
        'rspe',
        'z3c.jbot',
        'plone.api',
        'collective.dexteritytextindexer',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
