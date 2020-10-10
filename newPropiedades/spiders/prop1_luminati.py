import scrapy
import json
from newPropiedades.items import NewpropiedadesItem
import re
import random
 
#---
from newPropiedades.gabesmid import  NeukollnBaseSpider
#---
#import brotli  #instalation de bibli brotlipy pour decodage
class PropiedadesSpider(NeukollnBaseSpider,scrapy.Spider):
    name = 'Propiedades_09_part1'
    allowed_domains = ['propiedades.com']
    global nb_erreur,nbr_page_crawler,dict_location,list_user_agents
    nb_erreur,nbr_page_crawler=0,0


#---


    luminati_username = "lum-customer-autobiz-zone-pige_auto_generic_world"
    luminati_password = "rs8y0xdvz2wh"
    luminati_allow_debug = False
#---
    def __init__(self, *args, **kwargs):
        super(PropiedadesSpider, self).__init__(*args, **kwargs)
                        # ...


    def response_is_ban(self, request, response):
                    # use default rules, but also consider HTTP 200 responses
                            # a ban if there is 'captcha' word in response body.
        ban = super(PropiedadesSpider, self).response_is_ban(request, response)
                                            # ban = ban or 'captcha' in response.body.lower()
        return ban

#---

    list_user_agents =  [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Safari/537.36 ADAPI/2.0 (UUID:9e7df0ed-2a5c-4a19-bec7-2cc54800f99d) RK3188-ADAPI/1.2.84.533 (MODEL:XMP-6250)'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36	'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',


            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.79 Mobile/14D27 Safari/602.1',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
            'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        ]    
    dict_location={'138360':'DF','138361':'Estado+de+Aguascalientes','4301':'Norte,+Baja+California',
                    '138363':'Baja+California+Sur','138364':'Estado+de+Campeche','138365':'Coahuila',
                    '138366':'Estado+de+Colima','138367':'Chiapas','138368':'Estado+de+Chihuahua','138369':'Estado+de+Durango',
                    '138370':'Estado+de+Guanajuato','138371':'Guerrero','138372':'Hidalgo','138373':'Jalisco','65712':'Estado+de+México+(El+Tambor),+Estado+de+México',
                    '138375':'Michoacán','138376':'Morelos','138377':'Nayarit','138378':'Nuevo+León',
                    '138379':'Oaxaca','138380':'Estado+de+Puebla','138381':'Estado+de+Querétaro','138382':'Quintana+Roo',
                    '138383':'Estado+de+San+Luis+Potosí','138384':'Estado+de+Sinaloa','138385':'Sonora',
                    '138386':'Tabasco','138387':'Tamaulipas','138388':'Estado+de+Tlaxcala','138389':'Veracruz',
                    '138390':'Yucatán','138391':'Estado+de+Zacatecas'} # dans le format c a d parmetere requette { location : locationString  aussi state mais parfois le state est different alors il faut un test}

    #start_urls = ['http://propiedades.com/']

    def start_requests(self):
        #residencial , industrial , comercial
    
        #list_type_immo=['residencial' , 'industrial-' , 'comercial-']
        #changement des lien et aussi le type residencial est 1 , 'comercial 2 et , 'industrial' 3 dans le  format
        list_Referer=[

                        #-----------type=1 dans le format--------------------------------------------
                        'https://propiedades.com/df/residencial-',
                        'https://propiedades.com/aguascalientes/residencial-',
                        'https://propiedades.com/norte-mexicali/residencial-',
                        'https://propiedades.com/baja-california-sur/residencial-',
                        'https://propiedades.com/campeche/residencial-',
                        'https://propiedades.com/coahuila/residencial-',
                        'https://propiedades.com/colima/residencial-',
                        'https://propiedades.com/chiapas/residencial-',
                        'https://propiedades.com/chihuahua/residencial-',
                        'https://propiedades.com/durango/residencial-',
                        'https://propiedades.com/guanajuato/residencial-',
                        'https://propiedades.com/guerrero/residencial-',
                        'https://propiedades.com/hidalgo/residencial-',
                        'https://propiedades.com/jalisco/residencial-',
                        'https://propiedades.com/estado-de-mexico-el-tambor-naucalpan-de-juarez/residencial-',
                        'https://propiedades.com/michoacan/residencial-',
                        'https://propiedades.com/morelos/residencial-',
                        'https://propiedades.com/nayarit/residencial-',
                        'https://propiedades.com/nuevo-leon/residencial-',
                        'https://propiedades.com/oaxaca/residencial-',
                        'https://propiedades.com/puebla/residencial-',
                        'https://propiedades.com/queretaro/residencial-',
                        'https://propiedades.com/quintana-roo/residencial-',
                        'https://propiedades.com/san-luis-potosi/residencial-',
                        'https://propiedades.com/sinaloa/residencial-',
                        'https://propiedades.com/sonora/residencial-',
                        'https://propiedades.com/tabasco/residencial-',
                        'https://propiedades.com/tamaulipas/residencial-',
                        'https://propiedades.com/tlaxcala/residencial-',
                        'https://propiedades.com/veracruz/residencial-',
                        'https://propiedades.com/yucatan/residencial-',
                        'https://propiedades.com/zacatecas/residencial-',

                         ] #le champ Referer dans le headers


             
        #dict_location={}
        list_purpose=[1,2] #dans le format c a dire parametre requette 1 venta  , 2 renta
        my_formdata={'address':'null','busqueda-distancia':'0','busqueda-mas-distancia':'0','change_list':'false',
                    'change_location':'false','colony':'','distance':'0',
                    'filter':'&precio-max=&recamaras=&bathrooms=&precio-min-tmp-list=&precio-max-tmp-list=',
                    'hide_special':'0','highlighted':'false','lat':'19.4403374017544','listType':'list',
                    'lng':'-99.1525628202514','location':'','locationString':'',
                    'page':'1','point_ne':'','point_sw':'','purpose':'','realestates':'false','return':'galeria',
                    'section':'VL','state':'','subtype':'0','switchList':'false','type':'',
                    'url_search':'','YII_CSRF_TOKEN':'null','zoom':'0' }

        compteur_Referer_list=0
        
       # for type_immo in list_type_immo:
        for location in dict_location.keys():# parcourire les region avec les code et affecter vers le parametre aussi affectation de refere dans  headers
          
            my_formdata['location']=str(location)
            my_formdata['locationString']=str(dict_location[location])
            if str(my_formdata['location'])=="138365":
                my_formdata['state']="Coahuila+de+Zaragoza"
            elif str(my_formdata['location'])=='65712':
                my_formdata['state']='Estado+de+México'
            elif str(my_formdata['location'])=='138375':
                my_formdata['state']='Michoacán+de+Ocampo'
            elif str(my_formdata['location'])=='138389':
                my_formdata['state']='Veracruz+de+Ignacio+de+la+Llave'
                
            else:
                my_formdata['state']=str(dict_location[location])

            
            
            for purpose in list_purpose: #parcourire list prupose le venta et renta
                my_formdata['purpose']=str(purpose) #affecter le venta renta dans le format c a dire parameter requete
                
                
                for num_page in range(1): #parcourire les pages 1 page seulement juste pour attraper le nombre de page dans le lien 

                    my_formdata['page']=str(num_page)#affecter le numero page  dans le format c a dire parameter requete

                    headers1={'POST':'/properties/filtrar HTTP/1.1','Host': 'propiedades.com','User-Agent': '','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'fr','Accept-Encoding': 'gzip, deflate, br','Referer': '','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest',}
                  #  'Cookie': '__cfduid=decf9b410d4df2221abae51e45a637f181509370728; mktz_client=%7B%22is_returning%22%3A1%2C%22uid%22%3A%22930262737245657822%22%2C%22session%22%3A%22ses1249351486ion%22%2C%22views%22%3A9%2C%22referer_url%22%3A%22%22%2C%22referer_domain%22%3A%22%22%2C%22referer_type%22%3A%22direct%22%2C%22visits%22%3A8%2C%22landing%22%3A%22https%3A//propiedades.com/df/residencial-venta%3Fpagina%3D5%22%2C%22enter_at%22%3A%222017-11-30%7C10%3A19%3A41%22%2C%22first_visit%22%3A%222017-10-30%7C14%3A38%3A50%22%2C%22last_visit%22%3A%222017-11-29%7C8%3A50%3A52%22%2C%22last_variation%22%3A%22%22%2C%22utm_source%22%3Afalse%2C%22utm_term%22%3Afalse%2C%22utm_campaign%22%3Afalse%2C%22utm_content%22%3Afalse%2C%22utm_medium%22%3Afalse%7D; __utma=157410171.404890271.1509370732.1526053570.1526377157.149; __utmz=157410171.1509521801.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __ssid=b9b432bd-fb02-4e84-a9a2-a243ca5d0283;  scarab.visitor=%2259BBAD39F98C4EB9%22; scarab.profile=%224818533%7C1522848674%22; mktz_ab=%7B%2235515%22%3A76533%7D; D_IID=8B7F5018-2975-3E0E-AEF0-9084AC95B38B; D_UID=880296BF-95FB-31B7-A6E4-2EE01487EE2B; D_ZID=9D3298FE-8305-38E9-9757-1CEEA492A9D9; D_ZUID=3E9F1A34-28B4-3FBE-A098-FD1FF27C3CA4; D_HID=57E14B87-F41A-3922-9B47-E3BF4968D032; PHPSESSID=st62rpheo1p6j6faa3k57rkvh5; __utmb=157410171.28.9.1526378507372; __utmc=157410171; YII_CSRF_TOKEN=3ba4dd1d96f29eabfdcf77307d8ad3479ddeb975s%3A40%3A%2242b34eb8c6319874eb576610abc097e23e6270fa%22%3B; user_fingerprint=de202241d9eb36cae06c16d839905b252fbed4bfs%3A128%3A%22b69b1e17ba03fe3b361671c20c9135f3a701844f44a345073432c209186a2e3cb43eb53448c082d59e156c4299b4a5192c50f2494099fcef29fbfb2033fb47f2%22%3B; scarab.mayAdd=%5B%7B%22i%22%3A%224756893%22%7D%5D; __utmt=1'}
            
                    headers1['User-Agent']=random.choice(list_user_agents)
                   # print(headers1['User-Agent'],"-------------------------------------------")
                    if  str(purpose)=='1':
                        headers1['Referer']=str(list_Referer[compteur_Referer_list])+'venta' #prendre le element refere de la liste refer
                    else:
                        headers1['Referer']=str(list_Referer[compteur_Referer_list])+'renta'

                #----------------- test sur le type de lien 
                    if "residencial" in str(list_Referer[compteur_Referer_list]):
                        my_formdata['type']="1"
                    elif "comercial" in str(list_Referer[compteur_Referer_list]):
                        my_formdata['type']="2"
                    elif  "industrial" in str(list_Referer[compteur_Referer_list]):
                        my_formdata['type']="3"
                    else:
                        print("erreur type refer")

                    
                    #---------------------------mon requet scrapy avec format 
                    my_request=scrapy.FormRequest(url= 'https://propiedades.com/properties/filtrar',formdata=my_formdata,headers=headers1,encoding = "utf-8",callback=self.parse)
                    my_request.meta['location']=location
                    my_request.meta['purpose']=purpose
                    my_request.meta['url']=headers1['Referer']
                   
                    yield my_request

                    #--------------------------
            compteur_Referer_list+=1 # agumenter le ce compteur il est paralele a le Iéme numero de location

    def correct(self,champ):

        return str(champ).replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace(';', ' ').replace('\"', ' ').replace('None',"")

    def parse(self, response):
        location=response.meta['location'] #numero de region apartire de la liste de startrequest
        purpose=response.meta['purpose'] # venta ou renta  apartire de la liste de startrequest
        url=response.meta['url'] # lien complet a partire de refere
        print("url",url)
        print(response.body)
        body_json=response.body.decode('utf8')

        datas_first = json.loads(body_json)

        #-------------------nombre de page par lien global
        nombre_page="0"
        if "\'paginate\': {\'pages\':" in str(datas_first):
            nombre_page=str(datas_first).split("\'paginate\': {\'pages\':")[1].split("}")[0].strip()
            print("id region {} ,purpose {}, nombre page {}".format(location,purpose,nombre_page))

        #---------------------------------------------------------

    
        

        #list_type_immo=['residencial' , 'industrial' , 'comercial']

        
        #dict_location={}
        
        my_formdata={'address':'null','busqueda-distancia':'0','busqueda-mas-distancia':'0','change_list':'false',
                    'change_location':'false','colony':'','distance':'0',
                    'filter':'precio-min&precio-max=0&recamaras=0&bathrooms=0&precio-min-tmp-list=&precio-max-tmp-list=',
                    'hide_special':'0','highlighted':'false','lat':'19.40697619493845','listType':'list',
                    'lng':'-99.17211257406615','location':'','locationString':'',
                    'page':'1','point_ne':'','point_sw':'','purpose':'','realestates':'false','return':'galeria',
                    'section':'VL','state':'','subtype':'0','switchList':'false','type':'2',
                    'url_search':'','YII_CSRF_TOKEN':'null','zoom':'0' }

        
          
        my_formdata['location']=str(location)
        my_formdata['locationString']=str(dict_location[location])
        if str(my_formdata['location'])=="138365":
            my_formdata['state']="Coahuila+de+Zaragoza"
        elif str(my_formdata['location'])=='65712':
            my_formdata['state']='Estado+de+México'
        elif str(my_formdata['location'])=='138375':
            my_formdata['state']='Michoacán+de+Ocampo'
        elif str(my_formdata['location'])=='138389':
            my_formdata['state']='Veracruz+de+Ignacio+de+la+Llave'
            
        else:
            my_formdata['state']=str(dict_location[location])

        
        #----------------- test sur le type de lien 
            if "residencial" in str(url):
                my_formdata['type']="1"
            elif "comercial" in str(url):
                my_formdata['type']="2"
            elif  "industrial" in str(url):
                my_formdata['type']="3"
            else:
                print("erreur type refer")
        
        my_formdata['purpose']=str(purpose) #affecter le venta renta dans le format c a dire parameter requete valeur passer a partir de start request
        
        
        if int(nombre_page) >0 :
            for num_page in range(int(nombre_page)): #parcourire les pages 

                my_formdata['page']=str(num_page)#affecter le numero page  dans le format c a dire parameter requete

                headers1={'POST':'/properties/filtrar HTTP/1.1','Host': 'propiedades.com','User-Agent': '','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'fr','Accept-Encoding': 'gzip, deflate, br','Referer': '','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest',}
#'Cookie': '__cfduid=decf9b410d4df2221abae51e45a637f181509370728; mktz_client=%7B%22is_returning%22%3A1%2C%22uid%22%3A%22930262737245657822%22%2C%22session%22%3A%22ses1249351486ion%22%2C%22views%22%3A9%2C%22referer_url%22%3A%22%22%2C%22referer_domain%22%3A%22%22%2C%22referer_type%22%3A%22direct%22%2C%22visits%22%3A8%2C%22landing%22%3A%22https%3A//propiedades.com/df/residencial-venta%3Fpagina%3D5%22%2C%22enter_at%22%3A%222017-11-30%7C10%3A19%3A41%22%2C%22first_visit%22%3A%222017-10-30%7C14%3A38%3A50%22%2C%22last_visit%22%3A%222017-11-29%7C8%3A50%3A52%22%2C%22last_variation%22%3A%22%22%2C%22utm_source%22%3Afalse%2C%22utm_term%22%3Afalse%2C%22utm_campaign%22%3Afalse%2C%22utm_content%22%3Afalse%2C%22utm_medium%22%3Afalse%7D; __utma=157410171.404890271.1509370732.1526053570.1526377157.149; __utmz=157410171.1509521801.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __ssid=b9b432bd-fb02-4e84-a9a2-a243ca5d0283; scarab.visitor=%2259BBAD39F98C4EB9%22; scarab.profile=%224818533%7C1522848674%22; mktz_ab=%7B%2235515%22%3A76533%7D; D_IID=8B7F5018-2975-3E0E-AEF0-9084AC95B38B; D_UID=880296BF-95FB-31B7-A6E4-2EE01487EE2B; D_ZID=9D3298FE-8305-38E9-9757-1CEEA492A9D9; D_ZUID=3E9F1A34-28B4-3FBE-A098-FD1FF27C3CA4; D_HID=57E14B87-F41A-3922-9B47-E3BF4968D032; PHPSESSID=st62rpheo1p6j6faa3k57rkvh5; __utmb=157410171.28.9.1526378507372; __utmc=157410171; YII_CSRF_TOKEN=3ba4dd1d96f29eabfdcf77307d8ad3479ddeb975s%3A40%3A%2242b34eb8c6319874eb576610abc097e23e6270fa%22%3B; user_fingerprint=de202241d9eb36cae06c16d839905b252fbed4bfs%3A128%3A%22b69b1e17ba03fe3b361671c20c9135f3a701844f44a345073432c209186a2e3cb43eb53448c082d59e156c4299b4a5192c50f2494099fcef29fbfb2033fb47f2%22%3B; scarab.mayAdd=%5B%7B%22i%22%3A%224756893%22%7D%5D; __utmt=1'}
        
                headers1['User-Agent']=random.choice(list_user_agents)
                #print(headers1['User-Agent'],"-------------------------------------------")
                
                headers1['Referer']= url #prendre le element refere apartir de start request
                
                #---------------------------mon requet scrapy avec format 
                my_request=scrapy.FormRequest(url= 'https://propiedades.com/properties/filtrar',formdata=my_formdata,headers=headers1,encoding = "utf-8",callback=self.parse_details)
                my_request.meta['nombre_page']=nombre_page
                
                yield my_request

            #--------------------------

    def parse_details(self, response):
        item=NewpropiedadesItem()
        global nb_erreur,nbr_page_crawler
        nombre_page=response.meta['nombre_page']


        #------------------------------------------------correction et extraction de DATA JSON original
        
        body_json=response.body.decode('utf8')
        try:
            datas_first = json.loads(body_json)
        except:
            t="+++++++++++++++++++++++++++++++++++++++"+str(body_json)+"++++++++++++++++++++++++++++++++++++"

            self.log(t)
            print("++++++++++++++++++++"+body_json+"+++++++++++++++++++++++++++++")

        #-----------------
        
        datas_first=str(datas_first).split('markers')[1].split("clusters")[0]

        if datas_first:
            datas_first="{\'markers"+datas_first #ajouter le mot {'markers
        
        datas_second=""
        for caractere in datas_first: #parcourire json caractere par caractere pour faire le correction de json 
            if caractere=="\'":
                datas_second+="\""
                
            elif caractere=="\"":
                datas_second+="\'"

            else:
                datas_second+=caractere

        datas_second=datas_second.replace("False","\"False\"").replace("True","\"True\"").replace("None","\"None\"")
        
        datas_final=""
        if "pagination_html" in datas_second: #tester sur le mot pagination_html dans le json
            datas_second=datas_second.split("pagination_html")[0]#eliminer la partie de pagination_html


        validate_data_second=datas_second[-3]+datas_second[-2]+datas_second[-1] #le fin de json 
       
        
        
        if validate_data_second==", \"" :
            datas_final=datas_second[:-3]+"}" #correction la fin de json
            datas_final=datas_final.replace('\\xa0', ' ')
        else:
            datas_final=datas_second.replace('\\xa0', ' ')

        
        ##--------------------------------------Transformation DATA vers JSON---------------------------


        try:
            
            datas_json=json.loads(datas_final) #transformer le text vers json si il est str
            print("1er creation json +++++++++++++++++++++++ ")

        except json.decoder.JSONDecodeError:
            
            print("2eme correction json et creation +++++++++++++++++++++")

            datas_final=re.sub(r'\'.*?\'','0',datas_final) # le plus important c est le ? il faire la liaison entre les plus proche 2 cote lié  
                                                        #il eliminer tous simple cote les donnees entre simple cote '' par 0  pour eviter le plusieur format de json 
            
            datas_final=datas_final.replace("\'"," ") #remplacer les reste des smple cote impaire

            try:
                datas_json=json.loads(datas_final)
                
                
            except json.decoder.JSONDecodeError:
                #try:
                #    datas_json=brotli.decompress(datas_final)

            #except

                nb_erreur+=1
                print("************************-------------------------+++++++++++++++")
                print(datas_final)
        
   
        #----------------------------------------------------------*****************************
        try:
            
            #
            list_key_json=datas_json.keys()#les key de  premiers elements de json 
            #print(list_key_json)
            
            if 'markers' in list_key_json:
                list_markers=datas_json.get('markers').keys() # le liste de markers qui contient des id 
                
                data_markers=datas_json.get('markers') # le donner complet de element markers
                
                for marker in list_markers:
                    
                    
                    try:
                        url_link=data_markers.get(marker).get('property_url')
                    except:
                        url_link=""
                    if url_link !="":
                        try:    
                            nom=str(data_markers.get(marker).get('short_address'))
                        except:
                            nom=""
                        try:
                            json_prix=str(data_markers.get(marker).get('price_format'))
                            if "$" in json_prix:
                                t_prix=json_prix.split("$")
                                prix="".join(t_prix[1:]).strip()
                            else:
                                prix=json_prix

                        except:
                            prix=""
                        try:
                            id_client=str(data_markers.get(marker).get('id'))
                        except:
                            id_client=""
                        try:
                            annonce_date=str(data_markers.get(marker).get('modified'))
                        except:
                            annonce_date=""
                        #------------------------------------------Caregorie
                        try:
                            categorie=str(data_markers.get(marker).get('subtype_str'))
                        except:
                            categorie=""

                        if "Departamento" in categorie:

                            maison_apt=2
                        elif "Casa" in categorie :
                            maison_apt=1
                        elif "Cuartos" in categorie:
                            maison_apt=6

                        else:
                            maison_apt=8
                        #------------------------------------------Type
                        try:
                            typee=str(data_markers.get(marker).get('purpose'))
                        except:
                            typee="" 

                        if "Venta" in typee:
                            achat_loc = "1"
                        elif maison_apt==6:
                            achat_loc="6"
                        else:
                            achat_loc= "2" 
                        #----------------------------------------           
                        try:
                            annonce_text=str(data_markers.get(marker).get('description'))
                        except:
                            pass
                        try:
                           piece =str(data_markers.get(marker).get('bedrooms'))
                        except:
                            piece=""
                        try:
                            m_total=str(data_markers.get(marker).get('size_ground_format'))
                        except:
                            pass
                        #-----------------------------------Adressss   
                        try:
                            zip_code=str(data_markers.get(marker).get('sepomex').get('zipcode'))
                        except:
                            zip_code=""
                        try:
                            province=str(data_markers.get(marker).get('sepomex').get('state'))
                        except:
                            province=""                   
                        try:
                            ville=str(data_markers.get(marker).get('sepomex').get('city'))
                        except:
                            ville=""
                        try:
                            quartier=str(data_markers.get(marker).get('sepomex').get('colony'))
                        except:
                            quartier=""

                        #-----------------------neww ajouter

                        try:
                           longitude =str(data_markers.get(marker).get('longitude'))
                        except:
                            longitude=""
                        try:
                           latitude =str(data_markers.get(marker).get('latitude'))
                        except:
                            latitude=""
                        try:
                           nb_photo =str(data_markers.get(marker).get('total_photos'))
                        except:
                            nb_photo=""
                        try:
                            neuf_ind=response.xpath("//div[@class='subsection-content']//ul[@class='carac-large']//span[contains(.,'Edad del inmueble')]//following-sibling::span/text()").extract_first()
                        except:
                            neuf_ind=""
                        #----------------------------------------Itemmmmss


                        item['FROM_SITE']="propiedades"
                        item['ANNONCE_LINK']=self.correct(url_link)
                        item['NOM']=self.correct(nom)
                        item['PRIX']=self.correct(prix)
                        item['ID_CLIENT']=self.correct(id_client)
                        item['ANNONCE_DATE']=self.correct(annonce_date)
                        item['CATEGORIE']=self.correct(categorie)
                        item['ACHAT_LOC']=self.correct(achat_loc)
                        item['ANNONCE_TEXT']=self.correct(annonce_text)
                        item['PIECE']=self.correct(piece)
                        item['M2_TOTALE']=self.correct(m_total)
                        item['CP']=self.correct(zip_code)
                        item['PROVINCE']=self.correct(province)
                        item['VILLE']=self.correct(ville)
                        item['QUARTIER']=self.correct(quartier)
                        #-------------------------------------items newww
                        item['LATITUDE']=self.correct(latitude)
                        item['LONGITUDE']=self.correct(longitude)
                        item['PHOTO']=self.correct(nb_photo)
                        item['NEUF_IND']=self.correct(neuf_ind)
                        #--------------------------items manquant

                       # item['NB_GARAGE']=self.correct(garage)
                       # item['NB_ETAGE']=self.correct(nb_etage)
                       # item['SURFACE_TERRAIN']=self.correct(surfaceTerrain)


                        yield item
                    else:
                        pass
                nbr_page_crawler+=1
                
        except :
            pass

        print ("nombre de page total par lien : ",nombre_page)
        print("nombre de page ironee (--) : ",nb_erreur)
        print("page crawler Total (++) :: ",nbr_page_crawler)


            
       


    #fiinn
