import pandas as pd

#prepare short list of GP-practices
gp_counts = pd.read_csv('http://digital.nhs.uk/media/29065/Numbers-of-Patients-Registered-at-a-GP-Practice-July-2016-GP/Any/gp-reg-patients-prac-quin-age.csv').rename(columns=lambda x: x.strip())

gp_counts.practice=gp_counts.GP_PRACTICE_CODE.astype('str')
reduction = 0.05 #5%
x =int(len(gp_counts.practice) * reduction) 
sub_df = gp_counts.ix[0:x].copy(deep=True)

cols2 = ['sha', 'pct', 'practice', 'bnf_code', 'bnf_name', 'items', 'nic', 'act_cost', 'quantity', 'period']
path = 'http://datagov.ic.nhs.uk/presentation/'


#generate filenames
prefixes=[]
files=[]

import calendar
for year in range(2014,2017):
    for i in range(1,13):
        prefixes.append(str(year) +'_' +str(i).zfill(2) + '_' + calendar.month_name[i] + '/')
        files.append('T' + str(year) +str(i).zfill(2) + 'PDPI+BNFT.CSV')

  
#read files and reduce size

def file_reduction(prefix, file):
    df =  pd.read_csv(path + prefix +file, header=None, names=cols2, index_col=False, skiprows=1).rename(columns=lambda x: x.strip())
    df.practice=df.practice.astype('str')
    df_small= df[(df['practice'].isin(sub_df['GP_PRACTICE_CODE']) == True)] #only proportion of entire dataset
    df_small.to_csv('N:\\Work\\DMHR2017-18\\visualization\\data\\' + file)
    del df #make space in memory
    return None
    
    
for prefix, file in zip(prefixes,files):
    print(path + prefix +file)
    file_reduction(prefix, file)
    


    
