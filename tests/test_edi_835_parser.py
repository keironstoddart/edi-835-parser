from tests.conftest import current_path

def test_claim_count(
		blue_cross_nc_sample,
		emedny_sample,
		all_samples,
):
	assert blue_cross_nc_sample.count_claims() == 1
	assert emedny_sample.count_claims() == 3
	assert all_samples.count_claims() == 4

def test_patient_count(
		blue_cross_nc_sample,
		emedny_sample,
		all_samples,

):
	assert blue_cross_nc_sample.count_patients() == 1
	assert emedny_sample.count_patients() == 3
	assert all_samples.count_patients() == 4

def test_to_dataframe(
		blue_cross_nc_sample,
		emedny_sample,
		all_samples,
):
	blue_cross_nc_sample.to_dataframe().to_csv(f'{current_path}/output/blue_cross_nc_sample.csv')
	emedny_sample.to_dataframe().to_csv(f'{current_path}/output/emedny_sample.csv')
	all_samples.to_dataframe().to_csv(f'{current_path}/output/all_samples.csv')
