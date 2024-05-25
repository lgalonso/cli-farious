# cli-farious
CLI-farious is a clever wordplay that combines "CLI" (command-line interface) and "various" to suggest a versatile and comprehensive log analysis tool.

## Limitations
Currently only available as a clonable repository, for Linux-Ubuntu distributions, Docker container under development.
Currently only analyzes SQUID Proxy logs.

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

From the app folder execute in terminal:

```bash
pip install .
```

## Run the application

Execute the run.py file with the '--help' flag to visualize what is possible with the tool:
```bash
run.py --help

Usage: run.py [OPTIONS]

  CLI-farious is a clever wordplay that combines CLI and various to suggest a
  versatile and comprehensive log analysis tool.

Options:
  -i TEXT    Input: Path to the log file to analyze.  [required]
  -o TEXT    Output: Path to output file to write the log analysis results.
             [required]
  --mfip     Returns most frequent IP from log file.
  --lfip     Returns least frequent IP from log file.
  --eps      Returns Events Per Second from log file.
  --bytes    Returns total amount of bytes exchanged from log file.
  --version  Show the version and exit.
  --help     Show this message and exit.
```

### Examples
The first time we run the program with any of the flags will also create the output file:

```bash
python run.py -i /home/dev/Downloads/access.log -o /home/dev/Downloads/output.json --mfip
Processing...
10.105.23.212
File '/home/dev/Downloads/output.json' created successfully!
Data written to /home/dev/Downloads/output.json!
```

```bash
python run.py -i /home/dev/Downloads/access.log -o /home/dev/Downloads/output.json --lfip
Processing...
10.105.53.146
Data written to /home/dev/Downloads/output.json!
```

```bash
python run.py -i /home/dev/Downloads/access.log -o /home/dev/Downloads/output.json --eps
0.013436174182444784
Data written to /home/dev/Downloads/output.json!
```

```bash
python run.py -i /home/dev/Downloads/access.log -o /home/dev/Downloads/output.json --bytes
Processing...
1100744267
Data written to /home/dev/Downloads/output.json!
```

Output file content:

```bash
cat output.json 
{
    "MFIP": "10.105.23.212",
    "LFIP": "10.105.53.146",
    "EPS": 0.013436174182444784,
    "Bytes": 1100744267
}
```
