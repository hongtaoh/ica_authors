"""combine initial and manually collected google scholar data """

import pandas as pd
import sys

GSCHOLAR_DATA = sys.argv[1]
GSCHOLAR_DATA_MANUAL_CHECKED = sys.argv[2]
GSCHOLAR_DATA_COMBINED = sys.argv[3]

if __name__ == '__main__':
	df1 = pd.read_csv(GSCHOLAR_DATA)
	df2 = pd.read_csv(GSCHOLAR_DATA_MANUAL_CHECKED)
	df2_dois = list(set(df2.DOI))
	title_same = df1.query('DOI != @df2_dois')
	df = pd.concat([title_same, df2], axis = 0)
	df.to_csv(GSCHOLAR_DATA_COMBINED, index = False)

