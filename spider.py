from os.path import basename
import urllib
import re
import requests
import os
import json
import urllib

print('请输入开始id')
id = int(input())
print('请输入结束id')
end_id = int(input())

if not os.path.exists('images'):
    os.mkdir("images")

header = {
    'Cookie':'_zap=92a27b0f-e8e0-4bbd-8d27-761d105c6238; q_c1=a5cbba2d1a4c441fab6c9fcced143ae9|1516591530000|1513758485000; __utmz=155987696.1516688149.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); capsion_ticket="2|1:0|10:1516691211|14:capsion_ticket|44:ZThlNDhmNzc0OWIyNGI2OTkxZjQxZmMyY2M5NDYyOWQ=|c8f644e355c08e774a1db3b8509dce83d1a4504998626ae4e1ea51ccab1857f9"; z_c0="2|1:0|10:1516691242|4:z_c0|92:Mi4xYm1EcEFRQUFBQUFBY0tzQjlrRUlEU1lBQUFCZ0FsVk5LaTFVV3dEbDV6blkwV19CNFRqYWlVMUhjaVRSdVFNLS13|a15fc0caf5eb0542e3f92676d10d486034b87c4922d3a467d3b2fd539e5c28a2"; __utma=155987696.1315096443.1516688149.1516688149.1516691387.2; aliyungf_tc=AQAAAM3Iowm1TwEAHyuttLIG9bzmrZg+; d_c0="ACBt7MpZFQ2PTtdenvWLztGzQi-3fwHctnY=|1517551124"; _xsrf=6a2499c0-9cb0-46e2-a43c-8f3a41af2c44',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
x = 0
while id <= end_id:
    print('请求' + str(id))
    offset = 0
    flag = False
    try:
        while not flag:
            get_url = 'https://www.zhihu.com/api/v4/questions/'+ str(id) +'/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset='+str(offset)
            req = urllib.request.Request(get_url,  headers = header)
            response=urllib.request.urlopen(req).read().decode('utf-8')
            txt=json.loads(response)
            img_urls = re.findall(r'data-original=\"(.*?.)\"',str(txt))
            old_url = ''
            for img_url in img_urls:
                if img_url != old_url:
                    print(img_url)
                    try:
                        x+= 1
                        img_data = urllib.request.urlopen(img_url).read()
                        output = open('images/' +str(x)+'.jpg', 'wb')
                        output.write(img_data)
                        output.close()
                        old_url = img_url
                    except:
                        pass
            flag = txt['paging']['is_end']
            offset += 20
    except:
        print(str(id) + ':请求失败')
        id = id + 1
        continue
    print(str(id) + ':请求请求成功')
    id = id + 1
