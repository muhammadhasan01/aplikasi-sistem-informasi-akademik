import pytest
from faker import Faker
from mysql_controller import execQuery

@pytest.fixture
def supply_valid_username_password():
	query = "SELECT username, password FROM user"
	result = execQuery(query, None)
	return result

@pytest.fixture
def supply_invalid_username_password():
	num_of_invalid_data = 10
	result = []
	fake = Faker()
	for _ in range(num_of_invalid_data):
		result.append((fake.name(), fake.password()))
	return result

def test_login(supply_valid_username_password, supply_invalid_username_password):
	# Check login succesful and also to map valid data
	valid_data = {}
	for data in supply_valid_username_password:
	    # Query database
	    query = "SELECT * FROM user WHERE username=%s AND password=%s"
	    format = (data.username, data.password,)
	    user = None
	    try:
	        user = execQuery(query, format)
	    except Exception as e:
	        assert False, "Query is not valid"
	    # Check if user found
	    assert user != [], "Valid user not found"
	    # Map valid data for later use
	    valid_data[data.username] = data.password

	for invalid_data in supply_invalid_username_password:
		username = invalid_data[0]
		password = invalid_data[1]
		# if it's actually not an invalid data, then continue
		if (username in valid_data) and (password == valid_data[username]):
			continue
		# Query database
		query = "SELECT * FROM user WHERE username=%s AND password=%s"
		format = (username, password,)
		user = None
		try:
			user = execQuery(query, format)
		except Exception as e:
			assert False, "Query is not valid"
		# Check if user not found
		assert user == [], "Invalid user found"

	

