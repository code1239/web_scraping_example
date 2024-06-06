# Web Scraping Script

This Python script utilizes Selenium to scrape image sources from a website and save them to a JSON file.

## Prerequisites

- Python 3.x
- Chrome WebDriver
- `config.ini` file with the website URL specified

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies:

pip install selenium

3. Download Chrome WebDriver and place it in your system's PATH or in the same directory as the script.

## Usage

1. Configure the `config.ini` file with the desired website URL.
2. Run the script:

python script.py

3. The script will open the specified website, scrape image sources, and save them to `image_sources.json`.

## Configuration

- `config.ini`: Specify the website URL under the `[commands]` section.

## Logging

- Log messages are written to `scraping_log.log` file for tracking script execution.

