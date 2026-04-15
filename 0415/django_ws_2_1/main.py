
import requests
from pprint import pprint

# 1. API 설정 정보
# 상품 리스트 조회용 URL
API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
# 율님이 발급받은 TTBKey를 여기에 입력하세요
API_KEY = 'ttban84661201001'

# 2. 요구사항에 따른 파라미터 구성
params = {
    'ttbkey': 'ttban84661201001',
    'QueryType': 'ItemNewSpecial', # 요구사항: 주목할 만한 신간 리스트
    'MaxResults': 50,              # 요구사항: 최대 50개 데이터
    'start': 1,
    'SearchTarget': 'Book',        # 요구사항: 조회 대상 도서로 한정
    'output': 'js',                # 요구사항: 응답 데이터 JSON (js=json)
    'Version': '20131101',         # 최신 API 버전
}

def fetch_aladin_books():
    try:
        # API 요청 (GET)
        response = requests.get(API_URL, params=params)
        
        # JSON 형식으로 데이터 변환
        data = response.json()
        
        # 실제 도서 리스트 추출 (알라딘은 'item' 키에 데이터를 담아줌)
        items = data.get('item', [])
        
        # 3. 요구사항: 특정 값들만 모은 결과 생성
        result = []
        for item in items:
            book_info = {
                '책 제목': item.get('title'),
                '저자': item.get('author'),
                '출간일': item.get('pubDate'),
                '국제 표준 도서 번호 (ISBN)': item.get('isbn')
            }
            result.append(book_info)
        
        return result

    except Exception as e:
        print(f"데이터 수집 중 오류 발생: {e}")
        return []

# 4. 결과 출력
if __name__ == "__main__":
    books = fetch_aladin_books()
    
    # 가독성 좋게 출력하기 위해 pprint 사용
    pprint(books)
    
    # 수집된 개수 확인
    print(f"\n총 {len(books)}개의 도서 데이터를 수집했습니다.")