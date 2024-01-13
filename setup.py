from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="name_generator",
    version="1.0.0",
    description="Name Generator for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ferdinandkeller/name_generator",
    author="Ferdinand Keller",
    author_email="ferdinand.keller@proton.me",
    license="MIT",
    packages=["name_generator"],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="name generator name_generator moby docker docker-names",
)
