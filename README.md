# Python-Boto3
The following demo written is by @makexcake while completing Tech World With Nana DevOps bootcamp demos and exercises.

Collection of functions for monitoring and managing ec2 resources and monitoring servers.

The repo comes with a demo providing an example of possible usage of the functions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

* aws_info.py and eks_info.py functions return simplified version of from boto3 list describing AWS resourses that are in use.
* aws_snapshots functions allow to manage ec2 volumes snapshots by tag
* monitor.py monitors webpage status and optionally sends an e-mail if the webpage is corrupted

## Trying the demo

Insure that the following env vars: MAIL_ADR, MAIL_PWD are set. Uncomment the last line in demo and set the variable as in the exapmle:

```python
start_monitor('0.0.0.0', "http://example-url.com/", '340505b70ed8', "example@gmail.com")
```

