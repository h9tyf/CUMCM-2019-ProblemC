info = dict()
sl = dict()
# 添加
info[0] = {'农', '林', '牧', '渔', '菜', '木', '花', '大闸蟹', '猕猴桃'}
sl[0] = {11, 0}
info[1] = {'矿'}
sl[1] = {17, 0}
info[2] = {'食品', '服装', '药', '制造', '鞋', '灯', '饰', '门窗', '调味品', '家居', '化工',
           '家电', '电器', '电子', '金属', '材料', '设备', '实业', '汽车美容', '物资', '空调',
           '工艺品', '机械', '办公', '五金', '地毯', '厨房', '纺织', '卫浴', '机械', '轮胎',
           '机电', '器械', '钢', '塑料', '纸', '合金', '童装', '汽贸', '塑胶'}
sl[2] = {17, 0}
info[3] = {'电力', '热力', '燃气', '水', '天然气', '石化', '电气'}
sl[3] = {11, 0}
info[4] = {'建筑', '土木', '建设', '建材', '景观', '园艺', '路', '桥'}
sl[4] = {11, 0}
info[5] = {'批发', '零售'}
sl[5] = {17, 0}
info[6] = {'交通', '运输', '邮政', '物流', '快递', '运业', '货运', '运贸'}
sl[6] = {11, 6, 0}
info[7] = {'住宿', '餐饮'}
sl[7] = {17, 6, 0}
info[8] = {'信息', '软件', '科技', '通讯', '通信', '网络'}
sl[8] = {17, 11, 6, 0}
info[9] = {'金融', '保险', '商贸', '财务', '贸易', '发展', '个体经营', '工贸'}
sl[9] = {17, 6, 0}
info[10] = {'房地产'}
sl[10] = {11, 0}
info[11] = {'租赁', '服务', '劳务', '人力资源', '咨询', '税务', '律师', '策划', '工程检测', '质量检验测试', '招投标代理'}
sl[11] = {17, 11, 0}
info[12] = {'研究', '技术', '科技'}
sl[12] = {6, 0}
info[13] = {'水利', '生态', '环境', '公共设施', '土地', '地质', '环保'}
sl[13] = {17, 11, 6, 0}
info[14] = {'居民服务', '修理', '物业', '维修'}
sl[14] = {17, 6, 0}
info[15] = {'教育'}
sl[15] = {6, 0}
info[16] = {'卫生', '社会工作', '消防'}
sl[16] = {17, 6, 0}
info[17] = {'新闻', '出版', '广播', '电视', '电影', '录音', '文化', '艺术', '体育', '娱乐', '广告', '图书', '设计', '影城', '印'}
sl[17] = {17, 6, 0}
info[18] = {'机关', '机构', '组织', '管理'}
sl[18] = {6, 0}
info[19] = {'国际组织'}
sl[19] = {6, 0}

for i in range(0, 20):
    if len(info[i]) > 3:
        count = 0
        for elem in iter(info[i]):
            count = count + 1
            if count == 4:
                break
            if not count == 1:
                print("，", end="")
            print('%s' % elem, end="")
        print("......")
    else:
        count = 0
        for elem in iter(info[i]):
            count = count + 1
            if not count == 1:
                print("，", end="")
            print('%s' % elem, end="")
        print("")

