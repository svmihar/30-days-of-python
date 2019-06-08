#!/.venv python
import os
import json
import time
import pandas as pd
import requests
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def load_json(fname):
    with open(fname, 'r') as infile:
        data = json.load(infile)
    return data


def load_matches():
    return load_json('matches.json')


def save_json(url, fname):
    response = requests.get(url).text
    with open(fname, 'w') as out_file:
        out_file.write(response)
    del response
    print("Downloaded", fname)


def main(teams=[]):
    matches = load_matches()
    if not os.path.exists('heroes.json'):
        save_json('https://api.opendota.com/api/heroes', 'heroes.json')
    heroes = {x['id']: x['localized_name'] for x in load_json('heroes.json')}
    tbl = []
    for m in matches:
        if m['start_time'] < 1473984000:
            continue
        if teams != [] and m['opposing_team_name'] not in teams:
            continue

        fname = f'matches/{m["match_id"]}.json'
        url = f'https://api.opendota.com/api/matches/{m["match_id"]}'
        if not os.path.exists(fname):
            save_json(url, fname)
            time.sleep(1)
        match_obj = load_json(fname)
        if 'error' in match_obj:
            save_json(url, fname)
            match_obj = load_json(fname)
        team = 'radiant' if m['radiant'] else 'dire'
        vals = [
            team,
            'win' if m['radiant_win'] == (team == 'radiant') else 'loss',
            m['opposing_team_name']
        ]
        for i in match_obj['players']:
            if i['isRadiant'] == m['radiant']:
                vals.append('with_' + heroes[i['hero_id']])
            else:
                vals.append('against_' + heroes[i['hero_id']])
        tbl.append(vals)
    te = TransactionEncoder()
    te_ary = te.fit(tbl).transform(tbl)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    pd.set_option('display.max_colwidth', -1)
    pd.set_option('display.max_rows', -1)

    out_rules = apriori(df, min_support=0.05, use_colnames=True).sort_values('support')

    return out_rules


if __name__ == "__main__":
    import sys
    out = main(sys.argv[1:])
    # we can return only those rows with 'win' in them
    matcher = frozenset(['win'])
    out1 = out[out.itemsets.map(matcher.intersection).map(bool)]
    print(out1.to_string(index=False))