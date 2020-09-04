import codecs
import setuptools


setuptools.setup(
    name="bnemo",
    version="1.0",
    author="",
    author_email="",
    description="",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/faruk-ahmad/bnemo",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    
)
