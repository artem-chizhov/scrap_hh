from hh_class import Hh_scrap as HH
import json
import time

if __name__ == '__main__':
    site_url = 'https://hh.ru/search/vacancy?&order_by=publication_time&area=1&area=2&text=python'

    url_vacancy = []
    result_dict = {}

    get_url_vacancy = HH().find_all_soup(site_url,'a','serp-item__title')
    
    for data in get_url_vacancy:
        if data.get('href') is not None:
            url_vacancy.append(data.get('href'))

    for k_url in url_vacancy:
        
        description = HH().find_soup(k_url,'div',{'class':'vacancy-section'})

        if description.lower().find('django') is not -1 or description.lower().find('flask') is not -1:
            if HH().find_soup(k_url,'span', {'data-qa':'vacancy-view-raw-address'}) is None:
                city = HH().find_soup(k_url,'p', {'data-qa':'vacancy-view-location'})
            else:
                city = HH().find_soup(k_url,'span', {'data-qa':'vacancy-view-raw-address'})
            time.sleep(2)    
            name_vacancy = HH().find_soup(k_url, 'h1', {'data-qa':'vacancy-title'})
            time.sleep(2)  
            salary = HH().find_soup(k_url, 'div', {'data-qa':'vacancy-salary'})
            time.sleep(2)
            company = HH().find_soup(k_url,'a', {'data-qa':'vacancy-company-name'})
            time.sleep(2)  
            metro = HH().find_soup(k_url,'span','metro-station')
        else:
            continue

        result_dict[k_url] = {'name_vacancy':name_vacancy,
                              'City':city, 
                              'metro':metro, 
                              'Salary':salary, 
                              'company':company, 
                              'description':description}
        
    for item in result_dict.items():
        result_dict[item[0]] = str(item[1]).replace(r'\xa0', ' ')

    with open ('request.json', 'w', encoding='utf-8') as file:
        json.dump(result_dict, file, ensure_ascii=False)
