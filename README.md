
# pd-id-export
A simple python script that exports names and ids for all users, teams, escalation policies, schedules, and services in a PagerDuty account.

### Usage

 - Update line 8 with your PagerDuty API key.

    apiKey = 'YOUR_PAGERDUTY_API_KEY_GOES_HERE'

 - Remove or add any PagerDuty objects on line 11. You'll generate a CSV report for any object listed.

    reports = ['users', 'teams', 'escalation_policies', 'schedules', 'services']

***Note: Only 'users', 'teams', 'escalation_policies', 'schedules', and 'services' have been tested.***