# py-tools 

An example of implementation of python for Devops tasks solutions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

* aws_info.py and eks_info.py functions return simplified version of from boto3 list describing AWS resourses that are in use.
* aws_snapshots functions allow to manage ec2 volumes snapshots by tag
* monitor.py monitors webpage status and optionally sends an e-mail if the webpage is corrupted
