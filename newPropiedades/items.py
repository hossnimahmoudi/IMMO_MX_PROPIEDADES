# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewpropiedadesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    SITE = scrapy.Field()
    ANNONCE_LINK = scrapy.Field()
    FROM_SITE = scrapy.Field()
    ID_CLIENT = scrapy.Field()
    ACHAT_LOC = scrapy.Field()
    MAISON_APT = scrapy.Field()
    NOM = scrapy.Field()
    ADRESSE = scrapy.Field()
    CP = scrapy.Field()
    VILLE = scrapy.Field()
    QUARTIER = scrapy.Field()
    PROVINCE = scrapy.Field()
    ANNONCE_TEXT = scrapy.Field()
    SURFACE_TERRAIN = scrapy.Field()
    M2_TOTALE = scrapy.Field()
    NEUF_IND = scrapy.Field()
    NB_GARAGE = scrapy.Field()
    PIECE = scrapy.Field()
    PRIX = scrapy.Field()
    PRIX_M2 = scrapy.Field()

    ANNONCE_DATE=scrapy.Field()
    CATEGORIE=scrapy.Field()

    
    NB_ETAGE=scrapy.Field()

    #----------------  ajouter new

    LATITUDE =scrapy.Field()
    LONGITUDE=scrapy.Field()
    PHOTO=scrapy.Field()
