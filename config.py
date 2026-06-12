import os
import datetime

ymd = datetime.datetime.today().strftime('%Y%m%d')
md = datetime.datetime.today().strftime('%m%d')

db_name = "fujianmaoyi"

collection_name = f"fujianmaoyi_index_{ymd}"

collection_find_name = f"fujianmaoyi_index_find_{ymd}"

indexurl = "https://www.hottopic.com/home/?start={}&sz=80&prPos=-180"

indexFindUrl = "https://www.hottopic.com/product/{}/{}.html"

mother = 80

cookies = {
    'cqcid': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    'cquid': '||',
    'dwanonymous_23591031129026c185e7ee2aa18943e0': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    'preferredStoreDetails_hottopic': '"{\\"store_id\\":\\"8601\\",\\"postal_code\\":\\"3905\\",\\"latitude\\":64.1743,\\"longitude\\":51.7373}"',
    'preferredStoreId_hottopic': '8601',
    '__cq_dnt': '0',
    'dw_dnt': '0',
    'pickupStores_hottopic': '[]',
    'BVBRANDID': 'fa70a692-057d-44ca-850c-31135e9f9da9',
    '__cq_uuid': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    'AMCVS_33A90F985C014F620A495CF5%40AdobeOrg': '1',
    's_ecid': 'MCMID%7C07768362011298389703523816262609279369',
    's_cc': 'true',
    'AMCV_33A90F985C014F620A495CF5%40AdobeOrg': '281789898%7CMCIDTS%7C20615%7CMCMID%7C07768362011298389703523816262609279369%7CMCAAMLH-1781676976%7C11%7CMCAAMB-1781676976%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1781079377s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.1.0',
    '_taggstar_vid': 'e3e52cee-6493-11f1-b675-e704cfc75c02',
    '_taggstar_exps': '{"sp":{"id":"","group":""}}',
    '_scid': 'L-V_RanI02zGyq1HAZ495xH6O8tmIsN5',
    '_pin_unauth': 'dWlkPU1qWTNNRGsyWm1RdE1ESm1ZUzAwTnpka0xUbG1Oemd0WVdNeFpqTXpNR1kwTkRrMA',
    '_tt_enable_cookie': '1',
    '_ttp': '01KTR2SCGBHM3A2F6XPSD1ENJF_.tt.1',
    'forceCCPA': 'created',
    'kampyle_userid': '31a6-e07a-6a82-1792-f5c0-eb98-fed1-caf4',
    '_sctr': '1%7C1781020800000',
    '_fbp': 'fb.1.1781072518453.64457541160302638',
    '_gcl_au': '1.1.1913258941.1781072520',
    '_ga': 'GA1.1.1335073523.1781072520',
    '__attn_eat_id': '9b06def97efe4cd7b728981565179ece',
    '__attentive_id': '2e7cca271ae54ed1942ae9f5104ab7e1',
    '__attentive_cco': '1781072520799',
    '__attentive_dv': '1',
    '_cfuvid': '9gu21MEBjDgU7rugStKa3ud9urcRUlnLX1NKFd3UxzY-1781072635.6242454-1.0.1.1-ao47UHMvABpdAC9zYIyX.2iV_c5C9lrY_DLL74aYsz4',
    '_attn_bopd_': 'none',
    '__cq_seg': '0~0.05!1~-0.39!2~0.17!3~-0.41!4~-0.27!5~-0.02!6~0.05!7~-0.21!8~-0.12!9~-0.72',
    's_sq': '%5B%5BB%5D%5D',
    '__cq_bc': '%7B%22aavt-hottopic%22%3A%5B%7B%22id%22%3A%2233563204%22%7D%2C%7B%22id%22%3A%2211459228%22%7D%5D%7D',
    '_scid_r': 'KGV_RanI02zGyq1HAZ495xH6O8tmIsN5zIZKNQ',
    's_dslv': '1781076143555',
    '_br_uid_2': 'uid%3D2799474921650%3Av%3D12.0%3Ats%3D1781072176534%3Ahc%3D17',
    'cto_bundle': 'KNvRN19mRTFrT0I3eXFEMklFV2d4SnNoT2JvcVI1TnlvOTBhM3dqVVBjcDclMkZzd0pMRk11WUpqdmJlcTZEMTY0WUozbEpxZEZqUFl5TGl4ZXIyMUxPZzliclNmMmQxR3JlQUNQV29FT0puTW13Rm1hTk9ScnN5RTlMS2VxZk1Vb2J3MkdUdDZRSmoxZ2dLQjBJbGcxTDg0RERaQSUzRCUzRA',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzgxMDcyNTIwNzk3LFwidW9cIjoxNzgxMDcyNTIwNzk3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjJlN2NjYTI3MWFlNTRlZDE5NDJhZTlmNTEwNGFiN2UxXCJ9IiwiZWF0Ijoie1wiY29cIjoxNzgxMDc2MTQ3NDYyLFwidW9cIjoxNzgxMDc2MTQ3NDYzLFwibWFcIjozNjUwLFwiaW5cIjp0cnVlLFwidmFsXCI6XCJodHRwczovL3NlZ2hnLmhvdHRvcGljLmNvbVwifSJ9',
    'utag_main': 'v_id:019eb02c9d23001d0d34a9ab325d0506f005406700bd0$_sn:2$_se:3$_ss:0$_st:1781077949472$vapi_domain:hottopic.com$ses_id:1781076141842%3Bexp-session$_pn:1%3Bexp-session',
    's_nr30': '1781076149477-Repeat',
    's_plt': '23.12',
    's_pltp': 'home',
    'kampyleUserSession': '1781076150338',
    'kampyleUserSessionsCount': '6',
    'kampyleUserPercentile': '56.847191815659535',
    'kampyleSessionPageCounter': '1',
    'ttcsid_C10JAK95A0R73RNSBSAG': '1781076151893::HXZlZCnPU-pElDp6nJPO.2.1781076162065.1',
    'ttcsid': '1781076151894::JAhTJBLG6cfU_Q9svpcm.2.1781076162063.0::1.-26066.135::0.0.0.0::262037.4.0',
    'lastVisited_hottopic': '',
    '_ga_5KQG1X9V34': 'GS2.1.s1781087920$o2$g0$t1781087920$j60$l0$h0',
    'dwsid': 'kNGMpo5tiztQjy-CuoipLuaxLxQQCwypeLdlALCkcZEq_NZa6mYa2WGuA0jZYuYor2Gug8As44gEZZHSjJhvLw==',
    'dwac_bcFJoiaaiZzQwaaadn1EVwqxpC': 'gyXefBnfhFcJimzx24cM7vVFfc6HuQPFIbI%3D|dw-only|||USD|false|US%2FPacific|true',
    'sid': 'gyXefBnfhFcJimzx24cM7vVFfc6HuQPFIbI',
    'dwsecuretoken_23591031129026c185e7ee2aa18943e0': 'IKKWc3ExdIN5XN2rBHUM-MOgioJ2xsAamg==',
    'BVBRANDSID': 'd9b4f1a3-ea2b-4da0-931d-797f07d67a15',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jun+10+2026+20%3A06%3A31+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202604.2.0&browserGpcFlag=0&isDntEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=BG90%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'cqcid=acaAxH9Utu1g4KGIKpkDubqfVh; cquid=||; dwanonymous_23591031129026c185e7ee2aa18943e0=acaAxH9Utu1g4KGIKpkDubqfVh; preferredStoreDetails_hottopic="{\\"store_id\\":\\"8601\\",\\"postal_code\\":\\"3905\\",\\"latitude\\":64.1743,\\"longitude\\":51.7373}"; preferredStoreId_hottopic=8601; __cq_dnt=0; dw_dnt=0; pickupStores_hottopic=[]; BVBRANDID=fa70a692-057d-44ca-850c-31135e9f9da9; __cq_uuid=acaAxH9Utu1g4KGIKpkDubqfVh; AMCVS_33A90F985C014F620A495CF5%40AdobeOrg=1; s_ecid=MCMID%7C07768362011298389703523816262609279369; s_cc=true; AMCV_33A90F985C014F620A495CF5%40AdobeOrg=281789898%7CMCIDTS%7C20615%7CMCMID%7C07768362011298389703523816262609279369%7CMCAAMLH-1781676976%7C11%7CMCAAMB-1781676976%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1781079377s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.1.0; _taggstar_vid=e3e52cee-6493-11f1-b675-e704cfc75c02; _taggstar_exps={"sp":{"id":"","group":""}}; _scid=L-V_RanI02zGyq1HAZ495xH6O8tmIsN5; _pin_unauth=dWlkPU1qWTNNRGsyWm1RdE1ESm1ZUzAwTnpka0xUbG1Oemd0WVdNeFpqTXpNR1kwTkRrMA; _tt_enable_cookie=1; _ttp=01KTR2SCGBHM3A2F6XPSD1ENJF_.tt.1; forceCCPA=created; kampyle_userid=31a6-e07a-6a82-1792-f5c0-eb98-fed1-caf4; _sctr=1%7C1781020800000; _fbp=fb.1.1781072518453.64457541160302638; _gcl_au=1.1.1913258941.1781072520; _ga=GA1.1.1335073523.1781072520; __attn_eat_id=9b06def97efe4cd7b728981565179ece; __attentive_id=2e7cca271ae54ed1942ae9f5104ab7e1; __attentive_cco=1781072520799; __attentive_dv=1; _cfuvid=9gu21MEBjDgU7rugStKa3ud9urcRUlnLX1NKFd3UxzY-1781072635.6242454-1.0.1.1-ao47UHMvABpdAC9zYIyX.2iV_c5C9lrY_DLL74aYsz4; _attn_bopd_=none; __cq_seg=0~0.05!1~-0.39!2~0.17!3~-0.41!4~-0.27!5~-0.02!6~0.05!7~-0.21!8~-0.12!9~-0.72; s_sq=%5B%5BB%5D%5D; __cq_bc=%7B%22aavt-hottopic%22%3A%5B%7B%22id%22%3A%2233563204%22%7D%2C%7B%22id%22%3A%2211459228%22%7D%5D%7D; _scid_r=KGV_RanI02zGyq1HAZ495xH6O8tmIsN5zIZKNQ; s_dslv=1781076143555; _br_uid_2=uid%3D2799474921650%3Av%3D12.0%3Ats%3D1781072176534%3Ahc%3D17; cto_bundle=KNvRN19mRTFrT0I3eXFEMklFV2d4SnNoT2JvcVI1TnlvOTBhM3dqVVBjcDclMkZzd0pMRk11WUpqdmJlcTZEMTY0WUozbEpxZEZqUFl5TGl4ZXIyMUxPZzliclNmMmQxR3JlQUNQV29FT0puTW13Rm1hTk9ScnN5RTlMS2VxZk1Vb2J3MkdUdDZRSmoxZ2dLQjBJbGcxTDg0RERaQSUzRCUzRA; _attn_=eyJ1Ijoie1wiY29cIjoxNzgxMDcyNTIwNzk3LFwidW9cIjoxNzgxMDcyNTIwNzk3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjJlN2NjYTI3MWFlNTRlZDE5NDJhZTlmNTEwNGFiN2UxXCJ9IiwiZWF0Ijoie1wiY29cIjoxNzgxMDc2MTQ3NDYyLFwidW9cIjoxNzgxMDc2MTQ3NDYzLFwibWFcIjozNjUwLFwiaW5cIjp0cnVlLFwidmFsXCI6XCJodHRwczovL3NlZ2hnLmhvdHRvcGljLmNvbVwifSJ9; utag_main=v_id:019eb02c9d23001d0d34a9ab325d0506f005406700bd0$_sn:2$_se:3$_ss:0$_st:1781077949472$vapi_domain:hottopic.com$ses_id:1781076141842%3Bexp-session$_pn:1%3Bexp-session; s_nr30=1781076149477-Repeat; s_plt=23.12; s_pltp=home; kampyleUserSession=1781076150338; kampyleUserSessionsCount=6; kampyleUserPercentile=56.847191815659535; kampyleSessionPageCounter=1; ttcsid_C10JAK95A0R73RNSBSAG=1781076151893::HXZlZCnPU-pElDp6nJPO.2.1781076162065.1; ttcsid=1781076151894::JAhTJBLG6cfU_Q9svpcm.2.1781076162063.0::1.-26066.135::0.0.0.0::262037.4.0; lastVisited_hottopic=; _ga_5KQG1X9V34=GS2.1.s1781087920$o2$g0$t1781087920$j60$l0$h0; dwsid=kNGMpo5tiztQjy-CuoipLuaxLxQQCwypeLdlALCkcZEq_NZa6mYa2WGuA0jZYuYor2Gug8As44gEZZHSjJhvLw==; dwac_bcFJoiaaiZzQwaaadn1EVwqxpC=gyXefBnfhFcJimzx24cM7vVFfc6HuQPFIbI%3D|dw-only|||USD|false|US%2FPacific|true; sid=gyXefBnfhFcJimzx24cM7vVFfc6HuQPFIbI; dwsecuretoken_23591031129026c185e7ee2aa18943e0=IKKWc3ExdIN5XN2rBHUM-MOgioJ2xsAamg==; BVBRANDSID=d9b4f1a3-ea2b-4da0-931d-797f07d67a15; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jun+10+2026+20%3A06%3A31+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202604.2.0&browserGpcFlag=0&isDntEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=BG90%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


cookies_find = {
    'dwanonymous_23591031129026c185e7ee2aa18943e0': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    'preferredStoreDetails_hottopic': '"{\\"store_id\\":\\"8601\\",\\"postal_code\\":\\"3905\\",\\"latitude\\":64.1743,\\"longitude\\":51.7373}"',
    'preferredStoreId_hottopic': '8601',
    'pickupStores_hottopic': '[]',
    'BVBRANDID': 'fa70a692-057d-44ca-850c-31135e9f9da9',
    '__cq_uuid': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    's_ecid': 'MCMID%7C07768362011298389703523816262609279369',
    '_taggstar_vid': 'e3e52cee-6493-11f1-b675-e704cfc75c02',
    '_taggstar_exps': '{"sp":{"id":"","group":""}}',
    '_scid': 'L-V_RanI02zGyq1HAZ495xH6O8tmIsN5',
    '_pin_unauth': 'dWlkPU1qWTNNRGsyWm1RdE1ESm1ZUzAwTnpka0xUbG1Oemd0WVdNeFpqTXpNR1kwTkRrMA',
    '_tt_enable_cookie': '1',
    '_ttp': '01KTR2SCGBHM3A2F6XPSD1ENJF_.tt.1',
    'forceCCPA': 'created',
    'kampyle_userid': '31a6-e07a-6a82-1792-f5c0-eb98-fed1-caf4',
    '_sctr': '1%7C1781020800000',
    '_fbp': 'fb.1.1781072518453.64457541160302638',
    '_gcl_au': '1.1.1913258941.1781072520',
    '_ga': 'GA1.1.1335073523.1781072520',
    '__attn_eat_id': '9b06def97efe4cd7b728981565179ece',
    '__attentive_id': '2e7cca271ae54ed1942ae9f5104ab7e1',
    '__attentive_cco': '1781072520799',
    '_attn_bopd_': 'none',
    'cto_bundle': 'KNvRN19mRTFrT0I3eXFEMklFV2d4SnNoT2JvcVI1TnlvOTBhM3dqVVBjcDclMkZzd0pMRk11WUpqdmJlcTZEMTY0WUozbEpxZEZqUFl5TGl4ZXIyMUxPZzliclNmMmQxR3JlQUNQV29FT0puTW13Rm1hTk9ScnN5RTlMS2VxZk1Vb2J3MkdUdDZRSmoxZ2dLQjBJbGcxTDg0RERaQSUzRCUzRA',
    'cqcid': 'acaAxH9Utu1g4KGIKpkDubqfVh',
    'cquid': '||',
    '__cq_dnt': '0',
    'dw_dnt': '0',
    'AMCVS_33A90F985C014F620A495CF5%40AdobeOrg': '1',
    's_cc': 'true',
    '_cfuvid': 'vIcF92XJ7YTnPFE.ndSjQrG4PieIuoVvaCymQTKnia8-1781155735.688158-1.0.1.1-w7JIeTFGh7XwMqspH7rvT9GFzTAOviJgP5IBixINfBs',
    'dwac_bcFJoiaaiZzQwaaadn1EVwqxpC': '8ASAuNc8BuwAl3GTo07Srihvi7nFw8hIOX8%3D|dw-only|||USD|false|US%2FPacific|true',
    'sid': '8ASAuNc8BuwAl3GTo07Srihvi7nFw8hIOX8',
    'dwsid': 'R-Nt8HlroSzOwI1Oi67phJ-IZvFrlG-I9yjKFIKKosZXU_QtJzBOGhisF0lP7_bJy3fiMc_ACsjLmRbj9aNMeA==',
    '__attentive_dv': '1',
    'dwsecuretoken_23591031129026c185e7ee2aa18943e0': 'EPAKP0_PMKpjYAlZF2BT0tdzi5iOwHtN3A==',
    'BVBRANDSID': 'd18aad34-0dcf-4116-a1f2-d03a562dda21',
    'AMCV_33A90F985C014F620A495CF5%40AdobeOrg': '281789898%7CMCIDTS%7C20617%7CMCMID%7C07768362011298389703523816262609279369%7CMCAAMLH-1781831137%7C11%7CMCAAMB-1781831137%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1781233537s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.1.0',
    's_dslv': '1781226337798',
    's_sq': '%5B%5BB%5D%5D',
    '_taggstar_ses': 'd2d24629-65fa-11f1-b62c-93709f9ceb7a',
    '_br_uid_2': 'uid%3D2799474921650%3Av%3D12.0%3Ats%3D1781072176534%3Ahc%3D25',
    '_scid_r': 'MGV_RanI02zGyq1HAZ495xH6O8tmIsN5zIZKPQ',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzgxMDcyNTIwNzk3LFwidW9cIjoxNzgxMDcyNTIwNzk3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjJlN2NjYTI3MWFlNTRlZDE5NDJhZTlmNTEwNGFiN2UxXCJ9IiwiZWF0Ijoie1wiY29cIjoxNzgxMjI2MzQyMzk2LFwidW9cIjoxNzgxMjI2MzQyMzk2LFwibWFcIjozNjUwLFwiaW5cIjp0cnVlLFwidmFsXCI6XCJodHRwczovL3NlZ2hnLmhvdHRvcGljLmNvbVwifSJ9',
    '__attentive_session_id': '5245c3f0607a4e5a8d057d378e50cdcc',
    '__attentive_pv': '1',
    '__attentive_ss_referrer': 'ORGANIC',
    'utag_main': 'v_id:019eb02c9d23001d0d34a9ab325d0506f005406700bd0$_sn:6$_se:6$_ss:0$_st:1781228145729$vapi_domain:hottopic.com$ses_id:1781226337011%3Bexp-session$_pn:2%3Bexp-session',
    's_nr30': '1781226345735-Repeat',
    's_plt': '6.64',
    's_pltp': 'sanrio%20japan%20originals%20hello%20kitty%20mascot%20chopsticks-36409998',
    'kampyleUserSession': '1781226346208',
    'kampyleUserSessionsCount': '11',
    'kampyleUserPercentile': '22.946106847543124',
    'kampyleSessionPageCounter': '1',
    'ttcsid': '1781226343417::jm3sg5Ey1tj9i5vpJED9.6.1781226353598.0::0.-4288.0::0.0.0.0::0.0.0',
    'ttcsid_C10JAK95A0R73RNSBSAG': '1781226343416::5G0EZQINzoxJUmq-DKSA.6.1781226353602.1',
    '_ga_5KQG1X9V34': 'GS2.1.s1781226323$o6$g1$t1781226371$j12$l0$h0',
    'lastVisited_hottopic': '"35650581,36409998,11459228,19508129"',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jun+12+2026+09%3A07%3A50+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202604.2.0&browserGpcFlag=0&isDntEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=BG90%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false',
    '__cq_bc': '%7B%22aavt-hottopic%22%3A%5B%7B%22id%22%3A%2235650581%22%7D%2C%7B%22id%22%3A%2236409998%22%7D%2C%7B%22id%22%3A%2211459228%22%7D%2C%7B%22id%22%3A%2219508129%22%7D%2C%7B%22id%22%3A%2234668121%22%7D%2C%7B%22id%22%3A%2236446023%22%7D%2C%7B%22id%22%3A%2236345778%22%7D%2C%7B%22id%22%3A%2219481982%22%7D%2C%7B%22id%22%3A%2219796763%22%7D%2C%7B%22id%22%3A%2219731789%22%7D%5D%7D',
    '__cq_seg': '0~-0.59!1~-0.08!2~-0.35!3~0.09!4~-0.04!5~-0.02!6~-0.22!7~-0.64!8~0.19!9~0.14!f0~3~2',
}

headers_find = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'dwanonymous_23591031129026c185e7ee2aa18943e0=acaAxH9Utu1g4KGIKpkDubqfVh; preferredStoreDetails_hottopic="{\\"store_id\\":\\"8601\\",\\"postal_code\\":\\"3905\\",\\"latitude\\":64.1743,\\"longitude\\":51.7373}"; preferredStoreId_hottopic=8601; pickupStores_hottopic=[]; BVBRANDID=fa70a692-057d-44ca-850c-31135e9f9da9; __cq_uuid=acaAxH9Utu1g4KGIKpkDubqfVh; s_ecid=MCMID%7C07768362011298389703523816262609279369; _taggstar_vid=e3e52cee-6493-11f1-b675-e704cfc75c02; _taggstar_exps={"sp":{"id":"","group":""}}; _scid=L-V_RanI02zGyq1HAZ495xH6O8tmIsN5; _pin_unauth=dWlkPU1qWTNNRGsyWm1RdE1ESm1ZUzAwTnpka0xUbG1Oemd0WVdNeFpqTXpNR1kwTkRrMA; _tt_enable_cookie=1; _ttp=01KTR2SCGBHM3A2F6XPSD1ENJF_.tt.1; forceCCPA=created; kampyle_userid=31a6-e07a-6a82-1792-f5c0-eb98-fed1-caf4; _sctr=1%7C1781020800000; _fbp=fb.1.1781072518453.64457541160302638; _gcl_au=1.1.1913258941.1781072520; _ga=GA1.1.1335073523.1781072520; __attn_eat_id=9b06def97efe4cd7b728981565179ece; __attentive_id=2e7cca271ae54ed1942ae9f5104ab7e1; __attentive_cco=1781072520799; __attentive_dv=1; _attn_bopd_=none; cto_bundle=KNvRN19mRTFrT0I3eXFEMklFV2d4SnNoT2JvcVI1TnlvOTBhM3dqVVBjcDclMkZzd0pMRk11WUpqdmJlcTZEMTY0WUozbEpxZEZqUFl5TGl4ZXIyMUxPZzliclNmMmQxR3JlQUNQV29FT0puTW13Rm1hTk9ScnN5RTlMS2VxZk1Vb2J3MkdUdDZRSmoxZ2dLQjBJbGcxTDg0RERaQSUzRCUzRA; cqcid=acaAxH9Utu1g4KGIKpkDubqfVh; cquid=||; __cq_dnt=0; dw_dnt=0; _cfuvid=v5r460GTQR2dAcyOI4xv_UBXLpiXAjC_MmQHrYLjcQ4-1781142076.3326614-1.0.1.1-9BzhsMTfnqNXijngj_dW_mgShr1xgcE_iaMFJ.l98SE; _scid_r=KWV_RanI02zGyq1HAZ495xH6O8tmIsN5zIZKNg; _br_uid_2=uid%3D2799474921650%3Av%3D12.0%3Ats%3D1781072176534%3Ahc%3D18; _sc_cspv=https%3A%2F%2Ftr.snapchat.com%2Fconfig%2Fcom%2Fab4a9bd2-d380-4001-a2a8-559bcbbbe981.js%3Fv%3D3.56.3-2606082033; _attn_=eyJ1Ijoie1wiY29cIjoxNzgxMDcyNTIwNzk3LFwidW9cIjoxNzgxMDcyNTIwNzk3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjJlN2NjYTI3MWFlNTRlZDE5NDJhZTlmNTEwNGFiN2UxXCJ9IiwiZWF0Ijoie1wiY29cIjoxNzgxMTQ3MjgzOTA3LFwidW9cIjoxNzgxMTQ3MjgzOTA3LFwibWFcIjozNjUwLFwiaW5cIjp0cnVlLFwidmFsXCI6XCJodHRwczovL3NlZ2hnLmhvdHRvcGljLmNvbVwifSJ9; AMCVS_33A90F985C014F620A495CF5%40AdobeOrg=1; AMCV_33A90F985C014F620A495CF5%40AdobeOrg=281789898%7CMCIDTS%7C20615%7CMCMID%7C07768362011298389703523816262609279369%7CMCAAMLH-1781752084%7C11%7CMCAAMB-1781752084%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1781154484s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.1.0; s_dslv=1781147284021; s_cc=true; ttcsid=1781147286244::7fLqjSKS7UTgZFVcee7P.3.1781147286565.0; ttcsid_C10JAK95A0R73RNSBSAG=1781147286243::lwMXJfoeBqraBAn4qqcb.3.1781147286565.0; utag_main=v_id:019eb02c9d23001d0d34a9ab325d0506f005406700bd0$_sn:3$_se:4$_ss:0$_st:1781149087745$vapi_domain:hottopic.com$ses_id:1781147279416%3Bexp-session$_pn:1%3Bexp-session; s_nr30=1781147287750-Repeat; s_plt=10.22; s_pltp=star%20wars%20the%20mandalorian%20the%20child%20tritan%20cup-19731789; kampyleUserSession=1781147288277; kampyleUserSessionsCount=7; kampyleUserPercentile=58.443250053667505; kampyleSessionPageCounter=1; _ga_5KQG1X9V34=GS2.1.s1781147283$o3$g0$t1781147295$j48$l0$h0; dwsid=X0G0Q65n49HCfoeqYQRxZYk_wFODYPTxisevT3pnnpv3VR6lMEmSsvNsga3taJN8PQMcmcgnbSAk1BsN4xXzIw==; dwac_bcFJoiaaiZzQwaaadn1EVwqxpC=eupJLXXbbIrPtscI7zFfgayUPT1Y3Huqhw8%3D|dw-only|||USD|false|US%2FPacific|true; sid=eupJLXXbbIrPtscI7zFfgayUPT1Y3Huqhw8; dwsecuretoken_23591031129026c185e7ee2aa18943e0=iGSdDSz4ZFVPPAEGO9VF2QO_h9Yabt_MWg==; lastVisited_hottopic="11459228,19796763"; __cq_bc=%7B%22aavt-hottopic%22%3A%5B%7B%22id%22%3A%2211459228%22%7D%2C%7B%22id%22%3A%2219796763%22%7D%2C%7B%22id%22%3A%2219731789%22%7D%2C%7B%22id%22%3A%2219752670%22%7D%2C%7B%22id%22%3A%2235661614%22%7D%2C%7B%22id%22%3A%2236345778%22%7D%2C%7B%22id%22%3A%2233563204%22%7D%5D%7D; __cq_seg=0~-0.45!1~0.33!2~-0.52!3~0.13!4~-0.28!5~-0.15!6~-0.29!7~-0.35!8~0.13!9~-0.26!f0~3~2; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+11+2026+12%3A24%3A11+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202604.2.0&browserGpcFlag=0&isDntEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=BG90%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


findurl = 'https://www.hottopic.com/on/demandware.store/Sites-hottopic-Site/default/Bopis-GetDeliveryOptions?pid={}&pids=[%22{}%22,%22{}%22]&prevPIDS=[%22{}%22,%22{}%22]&storeIds=[8601]&pidObjArray=%7b%22{}%22:%7b%22pid%22:%22{}%22,%22prevPID%22:%22{}%22,%22isStsProduct%22:true,%22isBopisProduct%22:true,%22storeId%22:8601%7d,%22pid%22:%22{}%22%7d&isInventoryCallNeeded=false&isCartPage=false'

savedir = 'D:/web/database/db3/'

ymd = datetime.datetime.today().strftime('%Y%m%d')
md = datetime.datetime.today().strftime('%m%d')

imgname = f'{md}-USman-1-hottopic/{ymd}_'
img = './img/'
if not os.path.exists(img):
    os.makedirs(img)

table = 'fujianmaoyi'
table_down = 'fujianmaoyi_down'


#详情页cookie查找
'''
https://www.hottopic.com/on/demandware.store/Sites-hottopic-Site/default/Bopis-GetDeliveryOptions?pid=11459228&pids=[%2211459228%22,%2211459228%22]&prevPIDS=[%2211459228%22,%2211459228%22]&storeIds=[8601]&pidObjArray=%7b%2211459228%22:%7b%22pid%22:%2211459228%22,%22prevPID%22:%2211459228%22,%22isStsProduct%22:true,%22isBopisProduct%22:true,%22storeId%22:8601%7d,%22pid%22:%2211459228%22%7d&isInventoryCallNeeded=false&isCartPage=false

'''