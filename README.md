# GHCN Daily Data Converter

## Overview
The `dly_to_csv.py` script in the GHCN Daily Data Converter repository efficiently parses and converts GHCN (Global Historical Climatology Network) `.dly` files into a single merged CSV format. This tool is designed for researchers and data analysts, optimized for high efficiency and low memory usage, making it suitable for processing large climate datasets.

## Features
- **Efficient Line-by-Line Processing**: Processes `.dly` files line by line to minimize memory usage and handle large datasets effectively.
- **Concurrent Processing**: Utilizes Python's concurrent futures to accelerate the processing of multiple `.dly` files simultaneously.
- **Streaming Data Writing**: Writes data directly to a CSV file in a streaming fashion, reducing memory and I/O overhead significantly.
- **Descriptive Headers in CSV**: Includes detailed headers in the CSV file, providing context and ease of understanding for the data fields.
- **Handling Missing Values**: Converts missing values (`-9999` in `.dly` files) to 'None' in the CSV output, enhancing data quality for subsequent analysis.

## Prerequisites
- Python installed on your system.
- `pandas` library for data manipulation. Install using `pip install pandas` if not already present.
- `psutil` library for system resource monitoring. Install using `pip install psutil`.

## Setup
1. **Download the Script**: Access the `dly_to_csv.py` file from the [GHCN Daily Data Converter](https://github.com/martin-international/ghcn-daily-data-converter) repository.
2. **Install Required Libraries**: Ensure Python, `pandas`, and `psutil` are installed on your system.

## Usage
1. **Prepare Directories**: Place `.dly` files in an input folder. Choose or create an output folder for the CSV file.
2. **Run the Script**: Execute `dly_to_csv.py`. The script will prompt for the input and output directories using a Tkinter dialog.
3. **Monitor the Process**: The script processes all `.dly` files in the input folder and saves a merged CSV file in the output folder.

## Output Format
- The output CSV file includes columns such as ID, Date, Element, Value, MFlag, QFlag, and SFlag, representing consolidated data from all processed `.dly` files.
- The CSV file begins with descriptive comments about each column, alongside a link to the GHCN Daily Readme for more detailed information.

## GHCN Daily Readme
For in-depth details on the GHCN `.dly` file format, including column and flag explanations, please refer to the GHCN Daily Readme:
[https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)
