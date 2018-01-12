def AuctionCrawl(url) :
    from urllib.request import urlopen
    from bs4 import BeautifulSoup as bs
    
    html = urlopen(url)
    crawler = bs(html.read(), "html.parser")
    
    
    import pandas as pd
    df = pd.DataFrame()
    rank_list =[]
    product_list = []
    
    
    for child1 in crawler.find("div",{"id" : "itembest_T"}).findAll("ul",{"class" : "uxb-img"}) :
        for child2 in child1.findAll("li") :

            if child2.find("div",{"class" : "rank"}) is None :
                continue
            rank = child2.find("div",{"class" : "rank"}).text
            rank_list.append(rank)
            #print(rank)

            if child2.find("a") is None :
                continue
            product = child2.find("em").text
            product_list.append(product)        
            #print(product)

    df["rank"] = rank_list
    df["product"] = product_list
    print("파일이 생성되었습니다")
    
    
    from datetime import datetime
    today = str(datetime.today())
    
    filename = "Auction{}".format(today[:10])
    print("파일명 : {}".format(filename))
    
    import csv
    df.to_csv("{}.csv".format(filename), encoding = "cp949")
    
    
    return df
        
