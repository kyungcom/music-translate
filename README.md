# music-translate🔉
## 웹크롤링과 naver 번역, 언어감지 api를 통한 노래 번역 서비스
```
kt AIVLE 스쿨에서 배운 api사용법과 크롤링 selenium 사용법을 복습하기 위해서,
혼자 만들어본 간단한 서비스입니다.
```

## 2. 프로젝트 구성
### 2-1. 주요기능
* 노래제목 입력
* 입력된 노래 제목을 멜론에 검색
* 검색결과 여부 확인
* 노래 가사를 네이버 언어감지 API를 통해 언어감지(한국어, 영어, 일본어 등등)
* 노래 가사를 네이버 번역 API를 통해 번역한 후, 사용자에게 전송

### 2-2. 사용 방법
1. 노래 제목 입력
2. 기다림

### 2-3. 개발 환경
+ Python 3.9.13
+ Selenium 4.3.0
+ Requests 2.28.1
+ time
+ json

### 2-4. API List
+ NAVER 언어감지 API
+ NAVER Papago 번역 API

## 3. 빌드방법
### 3-1. Api Key 발급
+ https://developers.naver.com/main/ 에서 NAVER 언어감지, NAVER Papago 번역 API 발급

### 3-2. git clone
git clone 해주세요

```
git clone https://github.com/kyungcom/MapDairy.git
```
### 3-3. chrome driver 설치
![image](https://user-images.githubusercontent.com/72953874/183106356-eb42ebfc-e36a-40cd-adef-b9ca4b1a94df.png)

```
https://chromedriver.chromium.org/downloads
```
에서 본인 버전에 맞는 크롬드라이버를 다운로드 및 압축해제 후, searchMusic.py가 있는 폴더에 넣어주세요.


### 3-4. config.py 파일 설정
config.py 파일을 만들고
```
CLIENT_ID = ?
CLIENT_SECRET = ?
```
? 값을 채워주세요.

translate.py를 실행하시면 끝입니다.

## 실행결과
![image](https://user-images.githubusercontent.com/72953874/183106217-8fa5196c-4174-4234-9eec-c2b5336bf596.png)


## License
````````
The MIT License

Copyright (c) 2022 ParkInho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
``````````