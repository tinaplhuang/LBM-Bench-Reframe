import pandas as pd

df = pd.read_csv('perflogs/generic/default/lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"])
#df = pd.read_csv('lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"])
#only difference between these lines are the filepath of the log

cols = ["job_completion_time", "runtime_bw_value", "runtime_bw_unit", "performance_bw_value", "performance_bw_unit", "bandwidth_bw_value", "bandwidth_bw_unit", "clockfreq_bw_value", "clockfreq_bw_unit", "accessbandwidth_bw_value", "accessbandwidth_bw_unit", "accessdatavolume_bw_value", "accessdatavolume_bw_unit", "accessrate_bw_value", "accessrate_bw_unit", "missrate_bw_value", "missrate_bw_unit", "missratio_bw_value", "missratio_bw_unit"]
#these are the columns that we are reading from the performance log csv file



d = {'Measurement': ['runtime[s]', 'performance [MFLUP/s]', 'bandwidth [GByte/s]', 'clockfreq [MHz]', 'accessbandwidth [MByte/s]', 'accessdatavolume [GBytes]', 'accessrate [%]', 'missrate [%]', 'missratio [%]'], "Mean": [df['runtime_bw_value'].mean(), df['performance_bw_value'].mean(), df['bandwidth_bw_value'].mean(), df['clockfreq_bw_value'].mean(), df['accessbandwidth_bw_value'].mean(), df['accessdatavolume_bw_value'].mean(), df['accessrate_bw_value'].mean(), df['missrate_bw_value'].mean(), df['missratio_bw_value'].mean()], 'SD:': [df['runtime_bw_value'].std(), df['performance_bw_value'].std(), df['bandwidth_bw_value'].std(), df['clockfreq_bw_value'].std(), df['accessbandwidth_bw_value'].std(), df['accessdatavolume_bw_value'].std(), df['accessrate_bw_value'].std(), df['missrate_bw_value'].std(), df['missratio_bw_value'].std()]}
#this above line could probably be automated with a loop

sum= pd.DataFrame(data=d)
sum = sum.round(4)
print("\n Summary Table:")
print(sum)


#data cleaning, taking unit, adding to column heading and deleting unit column

for i in range(1, len(cols), 2):
	df.rename(columns={f"{cols[i]}": f"{cols[i]} [{df.iloc[3, i+1]}]"}, inplace=True)

for i in range(len(cols), 1, -2):
	df.drop(f"{cols[i-1]}", axis=1, inplace=True)



pd.set_option('display.max_columns', None)
print("\n \n Individual Readings:")
print(df)

#^above is for single thread likwid-perfctr only, extra work required to scrape multiple outputs
#from multiple thread measurements
