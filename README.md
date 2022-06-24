# Intro

This project contains my codes to scrape ICA Annaual conference data and also some exploratory codes about ICA journal data from web of science and also openalex. 

## Data

- `interim/ica_paper_df.csv`, this file mainly contains dois for ica journal papers. I also included all other necessary information when it exists, for example, issue, and abstract. 

- `interim/ica_paper_data.csv`, this file is created when I scrape each paepr individually. It in fact does not contain any other useful information than in `ica_paper_df.csv`. It contains publication data, that might be the only useful thing. It only contains paperType but it seems all of them are 'ScholarlyArticle'. It also has 'keywords' but I am not sure where that data is from. 

