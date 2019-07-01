# @Author  :lgx
# @Time    :2019-04-02 12:41
# @File    :输出公司对应的秘钥.py

'''
在秘钥文件中找到对应的公司,并把公司和秘钥输出到新的文件
'''
guande=['广东广安冠德石化有限公司深圳分公司',
'深圳市顺归加油站有限公司',
'深圳市雄伟李氏经贸物资有限公司威程油气站',
'广东广安冠德石化有限公司惠州鸿业电力加油站',
'广东广安冠德石化有限公司乳源富诚加油站',
'广东广安冠德石化有限公司四会市贞山加油站',
'广东广安冠德石化有限公司金乐园加油站',
'四会市凯平加油站有限公司',
'广东广安冠德石化有限公司肇庆市四通北通加油站',
'广东广安冠德石化有限公司东莞塘厦林村加油站',
'东莞市永安石油化工有限公司第二加油站',
'台福油品（深圳）有限公司坪地加油站',
'西安市长安区八一加油站',
'广东广安冠德石化有限公司珠海和平界冲加油站',
'深圳市宝安广安冠德石油贸易有限公司上南加油站',
'中山市古镇七坊加油站',
'东莞市黄江东盛加油站有限公司',
'济南鉴德石油化工有限公司',
'山东中惠泽石油有限公司',
'成都鸿浩加气站有限公司'
]
jieshun=['深圳市顺易通信息科技有限公司',
'深圳市信利康物业管理有限公司',
'陕西鑫华泰物业管理有限公司',
'厦门市湖里华龙实业公司',
'厦门市阳光家园物业服务有限公司海沧分公司',
'广州鼎通晟物业管理有限公司',
'广州富利物业管理有限公司',
'深圳音乐厅运营管理有限责任公司深圳音乐厅停车场',
'广州科建投资管理有限公司',
'西安市享泰物业管理有限公司',
'深圳市福田农产品批发市场有限公司停车场',
'安徽八里河旅游开发有限公司',
'深圳市华侨城物业服务有限公司武汉分公司',
'深圳市新润园物业发展有限公司理想时代大厦停车场',
'成都新谷投资集团有限公司',
'成都百扬嘉欣物业服务有限公司',
'天津盛信商业管理有限公司',
'南京江城物业管理有限公司',
'汇隆置业（杭州）有限公司',
'同泰电子实业（深圳）有限公司同泰总部产业园停车场',
'广东省机场管理集团有限公司惠州机场公司',
'深圳巴士集团股份有限公司公交大厦停车场']

def match_company(company_list,pwd):
    exist=[]
    for i in company_list:
        f = open('C:/Users/lgx/Desktop/税号和密钥.txt', 'r', encoding='utf-8')
        line = f.readline()
        while line:
            if i in line:
                line=line.split(':')
                #print(line[0],line[1],line[3])
                company_shuihao_key='   '.join([line[0],line[1],line[3]])
                print(company_shuihao_key.strip())
                with open(pwd, 'a', encoding='utf-8') as f:
                    f.write(company_shuihao_key)
                exist.append(i)
                break
            line = f.readline()
    f.close()
    print("=="*25)
    #print(len(exist))
    no_exist=set(company_list)-set(exist)
    # print(list(no_exist))
    for i in list(no_exist):
        print("%s秘钥不存在"%i)



def main():
    guande_pwd='C:/Users/lgx/Desktop/冠德各公司秘钥.txt'
    #match_company(guande,guande_pwd)
    jieshun_pwd='C:/Users/lgx/Desktop/捷顺各公司秘钥.txt'
    match_company(jieshun,jieshun_pwd)


if __name__ == '__main__':
    main()
