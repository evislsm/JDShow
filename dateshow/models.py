from django.db import models

# Create your models here.
from mongoengine import *

class Categories(Document):
    _id = StringField()
    name = StringField()
    url = StringField()
    meta = {'collection':'Categories'}

class Comment(Document):
    _id = StringField()
    productId = StringField()  # 同ProductsItem的id相同
    guid = StringField()
    content = StringField()
    creationTime = StringField()
    isTop = StringField()
    referenceId = StringField()
    referenceName = StringField()
    referenceType = StringField()
    referenceTypeId = StringField()
    firstCategory = StringField()
    secondCategory = StringField()
    thirdCategory = StringField()
    replyCount = StringField()
    score = StringField()
    status = StringField()
    title = StringField()
    usefulVoteCount = StringField()
    uselessVoteCount = StringField()
    userImage = StringField()
    userImageUrl = StringField()
    userLevelId = StringField()
    userProvince = StringField()
    viewCount = StringField()
    orderId = StringField()
    isReplyGrade = StringField()
    nickname = StringField()
    userClient = StringField()
    mergeOrderStatus = StringField()
    discussionId = StringField()
    productColor = StringField()
    productSize = StringField()
    imageCount = StringField()
    integral = StringField()
    userImgFlag = StringField()
    anonymousFlag = StringField()
    userLevelName = StringField()
    plusAvailable = StringField()
    recommend = StringField()
    userLevelColor = StringField()
    userClientShow = StringField()
    isMobile = StringField()
    days = StringField()
    afterDays = StringField()
    meta = {'collection':'Comment'}


class CommentImage(Document):
    _id = StringField()
    associateId = StringField()  # 和CommentItem的discussionId相同
    productId = StringField()  # 不是ProductsItem的id，这个值为0
    imgUrl = StringField()
    available = StringField()
    pin = StringField()
    dealt = StringField()
    imgTitle = StringField()
    isMain = StringField()
    meta = {'collection':'CommentImage'}


class CommentSummary(Document):
    _id = StringField()
    goodRateShow = StringField()
    poorRateShow = StringField()
    poorCountStr = StringField()
    averageScore = StringField()
    generalCountStr = StringField()
    showCount = StringField()
    showCountStr = StringField()
    goodCount = StringField()
    generalRate = StringField()
    generalCount = StringField()
    skuId = StringField()
    goodCountStr = StringField()
    poorRate = StringField()
    afterCount = StringField()
    goodRateStyle = StringField()
    poorCount = StringField()
    skuIds = StringField()
    poorRateStyle = StringField()
    generalRateStyle = StringField()
    commentCountStr = StringField()
    commentCount = StringField()
    productId = StringField()  # 同ProductsItem的id相同
    afterCountStr = StringField()
    goodRate = StringField()
    generalRateShow = StringField()
    jwotestProduct = StringField()
    maxPage = StringField()
    score = StringField()
    soType = StringField()
    imageListCount = StringField()
    meta = {'collection':'CommentSummary'}


class HotCommentTag(Document):
    _id = StringField()
    name = StringField()
    status = StringField()
    rid = StringField()
    productId = StringField()
    count = StringField()
    created = StringField()
    modified = StringField()
    type = StringField()
    canBeFiltered = StringField()
    meta = {'collection':'HotCommentTag'}


class Products(Document):
    name =  StringField() # 产品名称
    url = StringField()  # 产品url
    _id = StringField()  # 产品id
    category = StringField()  # 产品分类
    reallyPrice = StringField()  # 产品价格
    originalPrice = StringField()  # 原价
    description = StringField() # 产品描述
    shopId = StringField()  # shop id
    venderId = StringField()  # vender id
    commentCount = StringField()  # 评价总数
    goodComment = StringField()  # 好评数
    generalComment = StringField()  # 中评数
    poolComment = StringField()  # 差评数
    favourableDesc1 = StringField()  # 优惠描述1
    favourableDesc2 = StringField()  # 优惠描述2
    meta = {'collection':'Products'}


class Shop(Document):
    _id = StringField()  # 店铺名称
    name = StringField()  # 店铺名称
    url1 = StringField()  # 店铺url1
    url2 = StringField()  # 店铺url2
    shopId = StringField()  # shop id
    venderId = StringField()  # vender id
    meta = {'collection':'Shop'}

