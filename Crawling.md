# **Crawling**

----


## **1.Crawling Type**
1. 바로 긁어올 수 있는 웹사이트 
2. 바로 긁어올 수 없는 웹사이트


----


## **2. Process**
Step1. 정보를 얻고 싶은 싶은 웹페이지 지정
Step2. 크롤러 생성
Step3. 태그를 이용해 웹페이지에서 원하는 정보만을 크롤


---


### **Step1. Webpage indication**

- urllib 패키지의 request모듈를 이용하여 urlopen함수를 가져옴.
- urlopen() : webpage를 html 형식으로 반환


----


#### **네이버 영화정보 가져오기**
> from urllib.request import urlopen <br>
> html= urlopen("http://movie.naver.com/movie/running/current.nhn#")

### **Step2. Creating Crawler**

- BeautifulSoup : 크롤러 생성 함수, bs4패키지에서 import 가능
- html_parser 
	- 어떤 방식으로 crawl을 해올 것인지에 관한 파라미터
	- html_parser는 "html 문법으로 불러 오겠다" 라는 의미



>pip3 install beautifulsoup4<br>
>from bs4 import BeautifulSoup <br>
>crawler = BeautifulSoup(html, "html_parser")

### **Step3. 웹페이지에서 원하는 정보만 크롤링**

- 목표 : 페이지에서 영화 제목만 크롤링 하고 싶음.

- crawler를 돌려보면 해당 html이 텍스트 형식으로 출력됨.
- 웹페이지의 정보를 담고 있는 crawler를 find 혹은 findAll을 이용하여<br>
내가 원하는 정보만 출력하고자 함.

	- find(tag, attribute, recursive, text, keyword) 
	- findAll(tag, attribute, limit, recursive, text, keyword)

- 여기서 **limit** 는 내가 원하는 태그를 몇개 찾을 것인지 지정하는 것인데, find는 limit=1이라고 생각하면 됨.

-tag 정보를 이용해서 크롤러로 tag에 접근

>for ul_tag in crawler.findAll("ul", {"class":"current_list"}) :<br>
>print(ul_tag)

**인사이트**
>len(crawler.**find**("ul", {"class": "current_list"}))<br>
> 41<br>
>len(crawler.**findAll**("ul", {"class":"current_list"})) <br>
>1

- **current_list** 라는 **클래스(attribute)** 를 가진 **"ul"** 를 크롤링하는 것.
-  이 ul 태그 안에는 여러 li들을 가지고 있는데  find의 경우에는 li들의 갯수가 측정됨.
- 반면 findAll은 리스트 형식으로 반환하기 때문에 길이가 1로 측정됨.

---
- ctrl + u : element source 전체 화면 띄우기
- ctrl + shift + i : webpage element, network 보기

---

- 영화정보 가져오기
>for child in crawler.find("ul", {"class": "current_list"}).findAll("li"):<br>
>print(child.find("a").get("title"))

- 41개 각각의 li들 별로, li들의 a 라는 tag를 찾아서 title이라는 attribute만을 반환해라
라는 의미

Output :
토르: 라그나로크
침묵
부라더
범죄도시
너의 췌장을 먹고 싶어
지오스톰
원스
대장 김창수
남한산성
메소드
블레이드 러너 2049
유리정원
나는 내일, 어제의 너와 만난다
아이 캔 스피크
배드 지니어스
배저로와 친구들: 신비한 모험
잠깐만 회사 좀 관두고 올게
루터
마더!
킹스맨: 골든 서클





