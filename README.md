# Malicious PDF Generator
![Tests](https://github.com/MustafaSarikaya/malicious-pdf-generator/actions/workflows/tests.yml/badge.svg)

## Overview

The Malicious PDF Generator is a Python-based tool that allows you to generate PDF files with embedded JavaScript payloads. The tool provides two types of payloads: a download action and an alert message displaying the current date.

## Installation

To install the tool, you need to have Python and pip installed on your system. Once you have these prerequisites, you can install the tool by running the following command in your terminal:

```bash
pip install -e .
```

This command installs the tool and its dependencies.

## Usage

To use the tool, you can run the `malicious_pdf_generator` script from your command line. The script accepts several arguments:

- `-i` or `--input`: The path to the input PDF file. This argument is optional. If not provided, the tool uses a default input PDF file.
- `-o` or `--output`: The path to the output PDF file. This argument is optional. If not provided, the tool generates the output PDF file in the current directory.

Here's an example of how to run the script:

```bash
malicious_pdf_generator -i input.pdf -o output.pdf
```

```bash
Choose the payload to embed into the pdf file:
1. Download file (URL action)
2. Alert message
Enter the payload number: 1
```

In this example, the tool generates a malicious PDF file named `output.pdf` based on the `input.pdf` file. The PDF file contains a JavaScript payload that downloads to a file when the user opens the PDF file.

## Payloads

The tool provides two types of JavaScript payloads:

- `downloader`: This payload downloads a file when the PDF file is opened.
- `alert_date`: This payload displays an alert message with the current date when the PDF file is opened.
