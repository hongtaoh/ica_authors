# ICA AUTHORS

This project contains my codes to scrape ICA Annaual conference data and also some exploratory codes about ICA journal data from web of science and also openalex. 

## TODO!

- In `2022-12-08-check-authors-without-only-initials.ipynb`, I found one author without first name. I need to remove that paper `10.1111/j.1460-2466.1980.tb02015.x` and the two authors
- There are 157 authors scattered in 70 papers whose first names are initials only.

## Google scholar data

I scraped citation data from Google Scholar. I queried title + journal + first author name. I then compared the original title and the title shown on Google Scholar to make sure my data is accurate. Among all 5,718 papers, only 293 papers have differences in titles. I then investigated these 293 papers. I compared the similarity (using python's difflib) between the two titles. More than half of them have a similarity score of 0.95. For these, I considered them as accurate. For the 122 papers, I collected their data on Google Scholar by searching their DOIs (instead of titles). In this case, searching by DOI yeilds a much better result (`data/interim/gscholar_data_manual.csv`). Still, there are some mismatches. I updated this dataset in https://docs.google.com/spreadsheets/d/14y72p5I9RvzueNOb5x1cE23M0N__A8rCaCRudckxU5U/edit#gid=1256132535. The resulting data is `interim/gscholar_data_manual_checked.csv`

Then, I combined the two datasets through `combine_gscholar_data.py`

>I thought about redoing scraping google scholar citation data by searching the DOI (right now, the majority of the data came from searching the title). However, after checking the result of data now (trying searching DOI for papers with strings like `[PDF]` and `CITATION`), I found that they are the same. So I probably won't do it again; I'll keep the data for now for my analysis.   

## Limitations 

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

