import json


data={
    "persons": [
        {
            "city": "Seattle",
            "name": "Brian"
        },
        {
            "city": "Amsterdam",
            "name": "David"
        }
    ]
}
print(json.dumps(data))