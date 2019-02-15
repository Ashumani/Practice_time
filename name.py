import requests
import json
import typing
import extract_link
import webbrowser
# url = "https://www.google.co.in/search?"
# query = input('Enter a search query: ')
# query = query.split()
# payload = {'q': query}

# response = requests.get(url, payload)

# with open('data.txt', mode='w') as f:
#     f.write(response.text)


with open('data.txt', mode='r') as f:
    data = f.read()

list_of_urls = extract_link.get_links(data)

def extract(list_of_urls) :
    for i in list_of_urls:
        if 'https' in i:
            i = i.replace('%3F', '?')
            i = i.replace('%3D','=')
            start_index = i.find('=')
            end_index = i.find('&', start_index)
            print(i[start_index+1: end_index])


# https://www.youtube.com/watch?v=YQHsXMglC9A















































# # response = requests.get(url+'+'.join(['sawpnil','shindemeshram']))

# string = '<a href="https://www.github.com">Google</a>  <a href="https://linkedin.com">Linkedin</a>'

# def get_next_target(string:str):
#     a_href_index = string.find('<a href=')
#     start_index = string.find('"', a_href_index)
#     end_index = string.find('"', start_index+1)
#     url = string[start_index+1: end_index]
#     return url, end_index



# def  get_urls(string):

#     url_list = []
#     start_index = 0
#     while True:
#         url, end_index = get_next_target(string)
#         url_list.append(url)
#         if string.find("<a", end_index) == -1:
#             break
#         start_index = end_index


# print(get_urls(string))