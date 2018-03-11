import requests
import json

# Get access token
def get_access_token(client_id, client_secret):
	r = requests.get(url + '/oauth/access_token/client_id=' + client_id + '/client_secret=' + client_secret)
	j = json.loads(r.text)
	access_token = j['access_token']
	return access_token


'''
TagType
'''

# Add TagType
def add_tagtype(tag_name, tag_value):
	data = {"data": {
	        "name": tag_name,
	        "value": tag_value
	    }}
	a = requests.post(url + '/api/tagtype', headers = headers, data = json.dumps(data))
	return a.text

# Read Tags
def read_tags(sensor_id):
	response = requests.get(url + '/api/sensor/' + sensor_id + '/tags', headers = headers)
	return response.text

'''
BuildingTemplate
'''

# Create a Building Template
def create_template(template_name, template_desciption, tag_types):
	data = {"data": {
	        "name": template_name,
	        "description": template_desciption,
	        "tag_types": tag_types
	    }}
	a = requests.post(url + '/api/template', headers = headers, data = json.dumps(data))
	return a.text

# Get BuildingTemplate details
def get_building_template(template_name):
	response = requests.get(url + '/api/template/' + template_name, headers = headers)
	return response.text

# Delete building
def delete_building_template(template_name):
	response = requests.delete(url + '/api/template/' + template_name, headers = headers)
	return response.text


'''
Building
'''

# Create a new building
def create_building(building_name, building_description, building_template):
	data = {"data": {
	        "name": building_name,
	        "description": building_description,
	        "template": building_template
	    }}
	p = requests.post(url + '/api/building', headers = headers, data = json.dumps(data))
	return p.text


# Get building details
def get_building(building_name):
	response = requests.get(url + '/api/building/' + building_name, headers = headers)
	return response.text


# Delete building
def delete_building(building_name):
	response = requests.delete(url + '/api/building/' + building_name, headers = headers)
	return response.text


'''
Building
'''

# Create a new building
def create_building(building_name, building_description, building_template):
	data = {"data": {
	        "name": building_name,
	        "description": building_description,
	        "template": building_template
	    }}
	p = requests.post(url + '/api/building', headers = headers, data = json.dumps(data))
	return p.text


# Get building details
def get_building(building_name):
	response = requests.get(url + '/api/building/' + building_name, headers = headers)
	return response.text


# Delete building
def delete_building(building_name):
	response = requests.delete(url + '/api/building/' + building_name, headers = headers)
	return response.text


'''
DataService
'''

# Create a DataService
def create_dataservice(dataservice_name, dataservice_desciption, host, port):
	data = {"data": {
	        "name": dataservice_name,
	        "description": dataservice_desciption,
	        "host": host,
	        "port": port
	    }}
	a = requests.post(url + '/api/dataservice', headers = headers, data = json.dumps(data))
	return a.text

# Get DataService details
def get_dataservice(dataservice_name):
	response = requests.get(url + '/api/dataservice/' + dataservice_name, headers = headers)
	return response.text

# Delete DataService
def delete_dataservice(dataservice_name):
	response = requests.delete(url + '/api/dataservice/' + dataservice_name, headers = headers)
	return response.text


'''
Sensor
'''

# Create a Sensor
def create_sensor(sensor_name, sensor_identifier, building):
	data = {
	        "name": sensor_name,
	        "building": building,
	        "identifier": sensor_identifier
	    }
	a = requests.post(url + '/api/sensor', headers = headers, data = json.dumps(data), verify=False)
	return a.text

# Get Sensor details
def get_sensor(sensor_name):
	response = requests.get(url + '/api/sensor/' + sensor_name, headers = headers)
	return response.text

# Search Sensor
def search_sensor(sensor_identifier, building, tags):
	data = {"data": {
	        "ID": sensor_identifier,
	        "Building": building,
	        "Tags": tags
	    }}
	response = requests.post(url + '/api/search', headers = headers, data = json.dumps(data))
	return response.text

'''
Metadata
'''

# Add Metadata
def add_metadata(name, value, sensor_id):
	data = {
		  "data":{[
          {
            "name": name,
            "value": value
          }]
		}}
	a = requests.post(url + '/api/sensor' + sensor_id + '/metadata', headers = headers, data = json.dumps(data))
	return a.text

# Read Metadata
def read_metadata(sensor_id):
	response = requests.get(url + '/api/sensor/' + sensor_id + '/metadata', headers = headers)
	return response.text		

'''
Usergroups
'''

# Create a Usergroup
def create_user_group(group_name, group_description):
	data = {
	        "name": group_name,
	        "description": group_description
	    }
	a = requests.post(url + '/api/user_group', headers = headers, data = json.dumps(data))
	return a.text

# Create a Usergroup
def add_user_group(group_name):
	data = {
		   "data":[
		            "synergy@gmail.com",
		            "test@gmail.com"
		          ]
		}
	a = requests.post(url + '/api/user_group/' + group_name + '/users', headers = headers, data = json.dumps(data))
	return a.text	

# Add users to UserGroup
def get_user_group(group_name):
	response = requests.get(url + '/api/user_group/' + group_name + '/users', headers = headers)
	return response.text

'''
Permission
'''

# Create Permission
def create_permission(sensor_group, user_group, permission):
	data = {
		  "data":{
		      "sensor_group":sensor_group,
		      "user_group":user_group,
		      "permission":permission
		  }
		}
	a = requests.post(url + '/api/permission', headers = headers, data = json.dumps(data))
	return a.text

# Read Permission
def get_permission(user_group, sensor_group):
	response = requests.get(url + '/api/permission?user_group=' + user_group + '&sensor_group=' + sensor_group, headers = headers)
	return response.text	

# Delete Permission
def delete_permission(user_group, sensor_group):
	response = requests.delete(url + '/api/permission?user_group=' + user_group + '&sensor_group=' + sensor_group, headers = headers)
	return response.text

'''
User
'''

# Add a new User
def add_user(first_name, last_name, email, role):
	data = {
		  "data":{
		      "first_name":first_name,
		      "last_name":last_name,
		      "email":email,
		      "role":role
		  }
		}
	a = requests.post(url + '/api/user', headers = headers, data = json.dumps(data))
	return a.text

# Get User Details
def get_user_details(email):
	response = requests.get(url + '/api/user/' + email, headers = headers)
	return response.text	

# Remove User
def remove_user(email):
	response = requests.delete(url + '/api/user/' + email, headers = headers)
	return response.text	


if __name__ == '__main__':
		url = 'http://localhost:81' #base url of the CentralServiceb54UNbnlfK31IcojTCTOoiGl4eDChtutjDiCR60EkV2r1jvu4Z
		access_token = get_access_token('eWhCdqnq7ty7zFof0O7QMn7PkUWfQmPfg31LnBJN', 'b54UNbnlfK31IcojTCTOoiGl4eDChtutjDiCR60EkV2r1jvu4Z') #client_id and client_secret obtained from the account at the CerntralService. Keep client_id and client_secret hidden.
		headers = {'Authorization': 'bearer ' + access_token, 'content-type':'application/json'}

		# Calling TagType functions
		# print add_tagtype('corridor', 'corridor')
		# print read_tags('26da099a-3fe0-4966-b068-14f51bcedb6e')

		# Calling BuildingTemplate functions
		# print create_template('Test_Building_Template', 'New Building Template', ["floor","room","corridor"])
		# print get_building_template('Test_Building_Template')
		# print delete_building_template('Test_Building_Template')

		# Calling Builidng functions
		# print create_building('Test_Building4', 'building_description2', 'Building1')
		# print get_building('Building1')
		# print delete_building('Test_Building')

		# Calling DataService functions
		# print create_dataservice('ds3', 'Test_ds3', '127.0.0.3', '83')
		# print get_dataservice('ds3')
		# print delete_dataservice('ds3')	

		# Calling Sensor functions
		# print create_sensor('Test Sensor', 'floor', 'B1')
		# print get_sensor('Test Sensor')
		# print search_sensor('Test Sensor', 'NSH', 'Sensor Tag')

		# Calling Metadata functions
		# print add_metadata('name', 'value', 'id')
		# print read_metadata('')

		# Calling UserGroup functions
		# print create_user_group('Test User Group', 'Description for User Group')
		# print add_user_group('Test User Group')
		# print get_user_group('Test User Group')

		# Calling Permission functions
		# print create_permission('Test Sensor Group', 'Test User Group', 'r')
		# print get_permission('Test Sensor Group', 'Test User Group')
		# print delete_permission('Test Sensor Group', 'Test User Group')

		# Calling User functions
		print add_user('Anurag', 'Last', 'anurag1@gmail.com', 'super')
		# print get_user_details('anurag@gmail.com')
		# print remove_user('anurag@gmail.com')