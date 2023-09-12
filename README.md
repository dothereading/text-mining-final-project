# Trending Topics in Towards Data Science Articles from 2017-2023

In this project, we scraped the website Towards Data Science to construct a novel dataset of all 55,000 articles published since the website’s founding in 2016. Using LDA, we modeled 10 general categories of topics discussed on the website. Using the TF-IDF score, we charted the popularity of specific topics over time and extracted words associated with the “hot” topics for each month. Using linear and random forest regression, we observed a positive relationship between article length and engagement as measured in claps. Coefficients on an article’s top topic were significant but difficult to interpret.

## Key Files

* `new-tds-scrape-all-days.ipynb` scrapes all articles from Towards Data Science for specified years producing a csv of the form: all_articled_20**_20**.csv,

* `Analysis.ipynb` runs through the analysis of the data,
 
* `finalreport.pdf` explains our methodology and results.
