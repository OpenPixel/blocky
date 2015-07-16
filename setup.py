from setuptools import setup, find_packages

install_requires = ['flask', 'django']

setup(
    name='blocky',
    version='0.0.1',
    description='Block rendering for flask.',
    long_description='',
    keywords='flask',
    author='Cameron A. Stitt',
    author_email='cameron@cam.st',
    url='https://github.com/OpenPixel/blocky',
    license='BSD',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
