from flask import Flask,request
import requests
import re
app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def get_name():
    name = request.args.get('goods')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    response = requests.get(url='http://trash.lhsr.cn/sites/feiguan/trashTypes_2/TrashQuery_h5.aspx?kw={}'.format(name),
                            headers=headers)
    pattern = re.compile(r'style="font-size:.6rem; color:.*?;">(.*?)</span', re.S)
    result = pattern.findall(response.text)
    # 大件垃圾
    pattern2 = re.compile(r'<font class="txt-red" style="color:#A41E33;">(大件垃圾)</font>', re.S)
    result2 = pattern2.findall(response.text)
    if result == []:
        if result2 == ['大件垃圾']:
            return result2[0]
        result = ["没有找到你需要的垃圾，提示：",
                  "可回收物一般是废纸、废塑料、废玻璃、废金属、废衣物等可循环利用的生活废弃物",
                  "有害垃圾一般是废电池、废灯管、废药品、废油漆等有害人体健康或对自然环境造成危害的废弃物",
                  "湿垃圾是容易腐烂的垃圾，一般是剩饭剩菜，过期食品，瓜皮果核等等,"
                  "干垃圾是指除可回收物，有害垃圾，湿垃圾以外的其他废弃物"]
    return "没有找到你需要的垃圾，提示：\n可回收物一般是废纸、废塑料、废玻璃、废金属、废衣物等可循环利用的生活废弃物,\n有害垃圾一般是废电池、废灯管、废药品、废油漆等有害人体健康或对自然环境造成危害的废弃物,\n湿垃圾是容易腐烂的垃圾，一般是剩饭剩菜，过期食品，瓜皮果核等等,\n干垃圾是指除可回收物，有害垃圾，湿垃圾以外的其他废弃物"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=50000)
