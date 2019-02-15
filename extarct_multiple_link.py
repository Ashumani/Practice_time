def get_links(string):
    """

    :param string:
        String is htmal, javascript and css returned by search query in a str
    :return:
        List of url present in <a> tag

    """
    urls = []
    index = 0
    while True:

        href_index = string.find('<a href=', index)
        if href_index == -1:
            break
        start_index = string.find('"',href_index)
        end_index = string.find('"',start_index + 1)
        index = end_index
        urls.append(string[start_index+1 : end_index])
    return urls

