def get_num_words (content):
    words_list = content.split()
    words_count = len(words_list)
    return words_count

def count_characters (content):
    content_data = {}
    for i in content:
        if i not in content_data.keys():
            content_data[i] = 0
        if i in content_data.keys():
            content_data[i] += 1
    return content_data

def sort_on (dict):
    return dict["num"]


def sort_list(dict):
    key_list = dict.keys()
    list=[]
    for key in key_list:
        list.append({"character":key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list