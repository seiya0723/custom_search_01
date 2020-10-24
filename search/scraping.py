import sys,bs4,requests


SEARCH_NUM  = "100"
TIMEOUT     = 10
HEADER      = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}


#グーグル検索から検索結果のリストを返す関数
def search_google(words):

    link_list   = []
    title_list  = []

    try:
        url     = "https://www.google.co.jp/search?q="+words+"&num="+SEARCH_NUM+"&start=0"
        result  = requests.get(url, timeout=TIMEOUT, headers=HEADER)

        result.raise_for_status()
    except Exception as e:
        print("ERROR_DOWNLOAD:{}".format(e))
    else:

        soup        = bs4.BeautifulSoup(result.content, 'html.parser')
        links       = soup.select(".rc > div > a")
        titles      = soup.select(".rc > div > a > h3 > span")

        link_list   = [link_tag.get("href") for link_tag in links]
        title_list  = [title_tag.get_text() for title_tag in titles]


        #タイトルとリンクが不一致の場合、
        if len(link_list) != len(title_list):
            return [],[]

    return link_list,title_list
    


def main():

    words   = input("検索ワードを入力してください")
    print(search_google(words))


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nprogram was ended.\n")
        sys.exit()

