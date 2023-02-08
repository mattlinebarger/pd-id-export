#!/usr/bin/env python3

import requests
import datetime
import csv

# add your PagerDuty api key below (read-only is all that is needed)
apiKey = 'YOUR_PAGERDUTY_API_KEY_GOES_HERE'

# this list holds all the reports that will run, remove any that you do not want
reports = ['users', 'teams', 'escalation_policies', 'schedules', 'services']

# function to build a report based on report type
def build_report(apiKey, reportType):

    offset = 0
    more = True
    data = []

    headers = {
    'Authorization': 'Token token=' + apiKey,
    'Accept': 'application/vnd.pagerduty+json;version=2',
    'Content-Type': 'application/json'
    }

    while (more == True):
        url = 'https://api.pagerduty.com/' + reportType + '?limit=100&offset=' + str(offset)

        response = requests.request('GET', url, headers=headers)

        data = data + response.json()[reportType]

        if (more == True):
            offset = offset + 100

        more = response.json()['more']

    details = []
    for x in data:

            details.append({'id': x['id'],
                        'name': x['name']
                        })

    fileName = 'pagerduty_' + reportType + datetime.datetime.now().strftime('_%Y-%m-%d') + '.csv'
    fields = list(details[0].keys())

    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(details)

#  build report for each report type
for report in reports:
    build_report(apiKey, report)
