import redis

r = redis.Redis(host = '39.106.67.151', port = '6379', db= 0)
dupset = r.smembers('JDSpider:dupefilter')
dublist = list(dupset)
f = open('JDSpider:dupfilter.txt', 'wb')
for x in range(len(dublist)):
    if x // 10000 == 0:
        f = open('JDSpider:dupfilter' + str(x/10000) + '.txt','wb')
    f.writelines(dublist[x])
#print(duplist)