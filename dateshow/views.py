from django.shortcuts import render

from dateshow.models import *

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    productmessage,catecountlist,userclientlist,ismobilelist = [],[],[],[]
    productname,reallyprice,originalprice = [],[],[]
    commentsummaryidlist,commentsummarycountlist = [],[]
    memberleve = []
    ismobilecount = []
    comment = Comment.objects
    product = Products.objects
    commentsummary = CommentSummary.objects
    userclient = comment.distinct('userClientShow')
    ismobile = comment.distinct('isMobile')
    member = comment.distinct('userLevelName')
    catecount = product.distinct('category')
    for comm in commentsummary:
        commentsummaryidlist.append(comm['productId'])
        commentsummarycountlist.append(comm['commentCount'])
    for mem in member:
        a = comment.filter(userLevelName = mem).count()
        memberleve.append({'value':a, 'name':mem})
    for producesin in product:
        productname.append(producesin['name'])
        reallyprice.append(int(producesin['reallyPrice'].split('.')[0]))
        originalprice.append(int(producesin['originalPrice'].split('.')[0]))
    for im in ismobile:
        a = comment.filter(isMobile = im).count()
        if im == True:
            ismobilecount.append({'value':a,'name':'来自移动端'})
            ismobilelist.append('来自移动端')
        elif im == False:
            ismobilecount.append({'value':a,'name':'来自网页'})
            ismobilelist.append('来自网页')
    for i in userclient:
        a = comment.filter(userClientShow = i).count()
        if i == '':
            ind = userclient.index('')
            userclient.pop(ind)
            userclient.insert(ind, '来自网页')
            i = '来自网页'
        userclientlist.append({'value':a,'name':i})
    context = {
        'userclient':userclient,
        'userclientlist':userclientlist,
        'ismobilecount':ismobilecount,
        'catecount':len(catecount),
        'productname':productname,
        'originalprice':originalprice,
        'reallyprice':reallyprice,
        'member':member,
        'memberleve':memberleve,
        'commentsummaryidlist':commentsummaryidlist,
        'commentsummarycountlist':commentsummarycountlist
    }
    return render(request, 'index.html', context)

def table_cate(request):
    categories = Categories.objects
    paginator = Paginator(categories,15)
    page_num = int(request.GET.get('page', 1))
    categoriescontext = paginator.page(page_num)
    if paginator.num_pages > 7:
        if page_num - 3 < 1:
            page_ran = range(1,8)
        elif page_num + 3 > paginator.num_pages:
            page_ran = range(paginator.num_pages - 6,paginator.num_pages + 1)
        else:
            page_ran = range(page_num - 3, page_num + 4)
        page_range = page_ran
    else:
        page_range = paginator.page_range
    context = {
        'categoriescontext':categoriescontext,
        'paginator':paginator,
        'page_range':page_range
    }
    return render(request, 'table_cate.html', context)

def table_product(request):
    products = Products.objects
    paginator = Paginator(products , 15)
    page_num = int(request.GET.get('page',1))
    productcontext = paginator.page(page_num)
    if paginator.num_pages > 7:
        if page_num - 3 < 1:
            page_ran = range(1,8)
        elif page_num + 3 > paginator.num_pages:
            page_ran = range(paginator.num_pages - 6,paginator.num_pages + 1)
        else:
            page_ran = range(page_num - 3, page_num + 4)
        page_range = page_ran
    else:
        page_range = paginator.page_range
    context = {
        'productcontext':productcontext,
        'paginator':paginator,
        'page_range':page_range
    }
    return render(request, 'table_product.html', context)

def search(request):
    products = Products.objects
    categories = Categories.objects
    changecontext = request.GET.get('search')
    print(changecontext)
    print('*' * 20)
    if changecontext == '1':
        cate(request)
    elif changecontext == '2':
        product(request)

def cate(request):
    return render(request, 'cate.html')

def product(request):
    return render(request, 'product.html')