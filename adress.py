# app.py

from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # API로부터 데이터 가져오기
    api_key = '319c176db1d14a07ba02'
    url = f'http://openapi.foodsafetykorea.go.kr/api/{api_key}/I2500/xml/1/10'
    response = requests.get(url)

    if response.status_code == 200:
        encoding = response.encoding
        data = response.content.decode(encoding)
        soup = BeautifulSoup(data, 'lxml')

        # 주소 정보 추출
        addresses = [{"address": row.find('addr').text} for row in soup.find_all('row')]

        return render_template('index.html', address_data=addresses)

    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == '__main__':
    app.run(debug=True)
