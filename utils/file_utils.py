import json


def load_yokatlas_data(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def dump_yokatlas_data(path: str, parsed_data: list):
    with open (path, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=3)