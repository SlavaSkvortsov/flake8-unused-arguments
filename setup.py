from setuptools import setup

requires = [
    "flake8 > 3.0.0",
]

setup(
    name="flake8_unused_arguments",
    license="MIT",
    version="1.0.0",
    description="flake8 extension to warn on unused function arguments",
    author="Nathan Hoad",
    author_email="nathan@hoad.io",
    modules=["flake8_unused_arguments"],
    url="https://github.com/nathan-hoad/flake8-unused-arguments",
    install_requires=requires,
    entry_points={
        "flake8.extension": ["U10 = flake8_unused_arguments:Plugin"],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)