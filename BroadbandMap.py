#! /usr/bin/env python3

import json
import requests

class BroadbandMapData(object):
    """
    Bundling Broadband Map API data and methods
    """
    def __init__(self, State):
        """
        Initialize state, FIPS ID, and Demographics fields
        """
        self.state = State
        self.FIPS = self.getFIPS(self.state)
        self.demographics = self.getDemographics(self.FIPS)

    def getFIPS(self, State):
        """
        get FIPS ID per State
        """
        stateQuery = "https://www.broadbandmap.gov/broadbandmap/census/state/" + str(State) + "?&all=true&format=json"
        stateData = requests.get(stateQuery).json()
        FIPS = stateData['Results']['state'][0]['fips']
        return FIPS

    def getDemographics(self, FIPS):
        """
        get specific demographics per State / FIPS ID
        """

        demographicsQuery = "https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/" + str(FIPS) + "?format=json"
        demographicsData = requests.get(demographicsQuery).json()

        demographics = dict([('stateName',demographicsData['Results'][0]['geographyName']), \
                             ('population',demographicsData['Results'][0]['population']), \
                             ('households',demographicsData['Results'][0]['households']), \
                             ('incomeBelowPoverty',demographicsData['Results'][0]['incomeBelowPoverty']), \
                             ('medianIncome',demographicsData['Results'][0]['medianIncome'])])

        return demographics
