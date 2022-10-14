'UTF-8'
import os
import time
        
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
    
def create_repo():
    os.rmdir("dataset")
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.post(url,headers={"User-Agent":"Mozilla/5.0"})
    #print(r.text)
    time.sleep(3)
    if(r.status_code == 200) : return BS(r.content,'html.parser')
    else : return -1

if __name__=="__main__":

    html = get_page('https://www.livelib.ru/reviews/~2#reviews')
    url = 'https://www.livelib.ru/reviews/'

    dataset = dict()
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    html = get_page(url)

    if html == -1 : 
        print("No connection")
        exit()
            print("No connection")
            exit()

    for i in range (1,9999):
        html = get_page(url+'~'+str(i)+'#reviews')
        if html == -1 : break

    marks = list()

        marks = list()

    for item in html.findAll('span',class_='lenta-card__mymark'):
        marks.append(item.text.strip())
        for item in html.findAll('span',class_='lenta-card__mymark'):
            marks.append(item.text.strip())

    names = list()
        names = list()

    for item in html.findAll('a', class_='lenta-card__book-title'):
        names.append(item.text.strip())
        for item in html.findAll('a', class_='lenta-card__book-title'):
            names.append(item.text.strip())

    comments = list()
        comments = list()

    for item in html.findAll('div',id='lenta-card__text-review-escaped'):
        comments.append(item.text.strip())
        for item in html.findAll('div',id='lenta-card__text-review-escaped'):
            comments.append(item.text.strip())

        for j in range(marks.__len__()):
            dataset.update(
                {
                    names[j]:[comments[j],marks[j]]}
            )

    """
    print(marks)
    
    print(names)
@@ -57,6 +79,8 @@ def get_page(url):
    for comment in comments:
        outFile.write(comment.encode('utf-8'))
        outFile.write('\n\n\n'.encode('utf-8'))
    """