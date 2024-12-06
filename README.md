# Malicious PDF Generator
![Tests](https://github.com/MustafaSarikaya/malicious-pdf-generator/actions/workflows/tests.yml/badge.svg)


## Overview

The Malicious PDF Generator is a Python-based tool designed for security professionals and researchers to generate PDF files with embedded JavaScript payloads for testing and educational purposes. In addition to payload embedding, this tool includes an **automated PDF detection testing process**, verifying the generated PDF against both the Elastic Stack and VirusShare services. This approach helps assess the effectiveness of your obfuscation techniques by determining if the generated PDF triggers security alerts or is flagged as malicious.


## Prerequisites
Before using this Python tool, ensure that you have the following prerequisites installed:

### Python Dependencies:

- javascript (version 1!1.1.3)
- pdfalyzer (version 1.14.6)
- pytest (version 8.1.1)
- pytest-cov (version 4.1.0)
- PyPDF2 (version 2.12.1)
- setuptools (version 69.2.0)
- pyfiglet (version 1.0.2)
- elasticsearch (version 8.9.0)
- python-dotenv (version 0.21.0)
- paramiko (version 3.5.0)
- scp (version 0.15.0)

### Node.js Dependencies:

- javascript-obfuscator (version 4.0.0)
- express (version 4.21.1)

Ensure that both Python and Node.js are installed on your system before proceeding with the installation of these dependencies. You can install Node.js from here if you haven't already.

## Installation

For detailed setup instructions, including configuring the Elastic Stack infrastructure, setting up the VirusShare API key, and configuring SSH connections to your testing VM, please refer to the [Setup Guide]().

## Usage

To use the tool, you can run the `python main.py` script from your command line. The script accepts several arguments:

- `-i` or `--input`: The path to the input PDF file. This argument is optional. If not provided, the tool uses a default input PDF file.
- `-o` or `--output`: The path to the output PDF file. This argument is optional. If not provided, the tool generates the output PDF file in the current directory.

Here's an example of how to run the script:

```bash
python main.py -i input.pdf -o output.pdf
```

```bash
    __  ___      ___      _                     ____  ____  ______
   /  |/  /___ _/ (_)____(_)___  __  _______   / __ \/ __ \/ ____/
  / /|_/ / __ `/ / / ___/ / __ \/ / / / ___/  / /_/ / / / / /_    
 / /  / / /_/ / / / /__/ / /_/ / /_/ (__  )  / ____/ /_/ / __/    
/_/  /_/\__,_/_/_/\___/_/\____/\__,_/____/  /_/   /_____/_/       
                                                                  
   ______                           __            
  / ____/__  ____  ___  _________ _/ /_____  _____
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/


Choose the payload to embed into the pdf file:
1. Download file (URL action)
2. Alert message
3.Collect information using Grabify (URL action)
Enter the payload number: 1
```

In this example, the tool generates a malicious PDF file named `output.pdf` based on the `input.pdf` file. The PDF file contains a JavaScript payload that downloads a file when the user opens the PDF file.

## Payloads

The tool provides three types of JavaScript payloads:

- `downloader`: This payload downloads a file when the PDF file is opened.
- `alert_date`: This payload displays an alert message with the current date when the PDF file is opened.
- `track_and_collect_information`: This payload track and collect informations(IP address and device information) about the person who open the pdf file.
