# music-translate๐
## ์นํฌ๋กค๋ง๊ณผ naver ๋ฒ์ญ, ์ธ์ด๊ฐ์ง api๋ฅผ ํตํ ๋ธ๋ ๋ฒ์ญ ์๋น์ค
```
kt AIVLE ์ค์ฟจ์์ ๋ฐฐ์ด api์ฌ์ฉ๋ฒ๊ณผ ํฌ๋กค๋ง selenium ์ฌ์ฉ๋ฒ์ ๋ณต์ตํ๊ธฐ ์ํด์,
ํผ์ ๋ง๋ค์ด๋ณธ ๊ฐ๋จํ ์๋น์ค์๋๋ค.
```

## 2. ํ๋ก์ ํธ ๊ตฌ์ฑ
### 2-1. ์ฃผ์๊ธฐ๋ฅ
* ๋ธ๋์ ๋ชฉ ์๋ ฅ
* ์๋ ฅ๋ ๋ธ๋ ์ ๋ชฉ์ ๋ฉ๋ก ์ ๊ฒ์
* ๊ฒ์๊ฒฐ๊ณผ ์ฌ๋ถ ํ์ธ
* ๋ธ๋ ๊ฐ์ฌ๋ฅผ ๋ค์ด๋ฒ ์ธ์ด๊ฐ์ง API๋ฅผ ํตํด ์ธ์ด๊ฐ์ง(ํ๊ตญ์ด, ์์ด, ์ผ๋ณธ์ด ๋ฑ๋ฑ)
* ๋ธ๋ ๊ฐ์ฌ๋ฅผ ๋ค์ด๋ฒ ๋ฒ์ญ API๋ฅผ ํตํด ๋ฒ์ญํ ํ, ์ฌ์ฉ์์๊ฒ ์ ์ก

### 2-2. ์ฌ์ฉ ๋ฐฉ๋ฒ
1. ๋ธ๋ ์ ๋ชฉ ์๋ ฅ
2. ๊ธฐ๋ค๋ฆผ

### 2-3. ๊ฐ๋ฐ ํ๊ฒฝ
+ Python 3.9.13
+ Selenium 4.3.0
+ Requests 2.28.1
+ time
+ json

### 2-4. API List
+ NAVER ์ธ์ด๊ฐ์ง API
+ NAVER Papago ๋ฒ์ญ API

## 3. ๋น๋๋ฐฉ๋ฒ
### 3-1. Api Key ๋ฐ๊ธ
+ https://developers.naver.com/main/ ์์ NAVER ์ธ์ด๊ฐ์ง, NAVER Papago ๋ฒ์ญ API ๋ฐ๊ธ

### 3-2. git clone
git clone ํด์ฃผ์ธ์

```
git clone https://github.com/kyungcom/music-translate.git
```
### 3-3. chrome driver ์ค์น
![image](https://user-images.githubusercontent.com/72953874/183106356-eb42ebfc-e36a-40cd-adef-b9ca4b1a94df.png)

```
https://chromedriver.chromium.org/downloads
```
์์ ๋ณธ์ธ ๋ฒ์ ์ ๋ง๋ ํฌ๋กฌ๋๋ผ์ด๋ฒ๋ฅผ ๋ค์ด๋ก๋ ๋ฐ ์์ถํด์  ํ, searchMusic.py๊ฐ ์๋ ํด๋์ ๋ฃ์ด์ฃผ์ธ์.


### 3-4. config.py ํ์ผ ์ค์ 
config.py ํ์ผ์ ๋ง๋ค๊ณ 
```
CLIENT_ID = ?
CLIENT_SECRET = ?
```
? ๊ฐ์ ์ฑ์์ฃผ์ธ์.

translate.py๋ฅผ ์คํํ์๋ฉด ๋์๋๋ค.

## ์คํ๊ฒฐ๊ณผ
![image](https://user-images.githubusercontent.com/72953874/183108081-68d740c4-579a-4ac8-a358-0961ac99d700.png)

![image](https://user-images.githubusercontent.com/72953874/183108481-ba8cf704-78bb-4629-8684-37a9f51a7f15.png)



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