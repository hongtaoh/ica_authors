"""get author_with_pred, here, I simply re-arrange the column of author_with_pred_raw

"""

import sys
import pandas as pd

AUTHOR_WITH_PRED_RAW = sys.argv[1]
AUTHOR_WITH_PRED = sys.argv[2]

if __name__ == '__main__':
	author_with_pred_raw = pd.read_csv(AUTHOR_WITH_PRED_RAW)

	cols_to_keep = [
		'doi',
		'url',
		'year',
		'title',
		'journal',
		'authorFullName',
		'numberOfAuthors',
		'authorPosition',
		'genderize',
		'genderize_prob',
		'genderize_basedon',
		'genderAccuracy',
		'firstName',
		'lastName',
		'gscholarLink',
		'api',
		'black',
		'hispanic',
		'white',
		'race',
		'firstName',
		'lastName',
		'gscholarLink',
		'raceHighest',
		'raceSecondHighest',
		'raceDiff',
		'racePredAccuracy',
		'affProcessed',
		'affiliation',
		'ROR_AFFNAME',
		'matchMethod',
		'ROR_ID',
	]

	author_with_pred_raw[cols_to_keep].to_csv(
		AUTHOR_WITH_PRED, index=False)
