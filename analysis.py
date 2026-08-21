import pandas as pd


#This file does some work to format the raw csv file
#and ensure units are readable

#this should be saved in perflogs/generic/default alongside lbm_test.log



#with open('lbm_test.log', "r") as f:
#	reader = csv.reader(f, delimiter = "|")
#	data = list(reader)
#	row_count = len(data)


df = pd.read_csv('perflogs/generic/default/lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"])
#reading default csv


df2 = pd.DataFrame()
#empty dataframe to store the concatenated columns

df1 = df.fillna("x").astype(str)
#edited default dataframe so .astype(str) doesn't throw error with NaN

df2["runtime"] = df1["runtime_bw_value"].astype(str) + df1["runtime_bw_unit"]

df2["performance"] = df1["performance_bw_value"].astype(str) + df1["performance_bw_unit"]

df2["bandwidth"] = df1["bandwidth_bw_value"].astype(str) + df1["bandwidth_bw_unit"]

df2["clock_freq"] = df1["clockfreq_bw_value"].astype(str) + df1["clockfreq_bw_unit"]

df2["access_data_volume"] = df1["accessdatavolume_bw_value"].astype(str) + df1["accessdatavolume_bw_unit"]

df2["access_rate"] = df1["accessrate_bw_value"].astype(str) + df1["accessrate_bw_unit"]

df2["miss_rate"] = df1["missrate_bw_value"].astype(str) + df1["missrate_bw_unit"]

df2["miss_ratio"] = df1["missratio_bw_value"].astype(str) + df1["missratio_bw_unit"]

pd.set_option('display.max_columns', None)
#so all columns are shown instead of first last and ...
print(df2)

#^above is for single thread likwid-perfctr only
#format for output from multiple threads still needs work
