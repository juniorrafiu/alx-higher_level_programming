#!/usr/bin/python3
"""
takes GitHub credentials
and uses GitHub api to display id
"""

if __name__ == '__main__':
    import requests
    import sys
    user, passw = sys.argv[1], sys.argv[2]
    response = requests.get('https://api.github.com/user', auth=(user, passw))
    print(response.json().get('id'))