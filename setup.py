from setuptools import setup, find_packages
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="wrapcolor",
    version="0.1.0",
    description="Universal ANSI colorizer for Python (8/16 colors, 256-color, RGB, styles)",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Bohdan",
    author_email="datcukbogdan@gmail.com",
    url="https://github.com/yourusername/wrapcolor",
    license="MIT",
    packages=find_packages(include=["wrapcolor", "wrapcolor.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Terminals",
        "Topic :: Text Processing :: General",
        "Environment :: Console",
    ],
    python_requires=">=3.10",
)