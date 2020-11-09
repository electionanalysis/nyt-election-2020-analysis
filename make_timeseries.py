import json

import pandas as pd

states = [
 'Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado',
 'Connecticut', 'Delaware', 'Florida', 'Georgia',
 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky',
 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan',
 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina',
 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico',
 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin',
 'West Virginia', 'Wyoming',
]


def collapse_results_by_party(results_by_candidate, candidates):
    results_by_party = {}
    for candidate, count in iter(results_by_candidate.items()):
        party = candidates[candidate]['party']
        results_by_party[party] = results_by_party.get(party, 0) + count

    return results_by_party


all_results = {}
for state in states:
    state_str = state.lower().replace(" ", "-")
    filename = f"scrapes-allraces/{state_str}.json"
    with open(filename, 'r') as j:
        all_results[state_str] = json.loads(j.read())

records = []
for state, state_results in iter(all_results.items()):
    for race in state_results['data']['races']:

        print(f"race_type={race['race_type']} race_id={race['race_id']}")

        for candidate in race['candidates']:
            if candidate['party_id'] == 'republican':
                candidate['party'] = 'rep'
            elif candidate['party_id'] == 'democrat':
                candidate['party'] = 'dem'
            else:
                print(f"Found other party: {candidate}")
                candidate['party'] = 'trd'
        candidates = {candidate['candidate_key']: candidate for candidate in race['candidates']}

        # Not all races have a timeseries - see the "expectations_text" for an explanation why not
        if 'timeseries' in race:
            for data_point in race['timeseries']:
                data_point['state'] = state
                data_point['race_type'] = race['race_type']
                data_point['race_id'] = race['race_id']

                data_point['expected_votes'] = race['tot_exp_vote']
                # data_point['trump2016'] = race['trump2016']
                # data_point['votes2012'] = race['votes2012']
                # data_point['votes2016'] = race['votes2016']

                vote_shares = collapse_results_by_party(data_point['vote_shares'], candidates)
                for party in ['rep', 'dem', 'trd']:
                    data_point['vote_share_{}'.format(party)] = vote_shares.get(party, 0)

                data_point.pop('vote_shares')
                records.append(data_point)

time_series_df = pd.DataFrame.from_records(records)
time_series_df.to_csv('output-allraces/nyt_ts.csv', encoding='utf-8')
