import yaml  # import pyyaml module
import os

user_details = {'UserName': 'Ganesh',
                'Password': 'Gan123*',
                'phone': 3256,
                'AccessKeys': ['EmployeeTable',
                               'SoftwaresList',
                               'HardwareList']
                }


## Open the file and Write the file

with open("data.yaml", 'w') as yamlfile:
    data = yaml.dump(user_details, yamlfile,sort_keys=False, default_flow_style=False)
    print("Write successful")

## Open the file and load the file

with open("data.yaml", "r") as yamlfile:
    data_read = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
print(data_read)

#.......................................................................................
# WRITING  CONFIG FILES

from configparser import ConfigParser  #we have configparser module which can help us with creation of config files

#Get the configparser object
config_object = ConfigParser()

#Assume we need  sections in the config file, let's call them USERINFO
config_object["USERINFO"] = {
    "admin": "Ganesh Hendge",
    "loginid": "ganeshhendge",
    "password": "Gan123"
}



#Write the above sections to config.ini file
with open('data.cfg', 'w') as conf:
    config_object.write(conf)

#READING CONFIG FILES

#Read config.cfg file
config_object = ConfigParser()
config_object.read("data.cfg")

#Get the password
userinfo = config_object["USERINFO"]
print("Password is {}".format(userinfo["password"]))

#................................................................


# WRITING  JSON CONFIG FILE

import json

user_info = {
    "domain" : "Ganesh",
    "language" : "python",
    "date" : "02/09/2022",
    "topic" : "json file"
}
mydata_json = json.dumps(user_info)

with open("data.json", "w") as jsonfile:
    jsonfile.write(mydata_json)
    print("Write successful")


#READING JSON CONFIG FILE

with open("data.json", "r") as jsonfile:
    data2 = json.load(jsonfile)
    print("Read successful")
print(data2)