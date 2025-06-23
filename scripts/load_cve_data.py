# scripts/load_cve_data.py

import json
import pandas as pd

def load_cve_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    records = []
    for item in data.get('CVE_Items', []):
        cve_id = item['cve']['CVE_data_meta']['ID']
        description = item['cve']['description']['description_data'][0]['value']
        published_date = item['publishedDate']
        impact = item.get('impact', {})
        score = None
        attack_vector = None

        if 'baseMetricV3' in impact:
            score = impact['baseMetricV3']['cvssV3']['baseScore']
            attack_vector = impact['baseMetricV3']['cvssV3']['attackVector']
        elif 'baseMetricV2' in impact:
            score = impact['baseMetricV2']['cvssV2']['baseScore']
            attack_vector = impact['baseMetricV2']['cvssV2']['accessVector']

        records.append({
            'CVE_ID': cve_id,
            'Description': description,
            'Published': published_date,
            'Score': score,
            'Attack Vector': attack_vector
        })

    df = pd.DataFrame(records)
    return df
