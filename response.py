import requests
# a=open("input2.txt","w")
# str1=input('enter search value :')
serach_url = 'https://www.google.co.in/search?q='
query = input('Enter a query to search: ')
query = query.split()
query = '+'.join(query)
uri = serach_url+query
print(uri)
response = requests.get(uri)
print(response.url)
print(response.text)

