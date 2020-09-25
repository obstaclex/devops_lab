import requests
LOGIN = ""
PASSWORD = ""
URI_PARAMS = {'per_page': '100', 'state': 'all'}
URL = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'


def get_pulls(state):
    if state == "open" or state == "closed":
        return based_on_state(state)
    elif state == "accepted" or state == "needs work":
        return based_on_label(state)
    else:
        return get_all()


def get_info():
    get = requests.get(URL, params=URI_PARAMS, auth=(LOGIN, PASSWORD))
    github_info = get.json()
    return github_info


def get_all():
    list_json_data = []
    for x in get_info():
        list_json_data.append(
            {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return list_json_data


def based_on_state(state):
    list_json_data = []
    if state == "open" or state == "closed":
        for x in get_info():
            if x['state'] == state:
                list_json_data.append(
                    {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return list_json_data


def based_on_label(state):
    list_json_data = []
    if state == "accepted" or state == "needs work":
        for x in get_info():
            if x['labels'] == []:
                continue
            else:
                if x['labels'][0]['name'] == state:
                    list_json_data.append(
                        {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return list_json_data
