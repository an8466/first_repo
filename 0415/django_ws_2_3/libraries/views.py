import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttban84661201001' # 율님의 키

    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': 50,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(API_URL, params=params)
    data = response.json()
    items = data.get('item', [])

    result = []
    for item in items:
        # 요구사항: 제목, 저자, 출간일, ISBN 수집 (KeyError 방지)
        book_info = {
            'title': item.get('title'),
            'author': item.get('author'),
            'pubDate': item.get('pubDate'),
            'isbn': item.get('isbn'),
        }
        result.append(book_info)

    # 수집한 데이터를 template에 넘겨줌
    context = {
        'book_list': result,
    }
    return render(request, 'libraries/recommend.html', context)