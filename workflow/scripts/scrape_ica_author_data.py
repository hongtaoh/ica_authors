"""get paper and author data on ICA journal publications using BeautifulSoup"""

import sys
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import random
import time 
import requests
import re
import json

ICA_PAPER_DF = sys.argv[1]
ICA_PAPER_DATA = sys.argv[2]
ICA_AUTHOR_DATA = sys.argv[3]
ICA_ERROR_URLS = sys.argv[4]

def get_response(url, idx):
	headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36" \
	"(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
	}
	response = requests.get(url=url, headers=headers)
	while response.status_code != 200:
		time.sleep(1)
		print(f"{idx} : {url} status code is {response.status_code}, retrying ...")
		response = requests.get(url=url, headers=headers)
	return response 

def get_j(response):
	html = response.text 
	soup = BeautifulSoup(html, 'html.parser')
	try:
		string = soup.select_one(
			"script[type='application/ld+json']"
		).string.strip()

		j = json.loads(string)
	except:
		j = None
	return j 

def update_paper_data_tuples(doi, url, year, idx, j, paper_data_tuples):
	title = j['name']
	paper_type = j['@type']
	journal = j['isPartOf']['isPartOf']['name'] or np.nan
	date_published = j['datePublished']
	try:
		keywords_list = j['keywords']
		keywords = ", ".join(keywords_list)
	except:
		keywords = np.nan
		# print(f"there are no keywords in {idx} : {url}")
	paper_data_tuples.append((doi, url, year, title, paper_type, journal, date_published, keywords))
	return paper_data_tuples

def update_author_data_tuples(doi, url, year, idx, j, author_data_tuples):
	journal = j['isPartOf']['isPartOf']['name'] or np.nan
	date_published = j['datePublished'] or np.nan
	title = j['name'] or np.nan
	
	try:
		authors = j['author']
		author_num = len(authors)
	except:
		# print(f"there is no author data in {idx} : {url}")
		authors = None
		author_num = None
		name = np.nan; aff = np.nan; author_type = np.nan
	# if there is no author data, I don't need to proceed here
	if authors is not None:
		for author in authors:
			position = authors.index(author) + 1
			try:
				"""
				authors[0]['name'] returns last, and then first.
				one example: 'Read, Stephen J.'
				so I need to reverse the order
				"""
				name_elements = author['name'].split(', ')
				name_elements.reverse()
				fullname = ' '.join(name_elements)
				fullname_split = fullname.split(' ')
				lastname = fullname_split[-1]
				if fullname_split:
					if len(fullname_split) == 2:
						firstname = fullname_split[0]
					# e.g., "M. J. Clarke"
					elif len(fullname_split) > 2 and len(fullname_split[0]) <= 2 and len(fullname_split[1]) <= 2:
						firstname = fullname_split[0]
					# e.g., "M. Jennifer Clarke"
					elif len(fullname_split) > 2 and len(fullname_split[0]) <= 2 and len(fullname_split[1]) > 2:
						firstname = fullname_split[1]
					# g.g., "Mike John Clarke"
					elif len(fullname_split) > 2 and len(fullname_split[0]) > 2:
						firstname = fullname_split[0]
					else:
						firstname = 'ERROR!'
			except:
				fullname = np.nan
				lastname = np.nan 
				firstname = np.nan 
			try:
				aff = author['affiliation']
			except:
				aff = np.nan
			author_data_tuples.append((
				doi, url, year, title, 
				journal, date_published, 
				fullname, firstname, lastname, 
				author_num, position, aff))
	else:
		author_data_tuples.append((
				doi, url, year, title, journal, date_published))
	return author_data_tuples

if __name__ == '__main__':
	ica_papers = pd.read_csv(ICA_PAPER_DF)
	paper_urls = ica_papers.url.tolist()
	paper_dois = ica_papers.doi.tolist()
	years = ica_papers.year.tolist()
	url_doi_dic = dict(zip(paper_urls, paper_dois))
	ulr_year_dic = dict(zip(paper_urls, years))
	# 188, 1459 have some problems. You can check them out
	random_paper_urls = random.sample(paper_urls, 10)
	error_urls = []

	paper_data_tuples = []
	author_data_tuples = []
	
	total_urls = len(paper_urls)
	print(f'Total number of URLs to crawl: {total_urls}')

	# for url in random_paper_urls:
	# 	idx = random_paper_urls.index(url) + 1
	for url in paper_urls:
		idx = paper_urls.index(url) + 1
		doi = url_doi_dic[url]
		year = ulr_year_dic[url]
		response = get_response(url, idx)
		j = get_j(response)
		if j is not None:
			update_paper_data_tuples(doi, url, year, idx, j, paper_data_tuples)
			update_author_data_tuples(doi, url, year, idx, j, author_data_tuples)
		else:
			print(f'something wrong with {idx} : {url}')
			paper_data_tuples.append((doi, url, year))
			author_data_tuples.append((doi, url, year))
			error_urls.append(url)
		print(f'{idx} is done')
		time.sleep(0.5 + random.uniform(0, 0.4))

	paper_data = pd.DataFrame(
		list(paper_data_tuples),
		columns = [
			'doi',
			'url',
			'year',
			'title',
			'paperType',
			'journal',
			'datePublished',
			'keywords'
		]
	)

	author_data = pd.DataFrame(
		list(author_data_tuples),
		columns = [
			'doi',
			'url',
			'year',
			'title',
			'journal',
			'datePublished',
			'authorFullName',
			'firstName',
			'lastName',
			'numberOfAuthors',
			'authorPosition',
			'affiliation',
		]
	)

	paper_data.to_csv(ICA_PAPER_DATA, index=False)
	author_data.to_csv(ICA_AUTHOR_DATA, index=False)
	with open(ICA_ERROR_URLS, 'w') as f:
		for url in error_urls:
			f.write("%s\n" % url)
