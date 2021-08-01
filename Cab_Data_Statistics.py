import xlrd
workbook = xlrd.open_workbook('Dataset.xls')
i=0
#List of Cities
city = [str(workbook.sheet_by_index(0).cell_value(i,0)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,0))]
city.remove(city[0])
city.remove("City")
city.remove(city[-1])

#List of Total Sum of KM Traveled by Pink Cab in Cities
pink_sumKM = [str(workbook.sheet_by_index(0).cell_value(i,1)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,1))]
pink_sumKM.remove(pink_sumKM[0])
pink_sumKM.remove(pink_sumKM[0])
pink_sumKM.remove(pink_sumKM[-1])

#List of Average KM Traveled by Pink Cab in a City per Ride
pink_avgKM = [str(workbook.sheet_by_index(0).cell_value(i,2)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,2))]
pink_avgKM.remove(pink_avgKM[0])
pink_avgKM.remove(pink_avgKM[0])
pink_avgKM.remove(pink_avgKM[-1])

#List of Average Price Charged by Pink Cab in a City per Ride
pink_avgP = [str(workbook.sheet_by_index(0).cell_value(i,3)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,3))]
pink_avgP.remove(pink_avgP[0])
pink_avgP.remove(pink_avgP[0])
pink_avgP.remove(pink_avgP[-1])

#List of Average Cost of Ride by Pink Cab in a City
pink_avgC = [str(workbook.sheet_by_index(0).cell_value(i,4)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,4))]
pink_avgC.remove(pink_avgC[0])
pink_avgC.remove(pink_avgC[0])
pink_avgC.remove(pink_avgC[-1])

#List of Total Sum of Profit Earned from Each Ride by Pink Cab in a City
pink_sumP = [str(workbook.sheet_by_index(0).cell_value(i,5)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,5))]
pink_sumP.remove(pink_sumP[0])
pink_sumP.remove(pink_sumP[0])
pink_sumP.remove(pink_sumP[-1])

#List of Total Sum of KM Traveled by Yellow Cab in Cities
yellow_sumKM = [str(workbook.sheet_by_index(0).cell_value(i,6)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,6))]
yellow_sumKM.remove(yellow_sumKM[0])
yellow_sumKM.remove(yellow_sumKM[0])
yellow_sumKM.remove(yellow_sumKM[-1])

#List of Average KM Traveled by Yellow Cab in a City per Ride
yellow_avgKM = [str(workbook.sheet_by_index(0).cell_value(i,7)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,7))]
yellow_avgKM.remove(yellow_avgKM[0])
yellow_avgKM.remove(yellow_avgKM[0])
yellow_avgKM.remove(yellow_avgKM[-1])

#List of Average Price Charged by Yellow Cab in a City per Ride
yellow_avgP = [str(workbook.sheet_by_index(0).cell_value(i,8)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,8))]
yellow_avgP.remove(yellow_avgP[0])
yellow_avgP.remove(yellow_avgP[0])
yellow_avgP.remove(yellow_avgP[-1])

#List of Average Cost of Ride by Yellow Cab in a City
yellow_avgC = [str(workbook.sheet_by_index(0).cell_value(i,9)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,9))]
yellow_avgC.remove(yellow_avgC[0])
yellow_avgC.remove(yellow_avgC[0])
yellow_avgC.remove(yellow_avgC[-1])

#List of Total Sum of Profit Earned from Each Ride by Yellow Cab in a City
yellow_sumP = [str(workbook.sheet_by_index(0).cell_value(i,10)) for i in range(workbook.sheet_by_index(0).nrows) if not 'module' in str(workbook.sheet_by_index(0).cell_value(i,10))]
yellow_sumP.remove(yellow_sumP[0])
yellow_sumP.remove(yellow_sumP[0])
yellow_sumP.remove(yellow_sumP[-1])