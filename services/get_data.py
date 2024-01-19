import json


def filter_dict(data: dict) -> dict:
    return {
        k: v
        for k, v in data.items()
        if v and not k.endswith('последовательность)')
    }


def get_data(path: str) -> dict[str, list[str]]:
    with open("basedata/attestation.json", "r") as file:
        return filter_dict(json.load(file))
