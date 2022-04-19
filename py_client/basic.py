import requests


# # To display the user details with user id as an argument of request.
endpoint = "http://localhost:8000/api/user/"
get_response = requests.get(endpoint, json={'user_id': 2})
print('User Details:')
print(get_response.json())

# # To display the user details with user id in url.
endpoint = "http://localhost:8000/api/user/2"
get_response = requests.get(endpoint)
print('User Details:')
print(get_response.json())


# # To display the account details with account id as an argument of request.
endpoint = "http://localhost:8000/api/account/"
get_response = requests.get(endpoint, json={'account_id':3})
print('Account Details:')
print(get_response.json())


# # To display the account details with account id in url.
endpoint = "http://localhost:8000/api/account/3"
get_response = requests.get(endpoint)
print('Account Details:')
print(get_response.json())


# To perform transaction between accounts.
endpoint = "http://localhost:8000/api/ledger/create/"
get_response = requests.post(endpoint, json={'credit_account_id':3, 'debit_account_id':4, 'amount':2.93827492})
print(get_response.json())
