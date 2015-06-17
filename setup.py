from setuptools import find_packages, setup

install_requires = ['flask', 'jinja2']

setup(
    name='flask_blocky',
    version='0.0.1',
    description='Block rendering for flask.',
    long_description='',
    keywords='flask jinja2',
    author='Cameron A. Stitt',
    author_email='cameron@cam.st',
    url='https://github.com/OpenPixel/flask-blocky',
    license='BSD',
    packages=find_packages(exclude=['docs', 'tests*']),
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "Topic :: Software Development :: Libraries :: Python Modules",

        "Programming Language :: Python",
    ]
)
