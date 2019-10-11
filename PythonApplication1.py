
def CardHua(Cards):    #判断花色相同的情况，much代表需要判断几张同花（much为3或者5） 黑桃 红桃草花方块
    for i in range(1,5) :
        for j in range(2,15) :
                if card[i][j] == 1 :
                    sum=sum+1
        Cards[i][15]=sum
    return Cards; 
def CardTHua(Cards,much) :
    for i in range(4,0,-1) :
        if Cards[i][15]>=much :
            return i    #返回我手上是什么颜色的同花 若不符合much的要求，则返回0
            break
        else:
            return 0
            break
def CardsDel(Cards,much,ij,Type):#删行1,列0
    if Type == 1:
        for time in range(0,much) :
            for j in range(14,1,-1):
                if Cards[ij][j]==1 :
                    Cards[ij][j]==0
    if Type == 0:
        for time in range(0,much) :
            for i in range(4,0,-1):
                if Cards[i][ij]==1 :
                    Cards[i][ij]==0



#至尊青龙
def CardsZZQL(Cards) :
    pd=0
    for i in range(4,0,-1):
        for j in range(2,15):
            if Cards[i][j]==1 :
                pd=pd+1
        if pd==13 :
            return 1    #青龙
            break
        else:
            pd=0
    if pd != 13:
        return 0

#一条龙
def CardsYTL(Cards) :
    pd=0
    pdd=0
    for j in range(2,15):
        for i in range(4,0,-1):
            if Cards[i][j]==1 :
                pd=1
        if pd==1 :
            pdd=pdd+1
        pd=0
    if(pdd==13):
        return 1
    else:
        return 0

#十二皇族
def CardsSEHZ(Cards) :
    pd=1
    for j in range(11,15):
        for i in range(4,0,-1):
            if Cards[i][j]==1 :
                pd=0
                return 0
                break
    if pd==1:
        return 1
 
#全大8-14
def CardsQD(Cards):
    pd=1  #先假设是拳大
    for j in range(2,8):#除去8-A
        for i in range(4,0,-1):
            if Cards[i][j]==1 :
                pd=0
                return 0
                break
    if pd==1:
        return 1

#全小2-8
def CardsQX(Cards):
    pd=1
    for j in range(9,15):#9-A
        for i in range(4,0,-1):
            if Cards[i][j]==1 :
                pd=0
                return 0
                break
    if pd==1:
        return 1

#凑一色（放在最后便历）
def CardsCYS(Cards):
    ye=0
    ss=0
    for j in range(9,15):#9-A
        for i in range(4,0,-1):
            if Cards[i][j]==1 :
                pd=0
                return 0
                break
    if pd==1:
        return 1



                
    

