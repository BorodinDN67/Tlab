import json
from pathlib import Path

def merge_results(DATA_DIR: Path | str):
    if DATA_DIR is None:
        DATA_DIR = Path('./results/test')
    else:
        DATA_DIR = Path(DATA_DIR)

    CLASSIC_DIR =DATA_DIR / 'classic'
    GATE_DIR = DATA_DIR / 'gate'
    RANDOM_DIR = DATA_DIR / 'random'

    CLASSIC_RES = DATA_DIR / 'classic_results.jsonl'
    GATE_RES = DATA_DIR / 'gate_results.jsonl'
    RANDOM_RES = DATA_DIR / 'random_results.jsonl'


    classic = []
    with open(CLASSIC_DIR / 'results.jsonl', 'r') as f:
        for line in f:
            row = json.loads(line.strip())
            classic.append({
                'text': row['steering'],
                'prompt_id': row['prompt_id']
            })

    gate = []
    with open(GATE_DIR  / 'results.jsonl', 'r') as f:
        for line in f:
            row = json.loads(line.strip())
            gate.append({
                'text': row['steering'],
                'prompt_id': row['prompt_id']
            })

    random = []
    with open(RANDOM_DIR / 'results.jsonl', 'r') as f:
        for line in f:
            row = json.loads(line.strip())
            gate.append({
                'text': row['steering'],
                'prompt_id': row['prompt_id']
            })


    with open(CLASSIC_DIR / 'results_impersonal.jsonl' , 'w') as f:
        json.dump(classic, f, indent=2)
    with open(GATE_DIR / 'results_impersonal.jsonl' , 'w') as f:
        json.dump(gate, f, indent=2)
    with open(RANDOM_DIR / 'results_impersonal.jsonl' , 'w') as f:
        json.dump(random, f, indent=2)


if __name__ == '__main__':
    merge_results()
