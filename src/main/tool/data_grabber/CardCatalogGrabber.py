from src.main.tool.data_grabber.CardListGrabber import CardFromListGrabber
from src.main.tool.CardInfo import CardInfo
from src.main.tool.DriverFactory import DriverFactory
from src.main.tool.data_grabber.GetBaseData import BaseData, get_base_data
from src.main.tool.CsvEditor import CsvEditor

import random


class CardCatalogGrabber:
    def __init__(self, csv_editor: CsvEditor, driver_factory: DriverFactory):
        self.csv = csv_editor
        self.driver_f = driver_factory

    def grab_url(self, url: str):
        cur_list = 1
        filters="f[mx]=2ff-2fi-dbbc-d8xw"

        # base_data: BaseData = self.driver_f.parse(url + "?" + filters, get_base_data)
        # print(f'Total cards: {base_data.total_cards} on {base_data.total_pages} pages')


        list_g = CardFromListGrabber(self.csv, self.driver_f)
        while cur_list <= 1:
            print(f'- Page {cur_list}')
            cur_url = f'{url}?{filters}&p={cur_list}'
            list_g.grab_url(cur_url)
            cur_list = cur_list + 1