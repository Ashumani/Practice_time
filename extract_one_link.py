string ='<a href="www.google.co.in">google</a> <a href="www.facebook.com">facebook</a>'
urls = []

href_index = string.find('<a href=')
print(href_index)
start_index = string.find('"',href_index)
print(start_index)
end_index = string.find('"',start_index + 1)
print(end_index)
print(string[start_index+1 : end_index])