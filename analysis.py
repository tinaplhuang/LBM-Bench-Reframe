import pandas as pd

df = pd.read_csv('perflogs/generic/default/lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"])
#df = pd.read_csv('lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"])


cols = ["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"]
#these are the columns that we are reading from the performance log csv file


#data cleaning, taking unit, adding to column heading and deleting unit column
for i in range(1, len(cols), 2):
	df.rename(columns={f"{cols[i]}": f"{cols[i]} [{df.iloc[3, i+1]}]"}, inplace=True)

for i in range(len(cols), 1, -2):
	df.drop(f"{cols[i-1]}", axis=1, inplace=True)



pd.set_option('display.max_columns', None)
print("\n \n Individual Readings:")
print(df)

head = list(df) #getting a list of the new column headings
head = head[1:] #don't need job_completion_time in summary
mean = []
std = []
for i in range(len(head)):
	mean.append(df[f"{head[i]}"].mean())
	std.append(df[f"{head[i]}"].std())

d = {'Measurement': head, 'Mean': mean, 'SD': std}
sum = pd.DataFrame(data=d)
print("\n Summary Table:")
print(sum.round(4))

#^above is for single thread likwid-perfctr only, extra work required to scrape multiple outputs
#from multiple thread measurements
