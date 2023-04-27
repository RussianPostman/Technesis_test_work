from lxml import html
import requests

page = requests.get('https://audiobe.ru/muzykalnyj-gipermarket/drums-and-percussion/vic-firth-5a-nova-hickory-black-wood-tip-detail.html')
 
tree = html.fromstring(page.text) 
buyers: list[str] = tree.xpath('//*[@id="sp-component"]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/span[2]')
print(buyers[0].strip())
