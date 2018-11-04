# coding=utf-8


class Account(object):

    def __init__(self):
        self.biz = ''  # 公众号id
        self.nickname = ''  # 公众号名称
        self.description = ''  # 公众号描述
        self.head_image = ''  # 公众号头像
        self.weixin_id = None  # 公众号个性id
        self.updated_time = None  # 更新时间


class Msg(object):

    def __init__(self):
        self.id = '' #文章id
        self.title = ''  # 文章标题
        self.msg_link = ''#文章链接
        self.digest = ''  # 文章摘要
        self.author = ''  # 作者
        self.publish_time = ''  # 发布时间
        self.read_num = None  # 阅读量
        self.like_num = None  # 点赞量
        self.reward_num = None  # 赞赏量
        self.comment_num = None  # 评论数量
        self.reward_flag = None  # 能否赞赏 0-否 1-能
        self.comment_flag = None  # 能否评论 0-否 1-能
        self.idx = 0  # 消息序号
        self.biz = ''  # 公众号id
        self.mid = ''  # 消息id
        self.sn = ''  # 随机加密字符串，对于每条消息是唯一的
        #self.content = ''  # 文章内容
        self.source_url = ''  # 阅读原文链接地址
        self.cover = ''  # 封面图片地址
        self.copyright_stat = '',  # 版权信息
        self.copyright = None,
        self.updated_time = ''  # 记录更新时间
        self.content_gotten = 0 #是否已抓到内容

class Content(object):
    def __init__(self):
        self.msg_id = '' #对应msg表中的id
        self.content = '' #文章内容
        self.crawled_time = '' #抓取文章的时间


class Comment(object):
    def __init__(self):
        self.msg_id = '' #对应msg表中的id
        self.user_name = '' #评论人
        self.content = '' #评论内容
        self.create_time = '' #评论时间
        self.like_num = '' #该条评论的点赞数量
        self.is_from_friend = ''#该条评论是否来自朋友
        self.is_from_me = ''#该条评论是否来自于我
        self.is_top = '' #该条评论是否置顶
        self.reply = '' #该条评论的回复
