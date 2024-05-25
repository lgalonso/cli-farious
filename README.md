# cli-farious
CLI-farious is a clever wordplay that combines "CLI" (command-line interface) and "various" to suggest a versatile and comprehensive log analysis tool.

## Limitations
Currently only available as a clonable repository, for Linux-Ubuntu distributions, Docker container under development.

## Installation

Clone the repository:

```bash
git clone https://github.com/lgalonso/cli-farious.git
```

### Dependencies

Install python version 3.11 or higher.

```bash
apt-get install python=3.11
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install requirements.txt
```

### Setup distribution
```bash
python setup.py bdist_wheel
```
```bash
python setup.py sdist
```

### Install package

From the cli-farious folder execute in terminal:

```bash
pip install .
```

## Run the application

Execute the run.py file with the '--help' flag to visualize what is possible with the tool:
```bash
run.py --help
```
