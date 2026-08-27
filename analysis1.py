import pandas as pd

#with open('lbm_test.log', "r") as f:
#	reader = csv.reader(f, delimiter = "|")
#	data = list(reader)
#	row_count = len(data)


df = pd.read_csv('perflogs/generic/default/lbm_test.log', sep = '|', usecols=["job_completion_time", "runtime_bw_value", "performance_bw_value", "bandwidth_bw_value", "clockfreq_bw_value", "accessbandwidth_bw_value", "accessdatavolume_bw_value", "accessrate_bw_value", "missrate_bw_value", "missratio_bw_value"])
#df = d.fillna("x").astype(str)

#print(f"runtime: mean={df['runtime_bw_value'].mean()}s sd={df['runtime_bw_value'].std()}")
#print(f"performance: mean={df['performance_bw_value'].mean()}MFLUP/s sd={df['performance_bw_value'].std()}")
#print(f"bandwidth: mean={df['bandwidth_bw_value'].mean()}GByte/s sd={df['bandwidth_bw_value'].std()}")
#print(f"clockfreq: mean={df['clockfreq_bw_value'].mean()}MHz sd={df['clockfreq_bw_value'].std()}")
#print(f"accessbandwidth: mean={df['accessbandwidth_bw_value'].mean()}MBytes/s sd={df['accessbandwidth_bw_value'].std()}")
#print(f"accessdatavolume: mean={df['accessdatavolume_bw_value'].mean()}GBytes sd={df['accessdatavolume_bw_value'].std()}")
#print(f"accessrate: mean={df['accessrate_bw_value'].mean()}% sd={df['accessrate_bw_value'].std()}")
#print(f"missrate: mean={df['missrate_bw_value'].mean()}% sd={df['missrate_bw_value'].std()}")
#print(f"missratio: mean={df['missratio_bw_value'].mean()}% sd={df['missratio_bw_value'].std()}")

d = {'Measurement': ['runtime[s]', 'performance [MFLUP/s]', 'bandwidth [GByte/s]', 'clockfreq [MHz]', 'accessbandwidth [MByte/s]', 'accessdatavolume [GBytes]', 'accessrate [%]', 'missrate [%]', 'missratio [%]'], "Mean": [df['runtime_bw_value'].mean(), df['performance_bw_value'].mean(), df['bandwidth_bw_value'].mean(), df['clockfreq_bw_value'].mean(), df['accessbandwidth_bw_value'].mean(), df['accessdatavolume_bw_value'].mean(), df['accessrate_bw_value'].mean(), df['missrate_bw_value'].mean(), df['missratio_bw_value'].mean()], 'SD:': [df['runtime_bw_value'].std(), df['performance_bw_value'].std(), df['bandwidth_bw_value'].std(), df['clockfreq_bw_value'].std(), df['accessbandwidth_bw_value'].std(), df['accessdatavolume_bw_value'].std(), df['accessrate_bw_value'].std(), df['missrate_bw_value'].std(), df['missratio_bw_value'].std()]}

sum= pd.DataFrame(data=d)
sum = sum.round(4)
print("\n Summary Table:")
print(sum)


df.rename(columns={'runtime_bw_value': 'runtime [s]'}, inplace=True)
df.rename(columns={'performance_bw_value': 'performance [MFLUP/s]'}, inplace=True)
df.rename(columns={'bandwidth_bw_value': 'bandwidth [GByte/s]'}, inplace=True)
df.rename(columns={'clockfreq_bw_value': 'clockfreq [MHz]'}, inplace=True)
df.rename(columns={'accessbandwidth_bw_value': 'accessbandwidth [MBytes/s]'}, inplace=True)
df.rename(columns={'accessdatavolume_bw_value': 'accessdatavolume [GBytes]'}, inplace=True)
df.rename(columns={'accessrate_bw_value': 'accessrate [%]'}, inplace=True)
df.rename(columns={'missrate_bw_value': 'missrate [%]'}, inplace=True)
df.rename(columns={'missratio_bw_value': 'missratio [%]'}, inplace=True)


pd.set_option('display.max_columns', None)
print("\n \n Individual Readings:")
print(df)

#^above is for single thread likwid-perfctr only
