import requests
# a=open("input2.txt","w")
# str1=input('enter search value :')
search_url = 'https://www.google.co.in/search?q='
query = input('Enter a query to search: ')
query = query.split()
payload = {'q': query}
response = requests.get(search_url, payload)
print(response.text)



