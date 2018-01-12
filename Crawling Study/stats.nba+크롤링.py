
def nbaCrawl(url) :
    
    from urllib.request import urlopen
    from bs4 import BeautifulSoup as bs
    import pandas 
    
    
    import json
    html = urlopen(url)
    file = json.load(html)
    
    
    import pandas as pd
    nba = pd.DataFrame(file["resultSet"]["rowSet"])
    nba.columns = file["resultSet"]["headers"]
    print("파일이 생성되었습니다")
    
    
    from datetime import datetime
    today = str(datetime.today())
    filename = "nba{}".format(today[0:10])
    print("파일명 : {}".format(filename))
    
    import csv
    nba.to_csv("{}.csv".format(filename), encoding = "cp949")
    


