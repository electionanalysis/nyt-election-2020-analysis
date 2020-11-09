import requests

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

all_results = {}
for state in states:
    print(f'Downloading {state}')
    formatted_state = state.lower().replace(' ', '-')

    # Scrape data for this state and store as a dict
    state_response = requests.get(
        f'https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/state-page/{formatted_state}.json')
    all_results[formatted_state] = state_response.json()

    # Archive the response JSON too
    with open(f'scrapes-allraces/{formatted_state}.json', 'wb') as f:
        f.write(state_response.content)

