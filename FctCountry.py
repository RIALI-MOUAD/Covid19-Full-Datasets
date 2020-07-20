
import pandas as pd
import datetime



def listeDates(s,f):
    D=[]
    start = s
    end = f
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    for date in date_generated:
        D.append(date.strftime("%Y-%m-%d"))
    return D


def Fonction(s,f,m):
    L=listeDates(s,f)

    #L=['2020-05-0'+str(j) for j in range(1,10)]+['2020-05-'+str(j) for j in range(10,32)]+['2020-06-0'+str(j) for j in range(1,10)]+['2020-06-'+str(j) for j in range(10,31)]+['2020-07-0'+str(j) for j in range(1,10)]+['2020-07-'+str(j) for j in range(10,15)]
    df=pd.DataFrame(columns=['Date','Tot cases','New cases','Tot Deaths','New Deaths','Total Recovered','Active Cases','Serious','Tot C par million','Deaths par million','Total Test','Tot T par million'])
    M=pd.DataFrame(columns=['Date','Tot cases','New cases','Tot Deaths','New Deaths','Total Recovered','Active Cases','Serious','Tot C par million','Deaths par million','Total Test','Tot T par million'])
    for i in L:
        base=pd.read_csv("fichier_base"+i+".csv")
        Mor=base.where(base['Country']=='Morocco').dropna()
        df=df.append(Mor,ignore_index = True)
    
    df['Date']=L
    df.to_csv("MarocStat-"+m+".csv")

    
    
    
    
def FonctionCountry(s,f,m):
    L=listeDates(s,f)

    #L=['2020-05-0'+str(j) for j in range(1,10)]+['2020-05-'+str(j) for j in range(10,32)]+['2020-06-0'+str(j) for j in range(1,10)]+['2020-06-'+str(j) for j in range(10,31)]+['2020-07-0'+str(j) for j in range(1,10)]+['2020-07-'+str(j) for j in range(10,15)]
    df=pd.DataFrame(columns=['Date','Tot cases','New cases','Tot Deaths','New Deaths','Total Recovered','Active Cases','Serious','Tot C par million','Deaths par million','Total Test','Tot T par million'])
    M=pd.DataFrame(columns=['Date','Tot cases','New cases','Tot Deaths','New Deaths','Total Recovered','Active Cases','Serious','Tot C par million','Deaths par million','Total Test','Tot T par million'])
    for i in L:
        base=pd.read_csv("fichier_base"+i+".csv")
        Mor=base.where(base['Country']==m).dropna()
        df=df.append(Mor,ignore_index = True)

    
    df['Date']=L
    df['New Recov'] = df['New Recov'].fillna(0)
    df.to_csv("CovPerCountry//csv//Stat-"+m+".csv")
    df.to_json("CovPerCountry//json//Stat-"+m+".json")
    

L=list(pd.read_csv("fichier_base2020-07-15.csv")['Country'])


s=datetime.datetime.strptime("2020-05-02", "%Y-%m-%d")
f=datetime.datetime.today()
for Country in L:
    print(Country)
    try :
        FonctionCountry(s,f,Country)
    except :
        continue
