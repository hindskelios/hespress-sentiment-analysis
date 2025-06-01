import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save_to_csv(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        commentcontainer = soup.find('ul', class_='comment-list hide-comments')
        if commentcontainer:
            with open('Final_Data.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile,delimiter=';')
                csv_writer.writerow(['Author', 'Date', 'Reaction', 'Comment'])
                for comment in commentcontainer.find_all('div', class_='comment-body'):
                    author_element = comment.find('span', class_='fn heey')
                    date_element = comment.find('div', class_='comment-date')
                    react_num = comment.find('span', class_='comment-recat-number')
                    commenttext_element = comment.find('div', class_='comment-text')
                    if author_element and date_element and react_num and commenttext_element:
                        author = author_element.text.strip()
                        date = date_element.text.strip()
                        likes = react_num.text.strip()
                        commenttext = commenttext_element.text.strip()
                        csv_writer.writerow([author, date, likes, commenttext])
                    else:
                        print("Skipping comment due to missing element(s).")

            print(f"Comments data for {url} has been saved to 'Final_Data.csv'")
        else:
            print(f"No comments found on the page: {url}")
    else:
        print(f"The request for {url} failed with code: {response.status_code}")

# List of URLs to scrape, nous avons choisi de faire une liste manuellemnet car nous n'avons pas des mots specifies pour faire une recherche de ces articles
url_list = [
"https://www.hespress.com/أساتذة-الزنزانة-10-يطلبون-جبر-الضرر‬-1210590.html",
"https://www.hespress.com/بنموسى-النظام-الأساسي-في-المراحل-الأخ-1222930.html",
"https://www.hespress.com/نقابي-عرض-وزارة-التربية-الوطنية-ضعيف-1221413.html",
"https://www.hespress.com/إصلاح-منظومة-التربية-والتكوين-يتصدر-ا-1221446.html",
"https://www.hespress.com/الحكومة-تلغي-عقوبات-النظام-الأساسي-و-1274451.html",
"https://www.hespress.com/تنسيقيات-التعليم-ترفض-تعامل-وزارة-ال-1274092.html",
"https://www.hespress.com/الأسر-ترفض-رهن-التلاميذ-في-لعبة-شد-الح-1271084.html",
"https://www.hespress.com/احتجاج-أمام-وزارة-بنموسى-يهدد-بالتصع-1259407.html",
"https://www.hespress.com/بنموسى-يضع-سيناريوهات-لتعويض-خسائر-أس-1280778.html",
"https://www.hespress.com/تصعيد-الأساتذة-يتواصل-بالمغرب-التنس-1280793.html",
"https://www.hespress.com/نقابة-نسبة-انخراط-نساء-ورجال-التعليم-ف-1281042.html",
"https://www.hespress.com/إضراب-الأساتذة-يتواصل-في-عدة-مؤسسات-رغ-1288568.html",
"https://www.hespress.com/الاحتقان-يخيم-على-قطاع-التربية-رغم-است-1258000.html",
"https://www.hespress.com/بلاغ-رئاسة-الحكومة-بعد-لقاء-نقابات-الت-1257595.html",
"https://www.hespress.com/النقابات-ترد-على-بنموسى-نسبة-المشاركة-1254950.html",
"https://www.hespress.com/النظام-الأساسي-لموظفي-التربية-الوطني-2-1250082.html",
"https://www.hespress.com/ملحقات-وملحقو-التعليم-يطالبون-بالإنص-1226715.html",
"https://www.hespress.com/المصادقة-على-النظام-الأساسي-لموظفي-ال-1238891.html",
"https://www.hespress.com/النظام-الأساسي-لموظفي-التربية-الوطني-1238284.html",
"https://www.hespress.com/فيدرالية-أولياء-التلاميذ-تدعو-إلى-الح-1238853.html"

]
for url in url_list:
    scrape_and_save_to_csv(url)