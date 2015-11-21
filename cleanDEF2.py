import os
import csv
import numpy

# work=2
# business=3
# primary=4
# high=5
# tertiary=6
# shopping=7
# other=8
# listfiles=['/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/2036/Car_Passenger_Tours_2036_std.csv', '/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/2036/Ferry_Passenger_Tours_2036_std.csv', '/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/2036/LighRail_Passenger_Tours_2036_std.csv', '/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/2036/Rail_Passenger_Tours_2036_std.csv', '/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/2036/Taxi_Tours_2036_std.csv', 'Walk_Tours_2036_std.csv']
# ['Bicycle_Tours_2036_std.csv', 'Bus_Passenger_Tours_2036_std.csv', 'Car_Driver_Tours_2036_std.csv','Car_Passenger_Tours_2036_std.csv', 'Ferry_Passenger_Tours_2036_std.csv', 'LighRail_Passenger_Tours_2036_std.csv', 'Rail_Passenger_Tours_2036_std.csv', 'Taxi_Tours_2036_std.csv', 'Walk_Tours_2036_std.csv']
# listfiles =['CarSkims_PM_EV_2011_std.csv']

# file='/Users/hoecheeyam/Dropbox/ShareSGS-YHC/STM/Bus_Passenger_Tours_2036_std.csv'
##########deleting the fluff in the spreadsheet############
def createcsv(fileslist,column):
	arraysholder=[]
	f=2036
	for filename in fileslist:
		btsfile=csv.reader(open(filename,"r"),delimiter=",")
		btslist=[]
		for row in btsfile:
			btslist.append(row)

##find out number of rows to delete from top
		toppart = [i for i in range(len(btslist)) if '(p)' in btslist[i]]

		##check
		print(toppart)
		# [27]
		rowstodelete=toppart[0]+2
		
#delete the top rows
		deletetop_targetlen=len(btslist)-rowstodelete

		while len(btslist)>deletetop_targetlen:
			btslist.remove(btslist[0])

## check if the appropriate number of rows are deleted	
		print(btslist[0])
		# ['1', '2', '.000006', '.000003', '.000000', '.000000', '.000002', '.000000', '.000001', '']
		deletebtm_targetlen=len(btslist)-5

# delete the bottom 5 rows
		while len(btslist)>deletebtm_targetlen:
			btslist.remove(btslist[len(btslist)-1])

## check if the appropriate number of rows are deleted	
		print(btslist[len(btslist)-1])
		# ['3788', '3919', '.000000', '.000000', '.000000', '.000298', '.000000', '.000000', '.000000', '']
		##close file to fee up memory?
##########deleting the fluff in the spreadsheet############

		m4=numpy.zeros((4000, 4000))
		for r in range(len(btslist)-1):
			origin=int(btslist[r][0])
			dest=int(btslist[r][1])
			data=float(btslist[r][column])
			m4[origin][dest]=data
			# print(origin,dest,data,m4[origin][dest])
		
		#append each completed m4 int the arraysholder list
		arraysholder.append(m4)
	
		total=sum(arraysholder)	

		with open("result_"+str(f)+".csv", "w") as output:	
			writer = csv.writer(output,dialect='excel')
			writer.writerows(total)  
		output.close()
		m4=None
		f=f+5
		# btslist=None
		# matrix4000=None





