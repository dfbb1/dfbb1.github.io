静态页面生成说明|project|code|test

# 静态页面生成说明
## 工具演示说明

> quote格式展示  
> 本页面使用py-markdown2转换生成，代码样式参考 **pygment** [https://github.com/richleland/pygments-css]和css/code.css文件  
> 其他样式可在css/page.css进行自定义

### 页面结构说明 
1. markdown文件首行默认为元数据，build.py解析时，不会转为html。元数据使用|分割，第一项为文章名，第二项为html文件存储目标目录，默认在pages目录下，第二项及后续项均为tag分类标签  
2. 一级标题样式参考‘静态页面生成说明’标题，二级标题参考‘本页面由项目内工具生成’，二级页面默认转为副标题格式，其他标题为默认格式  

### 样式展示  
斜体字： *这是一行斜体字*  
粗体字： **这是一行粗体字**  

这是一段代码：  
```python
if __name__ == '__main__':
    engine = markdown2.Markdown(extras=['fenced-code-blocks'])
    parent_dir = 'resources'
    mds = os.listdir(parent_dir)
    for md in mds:
        f = open(parent_dir + os.sep + md, mode='r', encoding='utf-8')
        tags = f.readline().strip().split('|')
        print('=' * 60)
        html = engine.convert(f.read())
        print(html)
```

这是无序列表：  

- 静态页面生成说明  
- 本页面由项目内工具生成  

### 侠客行  
赵客缦胡缨，吴钩霜雪明。  
银鞍照白马，飒沓如流星。  
十步杀一人，千里不留行。  
事了拂衣去，深藏身与名。  
闲过信陵饮，脱剑膝前横。  
将炙啖朱亥，持觞劝侯嬴。  
三杯吐然诺，五岳倒为轻。  
眼花耳热后，意气素霓生。  
救赵挥金槌，邯郸先震惊。  
