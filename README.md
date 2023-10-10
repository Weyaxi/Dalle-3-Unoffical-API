# DALL-E 3 Unofficial API

The DALL-E 3 Unofficial API is a Python script that allows you to interact with the DALL-E 3 AI image generator app, enabling you to search for and download images created by the model.

## Table of Contents
- [Introduction](#dall-e-3-unofficial-api)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functionality](#functionality)
- [Output](#output)
  
## Prerequisites

Before using the DALL-E 3 Unofficial API, ensure you have the following prerequisites set up:

- Python 3.x
- Required Python packages: `undetected_chromedriver`, `selenium`, `requests`

To install the required packages, run:

```bash
pip install undetected-chromedriver selenium requests
```

## Usage

To utilize the DALL-E 3 Unofficial API, follow these steps:

1. Clone the repository or download the repo to your local machine.

```bash
git clone https://github.com/Weyaxi/Dalle-3-Unoffical-API
```

2. Open a terminal or command prompt and navigate to the script's directory:

```bash
cd  Dalle-3-Unoffical-API
```

3. Run the script dalle3_arg.py with a query as an argument to download the generated images:

```bash
python3 dalle3_arg.py "your_search_query"
```

## Functionality

The DALL-E 3 Unofficial API provides the following functionality:,

### Image Search and Download

- The script opens the Bing Image Creator (DALL-E 3) in a headless Chrome browser.
- It adds a cookie to bypass any automation detection.
- Searches for images based on the provided query.
- Extracts and downloads image URLs.

## Output

The script will create a timestamped folder in the specified directory (usually the current working directory) containing downloaded images. The images will be named with the format "query (index).png." Additionally, the script logs information about the process.

You can look at this too:

```
query/
├─ 10-10-2023 12-24-03/
│  ├─ query (1).png
│  ├─ query (2).png
│  ├─ query (3).png
│  ├─ query (4).png
```

Please note that this is an unofficial API and may be subject to changes on the target website. Use it responsibly.
