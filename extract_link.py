
# string = '<a href="www.google.co.in">google</a> <a href="www.facebook.com">facebook</a>'



def get_links(string):
    """
    params: 
        string - String is html, javascript and css returned by search query in a str
    return:
        list of urls in a '<a>' tag

    """
    urls = list()
    index = 0
    while True:
        a_index = string.find('<a href=', index)
        if a_index == -1:
            break
        start_index = string.find('"', a_index)
        end_index = string.find('"', start_index + 1)
        index = end_index
        urls.append(string[start_index+1: end_index])
    return urls 

