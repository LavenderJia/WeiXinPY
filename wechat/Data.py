# coding=utf-8
from .Model import *
import pymysql
from mitmproxy import ctx

class DataService(object):
    """
    数据层接口，不同数据库可分别实现
    """

    def update_msg(self, msg: Msg):
        """
        保存文章信息（若存在则更新）
        :param msg:
        """
        pass

    def save_content(self, content: Content):
        """
        保存文章内容
        :param content:
        :return:
        """
        pass

    def save_comment(self, comment: Comment):
        """
        保存评论内容
        :param comment:
        :return:
        """
        pass

    def get_uncrawled_link(self):
        """
        获取未抓取的文章的url
        :return:返回未抓取的文章的信息，格式为{id:'', link:''}
        """
        pass



class MySqlImpl(DataService):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "Lavender124", "wechat")

    def update_msg(self, msg: Msg):
        cursor =  self.db.cursor()
        sql = "UPDATE tmp_uncrawled_articles SET read_num = '%d', like_num = '%d',\
         reward_num = '%d', WHERE id = '%d'" % \
              (msg.read_num, msg.like_num, msg.reward_num, msg.id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def save_content(self, content: Content):
        #ctx.log(content.msg_id)
        ctx.log(content.crawled_time)
        cursor = self.db.cursor()
        pymysql.escape_string("'")
        sql1 = "INSERT INTO content(msg_id, content, crawled_time) VALUES ('%d', \'%s\', '%s')" % (content.msg_id, pymysql.escape_string(content.content), content.crawled_time)
        sql2 = "UPDATE tmp_uncrawled_articles SET content_gotten = 1 WHERE id = '%d'" % content.msg_id

        try:
            # 执行SQL语句
            cursor.execute(sql1)
            cursor.execute(sql2)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            ctx.log(str(e))

    def save_comment(self, comment: Comment):
        cursor = self.db.cursor()
        sql = "INSERT INTO comment(msg_id, user_name, content, create_time, \
        like_num, is_from_friend, is_from_me, is_top, reply) VALUES ('%d', '%s', '%s', '%s', \
        '%d', '%d', '%d', '%d', '%s')"%(comment.msg_id, comment.user_name, comment.content, comment.create_time, \
                                        comment.like_num, comment.is_from_friend, comment.is_from_me, comment.is_top, comment.reply)


        try:
            # 执行SQL语句
            cursor.execute(sql)
             # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
             self.db.rollback()

    def get_uncrawled_link(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM tmp_uncrawled_articles WHERE content_gotten is null LIMIT 1"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = cursor.fetchone()
            msg = Msg()
            msg.id = result[0]
            msg.msg_link = result[2]
            return msg
        except:
           pass




