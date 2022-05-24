from tests.conftest import current_path

def test_claim_count(
		blue_cross_nc_sample,
		emedny_sample,
		united_healthcare_legacy_sample,
		all_samples,
):
	assert blue_cross_nc_sample.count_claims() == 1
	assert united_healthcare_legacy_sample.count_claims() == 2
	assert emedny_sample.count_claims() == 3
	assert all_samples.count_claims() == 6

def test_patient_count(
		blue_cross_nc_sample,
		emedny_sample,
		united_healthcare_legacy_sample,
		all_samples,

):
	assert blue_cross_nc_sample.count_patients() == 1
	assert united_healthcare_legacy_sample.count_patients() == 2
	assert emedny_sample.count_patients() == 3
	assert all_samples.count_patients() == 6

def test_to_dataframe(
		blue_cross_nc_sample,
		emedny_sample,
		united_healthcare_legacy_sample,
		all_samples,
):
	payment = blue_cross_nc_sample.sum_payments()
	blue_cross_nc_data = blue_cross_nc_sample.to_dataframe()

	assert payment == blue_cross_nc_data['paid_amount'].sum()

	blue_cross_nc_data.to_csv(f'{current_path}/output/blue_cross_nc_sample.csv')

	payment = emedny_sample.sum_payments()
	emedny_data = emedny_sample.to_dataframe()

	assert payment == emedny_data['paid_amount'].sum()

	emedny_data.to_csv(f'{current_path}/output/emedny_sample.csv')

	payment = united_healthcare_legacy_sample.sum_payments()
	united_healthcare_legacy_ = united_healthcare_legacy_sample.to_dataframe()

	assert payment == united_healthcare_legacy_['paid_amount'].sum()

	united_healthcare_legacy_.to_csv(f'{current_path}/output/united_healthcare_legacy_sample.csv')

	payment = all_samples.sum_payments()
	all_data = all_samples.to_dataframe()

	assert payment == all_data['paid_amount'].sum().round(2)

	all_data.to_csv(f'{current_path}/output/all_samples.csv')
