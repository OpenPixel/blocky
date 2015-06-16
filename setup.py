from setuptools import setup

install_requires = ['flask']

setup(
    name='flask_blocky',
    version='0.0.1',
    description='Block rendering for flask.',
    long_description='',
    keywords='flask',
    author='Cameron A. Stitt',
    author_email='cameron@cam.st',
    url='https://github.com/cam-stitt/flask-blocky',
    license='BSD',
    py_modules=['flask_blocky'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
