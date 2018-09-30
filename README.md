---------------------------------------------------------------
National Broadband Map API
---------------------------------------------------------------
 * CLI for gathering National Broadband Map API demographic data on US states
 * Built with Python3

---------------------------------------------------------------
Prerequisites / Installation
---------------------------------------------------------------
* Python 3 must be installed in your environment
  * Please use your standard package manager - e.g. Mac OS 'brew install python3'
* Additional packages required: json, requests - e.g. 'python3 -m pip3 install <json|requests>'
  * json - handling JSON format
  * requests - HTTP library

---------------------------------------------------------------
Deployment / Components
---------------------------------------------------------------
* unzip package and grant execution rights -- e.g.
  'unzip /path/to/NewRelic_SREChallenge_ZanderHamidi.zip -d <destination> && chmod -R a+x    <destination>/NewRelic_SREChallenge_ZanderHamidi/'
  * demographics.py - CLI taking two arguments, a list of states and an output format
  * BroadbandMap.py - contains BroadbandMapData class bundling API requests and data per State

---------------------------------------------------------------
Usage
---------------------------------------------------------------
* cd into folder
* ./demographics.py <comma separated list of states, case insensitive> <CSV|averages>
  * 'CSV' creates file 'demographics.csv' in the same directory with several demographic fields on each state passed
    * fields = State Name, Population, Households, Income below Poverty, Median Income
  * 'averages' prints the simple average of Income below Poverty among all states passed

example 1:
cd /path/to/NewRelic_SREChallenge_ZanderHamidi
./demographics.py Missouri,kansas,Oregon,hawaii,Louisiana CSV
--> /path/to/NewRelic_SREChallenge_ZanderHamidi/demographics.csv

example 2:
cd /path/to/NewRelic_SREChallenge_ZanderHamidi
./demographics.py Missouri,kansas,Oregon,hawaii,Louisiana averages
-->  "Average Income Below Poverty:  0.15176"

---------------------------------------------------------------
Author - Zander Hamidi, linkedin.com/in/zander-hamidi
---------------------------------------------------------------
