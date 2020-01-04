"""
    拉取爬虫数据
"""
#!usr/bin/python3
#-*- coding:UTF-8 -*-
from urllib import request

import re

response = request.urlopen('https://movie.douban.com/')
content = response.read().decode('utf-8')
print(content)

class MovieTop(object):
    def __init__(self):
        self.start = 0
        self.param = "&filter="
        self.headers={}
        self.movie_list=[]
        self.file_path = ''  # 文件路径 file path

    def get_page(self):
        try:
            req = request.Request('https://movie.douban.com/top250?start=' + str(self.start),headers=self.headers)
            response = request.urlopen(req)
            page = response.read().decode('utf-8')
            page_num = (self.start+25)//25
            print('正在抓取第'+str(page_num)+'页数据...')
            self.start+=25
            return page

        except request.URLError as e:
              if hasattr(e,'response'):
                 print('获取失败，失败原因：',e.reason)
        pass

    def get_movie_info(self):
        while self.start <= 225:
            page = self.get_page()
            pattern = re.compile(u'<div.*?class="item">.*?'+'</div>')
            movies = re.findall(pattern,page)
            for movies in movies:
                self.movie_list.append(movies[0])


        pass

    def write_text(self):
        print('向文件中写入数据.....')
        file_top = open(self.file_path,'w',encoding='utf-8')
        try:
            for moive in self.movie_list:
                file_top.write('电影排名：'+moive[0]+'\r\n')
                file_top.write('电影排名：'+moive[0]+'\r\n')
                file_top.write('电影排名：'+moive[0]+'\r\n')
                file_top.write('电影排名：'+moive[0]+'\r\n')
            print('抓取数据写入文件成功.....')
        except Exception as e:
             print(e)
        finally:
             file_top.close()
        pass

    def main(self):
        print('开始拉取电影的抓取数据了....')
        self.get_movie_info()
        self.write_text()
        print('数据拉取完成.....')

if __name__ == '__main__':
     movietop = MovieTop()
     movietop.main()