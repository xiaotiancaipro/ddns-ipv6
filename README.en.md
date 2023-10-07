# ipv6-address-acquisition



### Description

Obtain the host IPv6 address and send it to the designated recipient through email.



### Project Architecture

```txt
ipv6-address-acquisition
├── config: Parameter configuration package
│   ├── smtp.py: SMTP server configuration
│   └── email.py: Email configuration
├── service
│   ├── email.py: Email related services
│   └── ipv6.py: IPv6 related services
├── view: Main Logic
│   └── ipv6_to_email.py 
├── utils: Utils toolkit
│   ├── logger.py: Log
│   ├── file.py: General tools related to file operations
│   ├── path.py: General tools related to path operations
│   └── system.py: General tools related to operation system
├── data: Data cache location
├── logs: Project log file
├── main.py
└── .env: Configuration information
```



### Installation

1、Enter the project directory `cd ipv6 address acquisition`;

2、Installation project dependencies `pip3 install -r requirements.txt`;

3、Copy the required configuration file for the project `cp. env. sample. env`, and configure all configuration information in the `. env` configuration file;

4、Execute project main program `python3 main.py`



### If this project is of some use to you, thank you for your star

