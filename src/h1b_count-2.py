## H1B csv file processing
#   Quyen Do
#   10/26/2018


import csv

import os


current_dir = os.getcwd()
top_dir = os.path.dirname(os.getcwd())
file_to_process = []

## Find csv files in input dir
for file in os.listdir(current_dir + '/input'):
    if file.endswith('.csv'):
        file_to_process.append(file)
       
        
## Initialize lists,dicts
jobs = []
states = []
jobs_count = {}
states_count = {}

## open first csv file found in input dir    
os.chdir(top_dir + '/input')
print('Found file ' + file_to_process[0] )
    
with open(file_to_process[0], 'r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter =";")
    
    ## append jobs and states with 'certified' status     
    for i, line in enumerate(csv_reader):        
        if line['STATUS'] == 'CERTIFIED':
            jobs.append(line['LCA_CASE_SOC_NAME'])  
            states.append(line['LCA_CASE_EMPLOYER_STATE'])
            
##Sort top states
    print('Processing state data...')

    total_accepted_apps = len(states)
    
    for state in set(states): # for each unique state
        states_count[state] = states.count(state)

    popular_states = sorted(states_count.items(), key = lambda x: x[1], reverse = True)
    top_10_percent_states = dict(popular_states[:11])

    
    # Write to txt file
    with open (top_dir + '/output/'+'top_10_states.txt', 'w+') as state_file:
        state_file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        
        for state in top_10_percent_states:        
            top_10_percent_states[state] = (top_10_percent_states[state]/total_accepted_apps)*100   
            state_file.write(state + ';' + str(states_count[state]) +';' +str(("%.1f" % top_10_percent_states[state])) + '%\n')
       
    print('top_10_states.txt written to output directory')

               
    
##Sort top jobs    
    print('Processing occupation data...')
    
    for job in set(jobs): # for unique jobs
        jobs_count[job] = jobs.count(job)
       
    popular_jobs = sorted(jobs_count.items(), key = lambda x: x[1], reverse = True)
    top_10_percent_job = dict(popular_jobs[:11])
    
    with open (top_dir + '/output/'+'top_10_occupations.txt', 'w+') as occupation_file:
        occupation_file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        
        for job in top_10_percent_job:            
            top_10_percent_job[job] = (top_10_percent_job[job]/total_accepted_apps)*100
            occupation_file.write(job + ';' + str(jobs_count[job]) +';' +str(("%.1f" % top_10_percent_job[job])) + '%\n')
            
    print('top_10_occupations.txt written to output directory')
    
    
