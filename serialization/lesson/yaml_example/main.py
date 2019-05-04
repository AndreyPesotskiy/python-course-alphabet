from ruamel.yaml import YAML

if __name__ == "__main__":
    yaml = YAML()
    with open("config.yaml", "r") as file:
        config = yaml.load(file)

    print(type(config), config)
    print(config['database'])
    print(config['database']['port'])
    dict_config = dict(config)
    print(type(dict_config), dict_config)

    with open("result.yaml", "w") as file:
        yaml.dump(dict_config, file)
