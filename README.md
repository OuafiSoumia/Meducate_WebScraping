# Meducate_WebScraping

This project focuses on extracting, cleaning, and enriching data from online sources for analytical purposes. Below is a brief description of the files included in this project:

## ScrapCode.py

This file contains the scraping code that allows you to extract data from online sources(webScraping). To run this script, use the following command:

```bash
python main.py -t=10 -s='hopitaux marrakech'
```
- The -t argument lets you specify the number of data entries you want to extract.
- The -s argument allows you to set the search query for the data.

## DataClean.py
This file is meant to be used with Google Colab, an online notebook platform. It contains steps to clean the extracted data, especially for the name column. The goal is to remove unwanted words and put the data in a more consistent format.

## AddSentiment.py
This file, also designed to be used with Google Colab, aims to enrich the data. It adds a sentiment column (neutral, positive, negative) to each data entry based on associated comments.

The overall objective of this project is to gather relevant data, clean it for easier analysis, and enrich it with additional information .
