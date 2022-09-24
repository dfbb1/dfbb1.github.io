readme|project|util

# github.io博客
## markdown文件自动转html部署

### 搭建
1. 创建{username}.github.io为名的仓库
2. 点击右上角头像-Settings-Developer settings-Personal access tokens-Generate new token，这一步用于Github Action Markdown2Html脚本提交代码
3. 克隆本项目`.github/workflows`, `css`,  `js`, `build.py`, `index.html`到自己的仓库  
4. 新建sitemap.json文件，内容为`{}`  
5. 修改页面导航栏及其他样式


### 使用说明  
1. 提交html、css、js会触发pages build工作流，将静态文件部署到github.io
2. 提交.md后缀的文件会触发Markdown2Html工作流，将resource(默认文件夹)下的md文件转为html存入pages目录，然后commit、部署到github.io  
3. 每次.md文件变更，build.py会先校验md5是否改变，md5不改变不改动，文章的日期为首次生成html时间，可在`js/data.js`手动调整  
4. 首页默认展示归档列表，每页展示数再index.html修改`const pageSize = 改这里;`


### 存在的问题  
1. 文章使用iframe展示，避免换页闪烁，但是iframe访问地址被记录在浏览器历史记录，返回时会跳到iframe链接地址  
2. 目前使用markdown2转换html，对.md文本格式要求严格，例如段落后需要加两个空格再换行，否则html不换行