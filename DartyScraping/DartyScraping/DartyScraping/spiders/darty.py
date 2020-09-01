import scrapy

from ..items import DartyscrapingItem
class DartySpider(scrapy.Spider):
    name = 'darty'
    # allowed_domains = ['darty.com']
    # start_urls = ['https://www.darty.com/nav/achat/gros_electromenager/lave-linge/index.html']

    def start_requests(self):
        curlRequest="curl 'https://www.darty.com/nav/achat/gros_electromenager/lave-linge/index.html' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Cookie: datadome=UGTziULWOYyZZ~NhhGUXhdVkm~IcSdZS6MrzzQbfEcMfBWRaiH1VjOiFA-Jrmt1iTkCWWUaHPlWfcgXq03hsRft~_AOi~aMwS.Nvd.5rMO; segm=09; rxVisitor=1598437771166SH3NO0BDNHDFVHRE85P8TQ4U7K8PQ8FG; tc_cj_v2=%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKOSRSJROMRPLKZZZ%5D; tCdebugLib=1; OptanonConsent=isIABGlobal=false&datestamp=Tue+Sep+01+2020+02%3A45%3A41+GMT%2B0530+(India+Standard+Time)&version=6.1.0&consentId=8d5d8e41-d32d-443d-8607-42cb628b7c5e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=&legInt=&geolocation=%3B&AwaitingReconsent=false; AMCV_0C4B401053DABFF10A490D4C%40AdobeOrg=870038026%7CMCIDTS%7C18506%7CMCMID%7C86488860138132122380590595927246602194%7CMCAID%7CNONE%7CMCOPTOUT-1598915743s%7CNONE%7CMCAAMLH-1599513343%7C12%7CMCAAMB-1599513343%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18508%7CvVersion%7C5.0.0%7CMCSYNCS%7C1083-18510*1085-18510*1086-18510*1087-18510*1088-18510*19913-18510; dartLev=Direct%3Awww%2Fcatalogue%2Fgros_electromenager%2Flave_linge%7C1598437774529; s_dartCode=Direct%3Awww%2Fcatalogue%2Fgros_electromenager%2Flave_linge%7C1598437774529; s_dartCanStc=Direct; cikneeto_uuid=id:64966e43-0fb5-450a-bd73-0616fae321ac; etuix=gie8.YIr53cw.w3AUn1CfTXtOl8R9IMl.zSuvlMpGrW3DL.mIWJftA--; eb-profile=e7ffc666-c656-4ee3-be3a-b609d0dfad8a:1100389102:1598908545943; s_ecid=MCMID%7C86488860138132122380590595927246602194; OptanonAlertBoxClosed=2020-08-26T10:29:49.207Z; _gcl_au=1.1.427472796.1598437790; sto__vuid=234858bec22d45147786bfa8e21a47c2; _fbp=fb.1.1598437802550.725473167; cto_bundle=5_FtzF9KRVdDU2xlNURrcjNHeExaakJpbEhXUmxUNG1aSVZ1d3BjWFIzbmU3bUdrekQwQUxISW5iNWZKalJ1MHAlMkJyWVhMVEtKdGFlQzRzOFdOdTlFME1WN3oxbE5scmkyQnVxZlQ1V1R3TGptVGVjVEw4YnBjWjJobyUyQmV4bDY4aGNHZ3NCNktmV0F0dkk0NEM2N3hwbHREdW9Pa0pTSUw5Z2E5Y3V5WWdrbUV5S0FpbUFoTktzcGMwWGxxZDFrWE5wbTAlMkI; kameleoonVisitorCode=_js_olkd53mtkd3usp1o; _hjid=47eadad4-aa99-4c49-a468-c8d3562e54df; eb-lastactivity-hash=357777313; eb-profile-cluster=0; eb-profile-clusters={%22587747fbec8040bea82640dc%22:{%221598618730397%22:0%2C%221598529252393%22:0}}; ak_bmsc=EE9F4A8634179BF08CBB70E59AB8B8DA312C8D3ED461000077684D5FB98A6D06~plBB3buZirpszYbONn81kTEYpEqGIWOY0K4UU7uv0tZMxmOJUGVRK8y0/kOdHoKo6OVel7QUU5+tFiU5Gb1l5zrncbACu2lc61QeVWixrXBuv2w6D44hs+DVQab6xFu90Ab19qDHy2CxGiylR1eKM3tI2w7Mgd3hYme7InUu4nCKsBGJAgXkek62sb8lbErTft0bCesAPBnEBQXV0liXIx6uHio4HPXuIBL8Ji0KbX21Y=; akavpau_VP_WaitingRoom=1598908852~id=eb2655180697fdca0c4639aea62b627e; dtPC=3$508536618_903h-vKWUFFLWMMEOPRJJOQUNGUGJAVROTHPIO-0e7; rxvt=1598910378368|1598908536628; dtSa=-; dtLatC=1059; JSESSIONID=0000fPaERlAsnArhl46JBiEYV1z:19858lpmu; session=fjwthztsc4chl0d1z4fyqt; bm_sv=74A2F3F292F24467A15877F35EEA7984~QnL+pjEchoD5CzH3QLocNv27wFH7syvHDzNMir1Q0uDkp+4k0Vqa3HhXpzHq/3sbmNhIcAayRW6rDaMp6sxhp4oofeAobYCeIS5lpY+5Zg4whJ/FdgDonz9owJBCC06H6oanAb1yOETONt4mt7xJfAtt5QrSUPAaACRRytyxX7s=; tc_payment=1; dartProfPa=1; gpv_p3=www%2Fcatalogue%2Fgros_electromenager%2Flave_linge; dartDateLastCall=1598908543247; AMCVS_0C4B401053DABFF10A490D4C%40AdobeOrg=1; s_cc=true; sto__session=1598908544024; sto__count=0; cikneeto=date:1598908544350; _hjIncludedInSessionSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=1; dtCookie=v_4_srv_3_sn_A9B1EAF43E37243B1906AD6730AC2DD7_app-3Ae8e01c74db6645d0_0_ol_0_perc_100000_mul_1' -H 'Upgrade-Insecure-Requests: 1'"
        yield scrapy.Request.from_curl(curlRequest,callback=self.start_scraping)

    def start_scraping(self, response):
        washingMachines=response.css('.next_prev_info')
        print(washingMachines)
        items=DartyscrapingItem()
        for item in washingMachines:
            productName=item.css('.prd-name').css('::text').extract()
            print(productName)
            productPrice=item.css('.darty_normal').css('::text').extract()

            items['productName']=productName
            items['productPrice']=productPrice

            yield items


