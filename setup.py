from setuptools import setup, find_packages

setup(
    name="malicious_pdf_generator",
    version="0.1",
    description="A Python package to generate malicious PDFs",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "javascript==1!1.1.3",
        "pdfalyzer==1.14.6",
        "pytest==8.1.1",
        "pytest-cov==4.1.0",
        "PyPDF2==2.12.1",
        "setuptools==69.2.0",
    ],
    entry_points={
        "console_scripts": [
            "malicious_pdf_generator=main:main",
        ],
    },
)