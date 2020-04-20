import pytest
from mysql_controller import execQuery

@pytest.fixture
def supply_username_password():
	query = "SELECT username, password FROM user"
	result = execQuery(query, None)
	return result

def test_login(supply_username_password):
	# Check login succesful
	for data in supply_username_password:
		# Query database
	    query = "SELECT * FROM user WHERE username=%s AND password=%s"
	    format = (data.username, data.password,)
	    user = None
	    try:
	        user = execQuery(query, format)
	    except Exception as e:
	        assert False, "Query is not valid"
	    # Check if user found
	    assert user != []
	
