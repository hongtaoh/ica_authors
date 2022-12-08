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

(More details can be found in `workflow/Snakefile` and also in each specific `py` file)

- `scrape_ica_paper_dois.py`: get ICA publication paper info, specifically, I got all paper dois, title, and abstracts

- `scrape_ica_author_data.py`: get paper and author data on ICA journal publications using BeautifulSoup

- `get_author_with_gender.py`: get gender raw predictions. This is to prevent me from having to do it again, which requires quota from genderize.io.

- `get_author_with_pred_raw.py`: get race and affiliations. "Raw" because I'll change column order later

- `get_author_with_pred.py`: rearrange colomn order

- `get_paper_and_author_with_type.py`: add 'type' to paper df and author data, and subsequently get research paper/author, and authors/papers to study. 

- `get_authorid_with_vars.py`: in this script, I processed the gender, race and aff coded data
and return basically dictionaries through a dataframe. 

- `get_authors_and_papers_expanded.py`: get all variables needed in analysis.

- `get_gscholar_data.py` and `get_gscholar_data_combined.py`: get gscholar data.

## Notebooks

These are exploratory notebooks. 

## Data

## Raw

`to_delete_dois.csv`: these are the non-research papers that I need to delete. The categories that they belong to are considered to be "research", just that they are the first papers that introduce other papers in the issue and therefore should be deleted. 

`category-classification.csv` is the result category classification directly from Google Sheet. 

### Interim

- `interim/ica_paper_df.csv`, this file mainly contains dois for ica journal papers. I also included all other necessary information when it exists, for example, issue, and abstract. 

- `interim/ica_paper_data.csv`, this file is created when I scrape each paepr individually. It in fact does not contain any other useful information than in `ica_paper_df.csv`. It contains publication data, that might be the only useful thing. It only contains paperType but it seems all of them are 'ScholarlyArticle'. It also has 'keywords' but I am not sure where that data is from. 

### Processed

I first get AUTHOR_WITH_PRED. Then the following:

- ICA_PAPER_DF_WITH_TYPE, type means research paper or not
- AUTHOR_WITH_PRED_WITH_TYPE, type means research paper or not
- RESEARCH_PAPER_DF, papers that are research papers
- RESEARCH_AUTHOR_WITH_PRED, authors of research papers with all kinds of predictions (race, gender, aff)
- AUTHORS_TO_STUDY, this is different from research authors because i removed thos research papers whose affiliaiton is nan
- DOIS_TO_STUDY, research papers with valid aff information
- PAPERS_TO_STUDY, research papers with valid affiliation information

Then, after all the manual coding is done (race, gender, and aff), I generated AUTHORID_WITH_VARS, i.e., author ID with the associated aff country, aff type, gender, and race. 

Finally, I generated

- AUTHORS_TO_STUDY_EXPANDED,
- PAPERS_TO_STUDY_EXPANDED,

Those two files are the most complete ones. 

- GSCHOLAR_DATA_COMBINED, this is the final google scholar data. For details of how I got this data, see the section of "Google scholar data"



