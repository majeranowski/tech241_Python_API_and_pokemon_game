import requests
import json

# #get request
#
#
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req) # <Response [200]>
#
# print(post_codes_req.status_code) # 200
#
# print(post_codes_req)
# print(type(post_codes_req.status_code)) #int
# print(type(post_codes_req)) #requests.models.response
#
# print(post_codes_req.content) # all the content from URI as bytes
#
# print(post_codes_req.json()) # all the content from URI as JSON, class dict
#
# # POST requests - sending data to the API
# print("---------")
# json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
# headers = {'Content-Type': 'application/json'}
#
# post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
#
# print(post_multi_req.json())

# Pokemon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(pokemon_req.json())

# BBC webpages

# bbc_request = requests.get("https://www.bbc.com/")
# print(bbc_request.content) ## if it is not API we need to do content
