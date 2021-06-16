from pyquery import PyQuery as pq

a = '''
<body>
    <h><a href='www.biaoti.com'>head</a></h>
    <p>段落1</p>
    <p>段落2</p>
</body>
'''

# 提取内容
"""提取标签内容，用.text()
提取标签属性值，用.attr()
提取子孙节点内容用.text()，如果只提取子节点用.html()，可能提取出来的是子节点的整个标签"""

doc = pq(a)
# 提取标签内容
doc('h').text()  # 'head'
doc('h').html()  # '<a href="www.biaoti.com">head</a>'
doc('body').html()  # '\n    <h><a href="www.biaoti.com">head</a></h>\n    <p>段落1</p>\n    <p>段落2</p>\n'
doc('p').text()  # '段落1 段落2'
doc('p').text().split(' ')  # ['段落1', '段落2']
doc('p:nth-of-type(1)').text()  # '段落1'
doc('body').text()  # 'head 段落1 段落2'

# 提取标签属性
doc('h a').attr('href')  # 'www.biaoti.com'

# 识别标签

# 只根据标签来识别
#
# 找到所有名为a的标签
# 找到名为a或b的标签
# 因为思路和xpath非常相似，所以直接上代码

b = '''
<body>
    <h1>head</h1>
    <h2>标题2</h2>
    <h2>标题3</h2>
</body>
'''

doc = pq(b)
doc('h1').text()  # 'head'
doc('h1, h2').text()  # 表示“或”用逗号 'head 标题2 标题3'
