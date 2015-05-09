import csv

#will get all the data that is in 
#the csv file, some of this data may
#be used and may not be.
def get_all_data(input_file):

	csv_file = open(input_file) 
	data = csv.DictReader(csv_file)
	store = {}

	for row in data:

		for key in row.keys():
			
			try:
				store[key].append(row[key])
			except KeyError:
				store[key] = [row[key]] 

	return store

#this is used to get a list of indices of
#a given attribute and given item of that 
#attribute.
#Example: All the indices of where Kobe Bryant
#occurs, Key = 'Player', Query = 'Kobe Bryant'
def get_index(data,key,query):
	pos = []
	for val in range(len(data[key])):
		if data[key][val] == query:
			pos.append(val)
	return pos

#returns a dictionary of a specific targeted data
#this can be a specific season's data, or specific
#player stats etc.
def get_specific_data(data,att,query):

	specific_info = {}

	#all the index positions of given player
	pos = get_index(data,att,query)

	for i in pos:

		for key in data.keys():

			try:
				specific_info[key].append(data[key][i])
			except KeyError:
				specific_info[key] = [data[key][i]]
	return specific_info

#returns data for a player from a specific season
def get_player_season(data,player,season):

	return get_specific_data(get_specific_data(data,'Player',player),'Season',season)

#returns data for a team from a specific season 
def get_team_season(data,team,season):
	return get_specific_data(get_specific_data(data,'Tm',team),'Season',season)

#returns unique row and column keys 
def create_keys(data, row, col):
	
	#create lists containing unique keys, row and column
	unique_row = sorted(list(set(data[row])))
	unique_col = sorted(list(set(data[col])))
	
	return [unique_row, unique_col]	

#sort the rows of pivot table by the number of empty elements in each row
def sort_pvt_vals(pvt_vals):
	return sorted(pvt_vals, key=lambda x:len(([num for num in x[1] if num < 0])))

#create a table of aggregation values
def get_pvt_vals(data, row, col, val, mode, unique_row, unique_col):

	#create a list containing values of aggregation corresponding to unique_row and unique_col
	pvt_vals = [] 
	#used for sorting
	count = 0

	for row_item in unique_row:
		 
		temp_row = []

		for col_item in unique_col:
			
			#get a list of values corresponding to row and column
			needed_data = get_specific_data(get_specific_data(data, row, row_item), col, col_item)
			
			if(needed_data):
				
				#calculate sum of values in the list
				tot = sum(map(int,needed_data[val]))
				
				#sum mode
				if mode == "SUM":
					
					temp_row.append(tot)
					
				#average mode
				else:
					
					average = int(tot / float(len(needed_data[val])))
					temp_row.append(average)

			#for blank cell 
			else:

				temp_row.append(-1)
			
		pvt_vals.append((count, temp_row))
		count += 1
			
	return sort_pvt_vals(pvt_vals)

#returns string of html coding a pivot table
def create_table_str(pvt_vals, unique_row):
	
	table_str = '<tbody>\n'

	for index in range(len(pvt_vals)):

		table_str += '<tr>\n<td>%d</td>\n<td>%s</td>\n'%(pvt_vals[index][0], unique_row[pvt_vals[index][0]])

		for item in pvt_vals[index][1]:

			if(item >= 0):			
				table_str += '<td>%d</td>\n'%(item)
			else:
				table_str += '<td></td>\n'

	table_str += '</tbody>\n'
  
	return table_str

