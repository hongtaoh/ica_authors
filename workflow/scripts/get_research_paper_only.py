"""with this script, I tries to get two files: ica_paepr_df_with_type, and 
	research_author_with_pred. The first one adds one column to the original ica_paper_df,
	i.e., type ('R' (research), or 'M' (Miscellaneous))

	The research_author_with_pred is only a subset of the original author_with_pred. I 
	only chose those who wrote research papers. 

"""

import sys
import pandas as pd
import numpy as np
import re 

CAT_CLASSIFICATION = sys.argv[1]
TO_DELETE_DOIS = sys.argv[2]
ICA_PAPER_DF = sys.argv[3]
AUTHOR_WITH_PRED = sys.argv[4]

ICA_PAPER_DF_WITH_TYPE = sys.argv[5]
RESEARCH_AUTHOR_WITH_PRED = sys.argv[6]

if __name__ == '__main__':
	### categories to exclude
	cat_df = pd.read_csv(CAT_CLASSIFICATION)[
		['category', 'issueURL', 'TO_EXCLUDE']
	]
	to_exclude_cat = cat_df[cat_df.TO_EXCLUDE == True][
		'category']
	num_to_exclude_cat = len(to_exclude_cat)
	print(f'There are {num_to_exclude_cat} categories to exclude.')

	### dois to exclude
	to_exclude_dois = pd.read_csv(TO_DELETE_DOIS, header=None).iloc[:, 0]
	to_exclude_dois = [
		re.sub('https://doi.org/', '', x) for x in to_exclude_dois]
	print(f'There are {len(to_exclude_dois)} dois to exclude')

	### Process papers
	papers = pd.read_csv(ICA_PAPER_DF)
	papers['type'] = np.where(
		(papers.category.isin(to_exclude_cat)) | (papers.doi.isin(to_exclude_dois)
			), 
		'M', 
		'R')
	print(f'papers shape: {papers.shape}')
	research_papers = papers[papers.type == 'R']
	print(f'research papers shape: {research_papers.shape}')
	papers.to_csv(ICA_PAPER_DF_WITH_TYPE, index=False)

	### Process authors
	research_paper_dois = research_papers.doi 
	authors = pd.read_csv(AUTHOR_WITH_PRED)
	print(f'Authors shape: {authors.shape}')
	research_authors = authors[authors.doi.isin(research_paper_dois)]
	print(f'Research authors shape: {research_authors.shape}')
	research_authors.to_csv(
		RESEARCH_AUTHOR_WITH_PRED, index=False)
	