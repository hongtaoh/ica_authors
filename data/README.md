# DATA

## Raw

`to_delete_dois.csv`: these are the non-research papers that I need to delete. The categories that they belong to are considered to be "research", just that they are the first papers that introduce other papers in the issue and therefore should be deleted. 

`category-classification.csv` is the result category classification directly from Google Sheet. 

## Processed

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

### Google scholar data

I scraped citation data from Google Scholar. I queried title + journal + first author name. I then compared the original title and the title shown on Google Scholar to make sure my data is accurate. Among all 5,718 papers, only 294 papers have differences in titles. I then investigated these 294 papers. I compared the similarity (using python's difflib) between the two titles. More than half of them have a similarity score of 0.95. For these, I considered them as accurate. For the 123 papers, I decided to collect their data manually. 