from setuptools import setup, find_packages

setup(
    name="salesdw-utils",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "send-sales-report=sales_dw_utils.cli:cli"
        ]
    },
    install_requires=[
        "psycopg2-binary",
        "python-dotenv"
    ]
)