from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="cli-farious",
    version="1.0.0",
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
        "Operating System :: Ubuntu 24.04 LTS",
    ],
    install_requires=["click==8.1.7"],
    python_requires=">=3.11",
)