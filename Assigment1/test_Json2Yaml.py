import unittest
from Json2Yaml import jsonToYaml
import json

"""
Testing APP 
"""

test_json = {
    "name": "Mher",
    "surname": "Barseghyan",
    "hobbies": ["Programming", "Football", "Tenis"],
    "family": {
        "mother": "mam jan",
        "Brother": "Lyov jan"
    },
    "Job": "in progress"
}

with open("test.json", 'w') as file:
    json.dump(test_json, file)


class TestJson2Yaml(unittest.TestCase):
    """
    Tests unit
    """

    def test_function(self):
        self.assertRaises(NameError, jsonToYaml, None, None)
        self.assertRaises(NameError, jsonToYaml, "test.json", None)
        self.assertRaises(NameError, jsonToYaml, None, "test.yaml")
        self.assertRaises(FileNotFoundError, jsonToYaml, 'Unknownfile', 'some.yaml')
        self.assertIsNone(jsonToYaml('test.json', 'test.yaml'))
