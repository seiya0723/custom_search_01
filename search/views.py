from django.shortcuts import render

# Create your views here.

#クラスベースのビューを作るため
from django.views import View

#スクレイピングのコードをインポート
from . import scraping 


import time

#拒否したいURLのリスト
DENY_URL_LIST   = [ "matome",
                    "sokuho",
                    "2ch",
                    "naver",
                    ]

DENY_TITLE_LIST = [ "コロナ",
                    "ウイルス",
                    ]


#Viewを継承してGET文、POST文の関数を作る
class SearchView(View):

    def get(self, request, *args, **kwargs):

        if "search_word" in request.GET:
            if request.GET["search_word"] != "":

                start_time  = time.time()

                word                    = request.GET["search_word"]

                #検索結果を表示
                link_list,title_list    = scraping.search_google(word)

                #テンプレートで扱いやすいように整形
                data        = []
                link_list_length    = len(link_list)

                #ここで特定URL、タイトルのサイトを除外する。
                for i in range(link_list_length):
                    allow_flag = True

                    for deny in DENY_URL_LIST:
                        if deny in link_list[i]:
                            allow_flag   = False
                            break
                        
                    if allow_flag:
                        for deny in DENY_TITLE_LIST:
                            if deny in title_list[i]:
                                allow_flag   = False
                                break

                    if allow_flag:
                        data.append( { "url":link_list[i] , "title":title_list[i] } )


    
                end_time    = int(time.time() - start_time)

                context = { "search_word"   : word,
                            "data"          : data,
                            "time"          : end_time
                            }

                return render(request,"search/results.html",context)

        return render(request,"search/base.html")

    def post(self, request, *args, **kwargs):

        pass

index   = SearchView.as_view()

