# 使用软件 Fiddler 4 获取 ts 地址，或者说是 u3u8 地址。
# Tools-Options-HTTPS-Check all to capture https package

import requests, os
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
path = "./video"; os.makedirs(path, exist_ok=True) # 自动创建文件夹
count = 1
while True:
    # url = f'https://dtliving-pre.alicdn.com/live_hp/572dfa6d-3383-448a-928b-969e9089bda2/{count}.ts' # Xu.Longya
    # url = f'https://aliliving-pre.alicdn.com/live_hp/a48e207c-c4df-46b6-8564-1620bbb23411/{count}.ts' # Towards zero emission and autonomous shipping
    # url = f'https://aliliving-pre.alicdn.com/live_hp/6c31bf65-da3f-455b-bfc0-c4865afe3fee/{count}.ts' # 1103-Hiroyuki.Ohsaki@东京大学
    # url = f'https://aliliving-pre.alicdn.com/live_hp/6747077f-8649-4076-816a-d84d4127edc4/{count}.ts' # 1023-Ayman
    # url = f'https://aliliving-pre.alicdn.com/live_hp/0975fcf8-70d5-4ca3-ab1c-091046cd302a/{count}.ts' # 1009-Chiba
    # url = f'https://aliliving-pre.alicdn.com/live_hp/91b4d49e-856b-4894-b9c7-7cbcd227a0f2/{count}.ts' # 0922-Akagi
    # url = f'https://dtliving-pre.alicdn.com/live_hp/08b0d31c-69d5-4024-b461-18ae5d87be58/{count}.ts' # 0424-Zhu.ZQ
    # url = f'https://aliliving-pre.alicdn.com/live_hp/ae153cca-44a0-423d-bfed-ac90fbc8147a/{count}.ts' # 0515-Kirtley
    # url = f'https://dtliving.alicdn.com/live_hp/af40dbf9-ebb0-4bb3-adcd-1f792d4e942d/{count}.ts' # 0522-汤广福-能源互联网技术（失败）
    # url = f'https://aliliving-pre.alicdn.com/live_hp/5e0d2e96-db88-408c-b31c-6206defc0a8f/{count}.ts' # WEVC
    # url = f'https://aliliving-pre.alicdn.com/live_hp/e80ae67d-32c2-4cbd-bbda-8a21911104bf/{count}.ts' # 0612-Elmonova
    # url = f'https://aliliving-pre.alicdn.com/live_hp/7c42e73b-ec42-4d5c-8466-083446576f38/{count}.ts' # 0626-Halia.Mechatronics
    # url = f'https://dtliving-pre.alicdn.com/live_hp/4b5a190a-e6ab-46d6-9af5-3e297b087ced/{count}.ts' # 0715-Design.of.electric.drive.system
    # url = f'https://dtliving-pre.alicdn.com/live_hp/28cb2dd8-273d-437c-b783-ffbd2859797f/{count}.ts' # 0727-Jahns-WEMPEC.UW-Madison-CSI(Fail)
    # url = f'https://aliliving-pre.alicdn.com/live_hp/8bbdcc27-59f6-4602-b3c0-1f3701186ee3/{count}.ts' # 0727-Jahns-WEMPEC.UW-Madison-CSI
    # url = f'https://aliliving-pre.alicdn.com/live_hp/b7aa3178-ca3f-47d9-bf4a-b4ece8091f23/{count}.ts' # 0806-Briz-high.freq.signal
    # url = f'https://aliliving-pre.alicdn.com/live_hp/c6d5a93e-110d-43fd-8f14-f76cd2b7b3a7/{count}.ts' # 0817-Flaabjerg
    # url = f'https://dtliving-pre.alicdn.com/live_hp/cf8e09ff-a4bf-4e31-9ba1-b9f518665bbe/{count}.ts' # 0903-Motors.Consulting
    url = f'https://aliliving-pre.alicdn.com/live_hp/ae0c37f8-6e2f-46db-84e7-ccea2d8a78d0/{count}.ts' # 1208-永守重信-浙江大学百年电气”系列论坛——收官之作！
                                                                                                        # 特邀“日本电产（NIDEC、尼得科）”创始人、会长 永守重信 先生！
                                                                                                        # 今天下午2：00正式开始！
                                                                                                        # 畅谈创业初心与经历，展望电机行业发展大局。
                                                                                                        # 日语演讲，全程中文同声翻译。
                                                                                                        # 欢迎参会~

    res = requests.get(url, headers=headers)

    if res.status_code != 200: # status code is not 200
        print(f'status code is {res.status_code}. Stop.')
        break
    if len(res.content) < 400: # size less than 5 KB
        print(f'Size: {len(res.content)} KB. Stop.')
        break
    print(count)
        
    with open(path + "/%04d.ts" % count, "wb")as f:
        f.write(res.content)

    count += 1
