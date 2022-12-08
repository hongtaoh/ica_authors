# ICA AUTHORS

This project contains my codes to scrape ICA Annaual conference data and also some exploratory codes about ICA journal data from web of science and also openalex. 

## TODO!

- In `2022-12-08-check-authors-without-only-initials.ipynb`, I found one author without first name. I need to remove that paper `10.1111/j.1460-2466.1980.tb02015.x` and the two authors
- There are 157 authors scattered in 70 papers whose first names are initials only. 

## Workflow

This project uses [snakemake](https://github.com/hongtaoh/snakemake-tutorial).
 
### Scripts

- `scrape_ica_paper_dois.py`: get ICA publication paper info, specifically, I got all paper dois, title, and abstracts

- `scrape_ica_author_data.py`: get paper and author data on ICA journal publications using BeautifulSoup

- `get_gender_race_aff_pred`: get predictions for gender, race, and affiliations

More details can be found in `workflow/Snakefile`.

## Notebooks

These are exploratory notebooks. 

## Data

- `interim/ica_paper_df.csv`, this file mainly contains dois for ica journal papers. I also included all other necessary information when it exists, for example, issue, and abstract. 

- `interim/ica_paper_data.csv`, this file is created when I scrape each paepr individually. It in fact does not contain any other useful information than in `ica_paper_df.csv`. It contains publication data, that might be the only useful thing. It only contains paperType but it seems all of them are 'ScholarlyArticle'. It also has 'keywords' but I am not sure where that data is from. 

