from src.main.tool.data_grabber.GetLinksFromCardList import get_links_price_from_card_list
from src.main.tool.data_grabber.CardInfoGrabber import CardInfoGrabber
from src.main.tool.CardInfo import CardInfo
from src.main.tool.CsvEditor import CsvEditor
from src.main.tool.DriverFactory import DriverFactory


class CardFromListGrabber:
    def __init__(self, csv_editor: CsvEditor, driver_factory: DriverFactory):
        self.csvEditor = csv_editor
        self.driver_factory = driver_factory

    def grab_url(self, url: str):
        print(f'-- get links from url {url}')
        links: [(str, str, (int, str))] = self.driver_factory.parse(url, get_links_price_from_card_list)
        print(f'-- found {len(links)} links')

        card_info_arr: [] = []
        for link in links:
            card_info = CardInfo(link[1])
            card_info.name = link[0]
            card_info.price = link[2][0]
            card_info.release = "2020"
            card_info.max_watt = "0"
            card_info.offer_charge_block = "0"
            card_info_arr.append(card_info)


        
        # card_info_grabber = CardInfoGrabber(self.driver_factory)
        # for link in links:
        #     print(f'-- link: {link}')
        #     search_res = self.csvEditor.find_url_in_file(url)
        #     if not search_res[0]:
        #         card_info = card_info_grabber.get_from_url(link)
        #         card_info_arr.append(card_info)
        #     elif link[1][0] != search_res[1][0] or (link[1][1] != search_res[1][1]):
        #         pass
        import pprint
        
        for card in card_info_arr:
            print("====Card array object")
            pprint.pprint(vars(card))
        if len(card_info_arr) > 0:
            self.csvEditor.add_cards_to_csv(card_info_arr)
        return card_info_arr

