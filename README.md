# Insight_challenge

This code analyze user input .csv file containing immigration data, calculate two metrics: Top 10 Occupations and Top 10 States for certified visa application, and generate the corresponding .txt result files.

The code reads in 1 .csv file format in the input folder. The columns in different .csv files do not have to match. The code only reads in columns with containing information regarding "STATUS", "OCCUPATION", and "EMPLOYER STATE"

The programing languge used is Python 3.7. The python code titled 'h1b_count-2.py' is located in the src folder.

Output: The code creates 2 output files in the output folder:
  top_10_occupations.txt
  top_10_states.txt
 Each .txt files contain information regarding the top 10 names, the number of certified visa status, and the percentage of application of occupational data or employer states' information in accordance to the .txt file name. Percentages were rounded off to 1 decimal place.
 
