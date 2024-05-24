from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="cli-farious",
    version="0.0.1",
    description="CLI standalone tool to analyze log files",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lgalonso/cli-farious",
    author="lgalonso",
    author_email="lucasgarcialonso@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    python_requires=">=3.11",
)