from urllib.request import Request, urlopen, HTTPError
import json
import random

APPLICATION_ID = '___'
REST_API_KEY = '___'

BASE_URL = 'https://parse.buddy.com/parse'

CLASSES = '/classes'
CLASS_COURSE ='/course'

PARSE_HEADERS = {
    'X-Parse-Application-Id': APPLICATION_ID,
    'X-Parse-REST-API-Key': REST_API_KEY,
    'Content-Type': 'application/json'
}

def read_course(object_id=None):
    url = BASE_URL + CLASSES + CLASS_COURSE

    if object_id is not None:
        url += '/' + object_id
    q = Request(url, method='GET', headers=PARSE_HEADERS)
    try:
        conn = urlopen(q)
        s_data = ''.join([line.decode('utf-8') for line in conn.readlines()])
        result = json.loads(s_data)
        conn.close()
    except HTTPError as e:
        result = json.dumps({
            'error':e.reason,
            'code':e.code
        })
    finally:
        return result
def delete_coures(object_id):
    url = BASE_URL + CLASSES + CLASS_COURSE + '/' + object_id

    q = Request(url, method='DELETE', headers=PARSE_HEADERS)
    try:
        conn = urlopen(q)
        s_data = ''.join([line.decode('utf-8') for line in conn.readlines()])
        result = json.loads(s_data)
        conn.close()
    except HTTPError as e:
        result = json.dumps({
            'error':e.reason,
            'code':e.code
        })
    finally:
        return result
def rate_course(object_id, rating):
    course = read_course(object_id)

    stars = course['stars']
    votes = course['votes']

    new_average = ((stars * votes) + rating) / (votes + 1)

    url = BASE_URL + CLASSES + CLASS_COURSE + '/' + object_id

    data = {
        'stars':new_average,
        'votes':votes + 1
    }

    q= Request(url, method='PUT', headers=PARSE_HEADERS, data=json.dumps(data).encode('utf-8'))
    try:
        conn = urlopen(q)
        s_data = ''.join([line.decode('utf-8') for line in conn.readlines()])
        result = json.loads(s_data)
        conn.close()
    except HTTPError as e:
        result = json.dumps({
            'error':e.reason,
            'code':e.code
        })
    finally:
        return result
def create_course(title, author_first_name, author_last_name):
    url = BASE_URL + CLASSES + CLASS_COURSE

    data = {
        'title':title,
        'author_first_name':author_first_name,
        'author_last_name':author_last_name,
        'votes':0,
        'stars':0
    }

    q = Request(url, method='POST', headers=PARSE_HEADERS, data=json.dumps(data).encode('utf-8'))
    conn = urlopen(q)
    s_data = ''.join([line.decode('utf-8') for line in conn.readlines()])
    result = json.loads(s_data)
    print(result)

if __name__=='__main__':
    create_course('Getting Started with the Python Standard Library','Douglas','Starnes')
    create_course('Python 101','John','Doe')
    all_courses = read_course()
    for course in all_courses['results']:
        print('{0}: {1}'.format(course['objectId'],course['title']))
    print('Getting details for: {0}', all_courses['results'][0])
    first_object_id = all_courses['results'][0]['objectId']
    course = read_course(first_object_id)
    print(course)
    for __ in range(10):
        rating = random.randint(1,5)
        print('Adding rating of {0}'.format(rating))
        rate_course(first_object_id,rating)
        updated_course = read_course(first_object_id)
        print('Average rating is now {0}'.format(updated_course['stars']))
    print('removing course')
    result = delete_coures(first_object_id)
    print(result)
    print('Trying to read nonexistent course')
    print(read_course(first_object_id))



    