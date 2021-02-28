import json
import yaml
import argparse

"""
Simple json to yaml parser
"""

parser = argparse.ArgumentParser(description='Pars Json to Yaml.')
parser.add_argument('--json', type=str,
                    help='input json file')

parser.add_argument('--yaml', type=str,
                    help='output yaml file')
args = parser.parse_args()
json_file = args.json
yaml_file = args.yaml


def jsonToYaml(json_file, yaml_file):
    """
    The function jsonToYaml read a JSON file and write YAML file
    also handled exceptions
    """
    if not json_file:
        print("Please specify input json ")
        raise NameError

    if not yaml_file:
        print("Please specify output yaml")
        raise NameError

    try:
        with open(json_file) as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"The specified json file ({json_file}) can't be found, please try again")
        raise FileNotFoundError

    except json.decoder.JSONDecodeError:
        print("Misconfigured json, please try again")
        raise json.decoder.JSONDecodeError

    with open(yaml_file, 'w') as file:
        yaml.dump(data=data, stream=file)


if __name__ == '__main__':
    """ 
    Running the function
    """
    jsonToYaml(json_file, yaml_file)
    print("Dumped Successfulle")
