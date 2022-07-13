import yaml
from yaml.loader import SafeLoader


data = yaml.load(open('example.yaml'), Loader=SafeLoader)
#print(data)
