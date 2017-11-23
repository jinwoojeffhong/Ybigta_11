
# coding: utf-8

# In[225]:


import pandas as pd
import cufflinks as cf
cf.go_offline()


# In[287]:


mk = pd.read_csv("C:\\Users\\Jeff Hong\\Desktop\\[MKA]Project\\facebook.csv", 
                 encoding="utf-8")


# # Preprocessing
# ----

# ## 1.Null값 확인
# ---
# 

# In[289]:


mk.isnull().sum() 


# ## 2. 컬럼네임--> 카멜표기법
# ----

# In[290]:


#컬럼네임 카멜표기법으로 바꿔주기
clist=[]
for col in mk.columns :
    col_tune = col.replace(" ","")
    clist.append(col_tune)
    
mk.columns=clist
print(mk.columns)


# ## 3. 데이터 타입 --> 날짜형식으로 변환 및 "요일(Day)"컬럼 생성
# ---

# In[291]:


# ReportinsStarts, ReportingEnds, Ends 날짜 형식으로 바꿔주기
type(mk.ReportingStarts[1]),type(mk.ReportingEnds[1]),type(mk.Ends[1])


# In[292]:


## End 컬럼의 "진행 중"항목을 날짜로 표시(2017-02-12)
mk.loc[lambda x: x["Ends"]=="진행 중","Ends"] ="2017-02-12"


## 데이터 형식을 날짜 형식으로 변환
import datetime
for i in range(len(mk["ReportingStarts"])) :
    mk.loc[i, "ReportingStarts"] = datetime.datetime.strptime(mk.loc[i,"ReportingStarts"],"%Y-%m-%d").date()

for i in range(len(mk["ReportingEnds"])) :
    mk.loc[i, "ReportingEnds"] = datetime.datetime.strptime(mk.loc[i,"ReportingEnds"],"%Y-%m-%d").date()


for i in range(len(mk["Ends"])) :
    mk.loc[i, "Ends"] = datetime.datetime.strptime(mk.loc[i,"Ends"],"%Y-%m-%d").date()
print(""" -------------------------
ReportingStarts 의 데이터 형식은 {}입니다.
ReportingEnds의 데이터 형식은 {}입니다.
Ends의 데이터 형식은 {}입니다""".format(type(mk.loc[1,"ReportingStarts"]),type(mk.loc[1,"ReportingEnds"]),type(mk.loc[1,"Ends"])))


# In[293]:


## 요일 컬럼 추가
## weekday : 0-Monday,6-Sunday
day ={0 : "Mon" , 1: "Tue" , 2 : "Wed", 3 : "Thu" , 4 : "Fri" , 5 : "Sat" , 6 : "Sun"}
mk["Day"] =0 
for i in range(len(mk)) :
    mark = mk.loc[i,"ReportingStarts"].weekday()
    mk.loc[i,"Day"] = day[mark]


# In[294]:


## 서로다른 날짜의 캠페인 구분을 위한 엑셀 작업을 위해 일단 여기서 export!
import csv
mk.to_csv("fb_before.csv") ## 절대 utf-8 하지 말 것. 한글이 뻑남


# ----
# # --------Excel 로 작업하는중---------- 
# 
# ---

# ## 4. "시차(Duration)"컬럼 추가

# In[311]:


mk1 =pd.read_csv("C:\\Users\\Jeff Hong\\Desktop\\[MKA]Project\\fb_before.csv",
                                encoding="cp949",
                                index_col="Unnamed: 0")


# In[312]:


mk1.head(10)


# In[313]:


i = 0
j= 1
while i < len(mk1) :
    if mk1.loc[i,"Change"] == 0 :
        mk1.loc[i,"Change"] = j
        j=j+1
    elif mk1.loc[i,"Change"] == 1 :
        j=1
        mk1.loc[i,"Change"] = j
        j=j+1
    
    i=i+1


# In[314]:


mk1.Change.isnull().sum()


# In[315]:


mk1.head(15)


# # 5.ReportingStarts,Ends 컬럼 --> Date컬럼으로 바꾸고, Change-->Duration

# In[316]:


## ReportingStarts,ReportingEnds --> Date컬럼으로 바꿈
mk1.columns = ['Date', 'ReportingEnds', 'Countries', 'Campaigns',
       'Categories', 'Delivery', 'Results', 'ResultIndicator', 'Reach',
       'CostperResults', 'AmountSpent(KRW)', 'Ends', 'Day', 'Duration']

del mk1["ReportingEnds"]


# In[317]:


mk.Categories.unique()


# # 6.Categories 재분류 --> "Promotion type" 새로운 컬럼 생성
# 
# ----
# 
# 1. Reward promotion : 참여하면 보상을 주는 프로모션
#     - 1. GS25 Promotion : 
#     - 1. Restaurant Promotion :
#     - 3. Everland Promotion 
#     - 4. Airline Promotion : 
#     - 5. Referral event : 추천인 코드 입력되면 경품 당첨
# 2. Advertising promotion : 광고성 홍보
#     - 6. Branding : 브랜딩은 브랜딩
#     - 7. Seasonal Day : 명절을 축하하거나 공지해주는 포스팅
#     - 8. Information of Sentbe :
#     - 9. Review : 사용자 경험 인터뷰
#     - 10. Page Boost : 회사 서비스 사용법 포스팅
#     - 11. Booth Promotion : 외국인 노동자들 거주 밀집 지역에서 진행하는 가입행사 안내
# 3. Nan-advertisng promotion : 비광고성 홍보
#     - 12. Tip of the Day
# 4. techincal promotion : 서비스 결함시 공지
#     - 13. Troubleshooting 
#     
# ----

# In[318]:


rp = ['GS25 Promotion', 'Restaurant Promotion', 'Everland Promotion', 'Airline Promotion', 'Referral event']
ap = [ 'Booth Promotion', 'Seasonal Day', 'Branding',  'Information of Sentbe', 'Review', 'Page Boost']
np = ["Tip of the Day"]
tp = ["Troubleshooting"]


# In[319]:


mk1["Promotion_type"]=0

for i in range(len(mk)) :
    if mk1.loc[i,"Categories"] in rp :
        mk1.loc[i,"Promotion_type"]="rp"
    elif mk1.loc[i,"Categories"] in ap :
        mk1.loc[i,"Promotion_type"]="ap"
    elif mk1.loc[i,"Categories"] in np :
        mk1.loc[i,"Promotion_type"]="np"
    else :
        mk1.loc[i,"Promotion_type"]="tp"


# In[320]:


mk1.head()


# # 6. 광고효과 산정 : Efficiency( = Reach/Result) 변수 생성

# In[321]:


mk1["Effect"] = mk1["Reach"]/mk["Results"]


# In[322]:


mk1.head()


# # 7. KR페이지 제거

# In[323]:


mk1 = mk1[lambda x: x.Countries !="KR"]


# # 8. Final : import csv

# In[325]:


import csv
mk1.to_csv("fb_final.csv")


# ----

# ## 국가별, 요일별 효과적인 광고 분석
# ---
# - "효과적이다"의 정의에 대한 고민이 필요함
# - 국가별 베스트 프로모션을 뽑기
# - 전처리
#     - 날짜들을 기반으로 요일 표시(0)
#     - 요일 컬럼 추가(0)

# In[18]:


## 나라별 카테고리 수
for country in mk.Countries.unique() :
    number = len(mk[lambda x: x.Countries==country]["Categories"].unique())
    print("{}의 카테고리 수는 {}개 입니다".format(country,number))


# In[19]:


mk["effective"] = round(mk["Results"]/(mk["Reach"]+mk["Results"]) * 100,2)


# In[20]:


## 요일별로 프로모션의 CostperResults
(
    mk.groupby(["Day"])["Reach"]
        .mean()
        .iplot(kind= "scatter", mode = "markers")
)


# In[145]:


## 요일별로 프로모션의 CostperResults
(
    mk.groupby(["Day","Categories"])["effective"]
        .mean()
        .unstack()
        .fillna(0)
        .iplot(kind= "scatter", mode = "markers")
)


# In[141]:


## 국가별로 진행한 프로모션들의 CostperResult
(
    mk.groupby(["Categories","Countries"])["Reach"]
        .mean()
        .unstack()
        .iplot(kind="scatter",mode="markers")
)


# ## 적정기간 광고분석
# -----

# In[21]:


mk.head()


# In[22]:


mk.Campaigns.unique()


# ## Action Type 별 부석(Result Indicator)

# In[23]:


mk.columns


# In[25]:


mk.ResultIndicator.unique()


# In[26]:


mk.head()


# In[27]:


df1 = mk.groupby(["ResultIndicator"])[["Reach","Results","CostperResults"]].mean()
df1["pct"] = df1["Reach"]/(df1["Reach"]+df1["Results"])
df1.iplot(kind="scatter",mode="markers")

