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
	        "description": tag_value
	    }}
	a = requests.post(url + '/api/tagtype', headers = headers, data = json.dumps(data))
	return a.text

#Add tags to sensor	
def add_tag_to_sensor(tags, sensor_id):
	data = {
	"data": tags
	    }
	a = requests.post(url + '/api/sensor/' + sensor_id + "/tags", headers = headers, data = json.dumps(data))
	return a.text

# Read Tags
def read_tags(sensor_id):
	response = requests.get(url + '/api/sensor/' + sensor_id + '/tags', headers = headers)
	return response.text

# Delete Tag
def delete_tag_type(tag_name):
	response = requests.delete(url + '/api/tagtype/' + tag_name, headers = headers)
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
Buildings
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
	        "data":{
		        "name": sensor_name,
		        "identifier": sensor_identifier,
		        "building": building
		    	}
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
def add_metadata(data, sensor_id):
	data = {
		  "data":data
		  }
	a = requests.post(url + '/api/sensor/' + sensor_id + '/metadata', headers = headers, data = json.dumps(data))
	return a.text

# Read Metadata
def read_metadata(sensor_id):
	response = requests.get(url + '/api/sensor/' + sensor_id + '/metadata', headers = headers)
	return response.text		

'''
SensorGroups
'''

# Create a Sensorgroup
def create_sensor_group(group_name, building, group_description):
	data = {
	        "name": group_name,
	        "building": building,
	        "description": group_description
	    }
	a = requests.post(url + '/api/sensor_group', headers = headers, data = json.dumps(data))
	return a.text

# Add tags to Sensorgroup
def add_tags_sensor_group(tags, group_name):
	data = {
		   "data": tags
		}
	a = requests.post(url + '/api/sensor_group/' + group_name + '/tags', headers = headers, data = json.dumps(data))
	return a.text	

# Get list of tags in SensorGroup
def get_sensor_group(group_name):
	response = requests.get(url + '/api/sensor_group/' + group_name + '/tags', headers = headers)
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

# Add users to UserGroup
def add_user_to_group(users, group_name):
	data = users
		  		
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
def create_permission(user_group, sensor_group, permission):
	data = {
		  "data":{
		      "user_group":user_group,
		      "sensor_group":sensor_group,
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
		# print add_tagtype('tag2', 'Something')
		tags = [
           {
            "name": "floor",
            "value": "3600"
           },
           {
            "name": "room",
            "value": "3606"
           }
          ]
		# print add_tag_to_sensor(tags,'d5b25356-6aa3-4341-8908-14e7f7852dc0')
		# print read_tags('d5b25356-6aa3-4341-8908-14e7f7852dc0')
		# print delete_tag_type('tag1')


		# Calling BuildingTemplate functions
		# print create_template('Test_Building_Template1', 'New Building Template', ["floor","room","corridor"])
		# print get_building_template('Test_Building_Template')
		# print delete_building_template('Test_Building_Template')


		# Calling Builidng functions
		# print create_building('Test_Building4', 'building_description2', 'Building1')
		# print get_building('Test_Building4')
		# print delete_building('Test_Building')


		# Calling DataService functions
		# print create_dataservice('ds3', 'Test_ds3', '127.0.0.3', '83')
		# print get_dataservice('ds3')
		# print delete_dataservice('ds3')	


		# Calling Sensor functions
		# print create_sensor('Test Sensor', 'floor', 'B1')
		# print get_sensor('c51fba09-5dff-46d2-880f-a27df0cf4eec')
		# print search_sensor('c51fba09-5dff-46d2-880f-a27df0cf4eec', 'B1', ["floor:1"])


		# Calling Metadata functions
		metadata = [
          {
            "name": "MAC",
            "value": "01:02:03:04:05:06"
          },
          {
            "name": "Type",
            "value": "Temperature"
          }
         ]
		# print add_metadata(metadata, 'c51fba09-5dff-46d2-880f-a27df0cf4eec')
		# print read_metadata('c51fba09-5dff-46d2-880f-a27df0cf4eec')


		# Calling SensorGroup functions
		# print create_sensor_group('SG_B1', 'B1','Description for Sensor Group')
		tags2 = [
           {
            "name": "floor",
            "value": "floor"
           }
          ]
		# print add_tags_sensor_group(tags2, 'SG_B1',)
		# print get_sensor_group('SG_B1')


		# Calling UserGroup functions
		# print create_user_group('Test_User_Group', 'Description for User Group')
		users = {
				"data":[
			    {
			      "manager": False, 
			      "user_id": "anurag1@gmail.com"
			    },
			    {
			      "manager": False, 
			      "user_id": "anurag@gmail.com"
			    }
			  ]
			  }
		# print add_user_to_group(users, 'Test_User_Group')
		# print get_user_group('Test User Group')


		# Calling Permission functions
		# print create_permission('Test User Groupr', 'SG_B1', 'r')
		# print get_permission('Test User Groupr', 'SG_B1')
		# print delete_permission('Test User Groupr', 'SG_B1')


		# Calling User functions
		# print add_user('Anurag', 'Last', 'anurag12@gmail.com', 'default')
		print get_user_details('anurag12@gmail.com')
		# print remove_user('anurag12@gmail.com')