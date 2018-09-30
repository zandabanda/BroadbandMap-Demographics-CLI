#! /usr/bin/env python3

import sys
import csv
from BroadbandMap import BroadbandMapData

states = str(sys.argv[1])                   # CLI input
outFormat = str(sys.argv[2])

def main():

    listStates = states.split(",")          # convert comma separated string to list of strings
    listStates.sort()                       # alphabetize
    listFIPS = []
    listDemographics = [['State Name', ' Population', ' Households', ' Income Below Poverty', ' Median Income']]    # CSV header
    listIncomeBelowPoverty = []

    num_States = len(listStates)

    for state in listStates:
        broadbandmapData = BroadbandMapData(state)                                              # initialize class for each State
        listFIPS.append(broadbandmapData.FIPS)                                                  # generate list of FIPS ID's
        listDemographics.append([broadbandmapData.demographics['stateName'], \
                                 " " + str(broadbandmapData.demographics['population']), \
                                 " " + str(broadbandmapData.demographics['households']), \
                                 " " + str(broadbandmapData.demographics['incomeBelowPoverty']), \
                                 " " + str(broadbandmapData.demographics['medianIncome'])])
        listIncomeBelowPoverty.append(broadbandmapData.demographics['incomeBelowPoverty'])      # generate list of Incomes below Poverty

    if outFormat == 'CSV':                                                                      # create CSV file
        with open('demographics.csv', 'w') as outfile:
            csvWriter = csv.writer(outfile)                                                     # writer handles formatting
            csvWriter.writerows(listDemographics)

    elif outFormat == 'averages':                                                               # calculate simple average 
        averageIncomeBelowPoverty = sum(listIncomeBelowPoverty)/num_States
        print("Average Income Below Poverty: ", averageIncomeBelowPoverty)



if __name__ == "__main__":
    main()
