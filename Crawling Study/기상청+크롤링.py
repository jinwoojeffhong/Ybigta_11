
def WeatherCrawl(url) :
    
    from urllib.request import urlopen
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    
    html = urlopen(url)
    crawler = bs(html.read(), "html.parser")
    
    data = []
    for tr in crawler.find("table", {"class" : "table_develop3"}).findAll("tr") :  ## table_develop3 라는 class를 가진 table 안의 tr들을 찾음

        tds = list(tr.findAll("td")) ## tr 밑의 td 태그들을 리스트로 묶어줌

        for td in tds :
            if td.find('a') :  ##head부분에는 a 태그가 없는 반면 body 부분(내용)에는 a 태그가 있으메 착안
                place = td.a.text  ##a 태그의 내용만을 가져오겠다
                temparature = tds[5].text
                wind = tds[12].text

                data.append([place, temparature, wind])
                
                
    import pandas as pd
    weather = pd.DataFrame(data, columns = ["place","temparature", "wind"])
    print("파일이 생성되었습니다")
    
    
    from datetime import datetime
    today = str(datetime.today())
    filename = "Weather{}".format(today[0:10])
    print("파일명 : {}".format(filename))
    
    
    import csv
    weather.to_csv("{}.csv".format(filename), encoding = "cp949")
