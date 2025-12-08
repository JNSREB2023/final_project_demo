# from final_project_demo import cleaning


# def test_cleaning_pipeline_calls_merge_and_prints(monkeypatch, capsys):
# 	# Patch pandas.read_csv used in the pipeline to avoid file I/O
# 	import pandas as pd

# 	def fake_read_csv(path):
# 		return pd.DataFrame()

# 	monkeypatch.setattr(cleaning.pd, "read_csv", fake_read_csv)

# 	# Patch merge_data to simulate behavior and print the expected message
# 	def fake_merge(sensor_avgs, states_df):
# 		print("Running cleaning pipeline...")
# 		return "merged-result"

# 	monkeypatch.setattr(cleaning, "merge_data", fake_merge)

# 	result = cleaning.cleaning_pipeline()

# 	captured = capsys.readouterr()
# 	assert "Running cleaning pipeline..." in captured.out
# 	assert result == "merged-result"
