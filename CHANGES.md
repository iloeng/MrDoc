## 版本更新记录

### v0.9.6 2025-07-02

- [新增]docker-compose.yml文件和基于docker compose的一键更新脚本；
- [新增]语言配置选项参数可忽略浏览器环境强制使用设置的语言；
- [新增]验证用户Token接口返回用户昵称和用户类型字段数据；
- [新增]用户Token获取文集信息接口；
- [新增]用户TokenAPI上传附件接口；
- [新增]支持config.ini配置文件preview配置项；
- [修复]测试邮件头不符合某些邮件供应商协议的问题;
- [修复]editormd编辑器工具栏插入分割线点击无效的问题；
- [修复]Editormd编辑器文档在Android webview83、iOS 14等低版本浏览器不渲染文档的问题；
- [修复]Markdown编辑器图片语法align属性设置right和left无效的问题；
- [修复]docker-update.sh脚本在某些环境下默认没有执行权限的问题；
- [优化]docker-compose.yml文件添加默认dns配置；
- [优化]用户Token API获取文集列表接口支持过滤和排序字段参数；
- [优化]用户Token获取单篇文档接口支持获取协作文集的文档；
- [优化]用户Token获取文集列表接口支持传递kw参数进行文集搜索；
- [优化]优化在线表格内容的存储和渲染效率；
- [优化]添加默认允许的跨域请求头；
- [优化]调整默认uwsgi配置http->http-socket；
- [优化]升级Markdown编辑器代码块高亮组件库，支持更多代码块高亮语法；
- [优化]带分享码的私密文档分享链接支持自动提交验证；
- [优化]导入本地Word文件时将wmf等格式图片转换为png格式以支持显示；
- [优化]Markdown编辑器工具栏echart图表功能可选择常见图表和粘贴echarts官方示例图表代码；

### v0.9.5 2025-02-17

- [新增]站点数据和媒体文件导出功能；
- [新增]editormd编辑器支持iframe语法和图片语法设置图片显示比例；
- [新增]editormd编辑器iframe视频语法支持设置视频宽高；
- [新增]文档页面下载PDF功能；
- [修复]升级PIL库导致验证码图片显示异常的问题；
- [修复]富文本编辑器发布文档异常的问题；
- [修复]editormd编辑器附件上传按钮无响应的问题；
- [修复]配置文件项Session会话过期时间配置不支持的问题；
- [修复]Editormd编辑器文档目录层级不缩进的问题；
- [修复]部分移动端设备首页样式错位的问题；
- [修复]部分情况下分页文集大纲页面不切换到当前文档所在页的问题；
- [优化]首页未登录状态不显示新建菜单；
- [优化]重构editormd编辑器、Markdown渲染器，统一站点图标风格；
- [优化]更新dockerfile文件；
- [优化]日志文件输出结构；
- [优化]设置COOP策略；
- [优化]文集访问码验证页面对不同类型文集URL的兼容；
- [优化]移动端首页头部样式；
- [优化]移动端设备下文集大纲侧边栏切换的交互体验；
- [优化]editormd编辑器编辑文档未保存时关闭浏览器将弹框提示；

### v0.9.4 2024-11-01

- [**重要提示！！！**]
- Docker 部署方式需升级 Docker 镜像至 v9.0；
- 其他部署方式需升级 Python 版本至 3.11；
- [**依赖库更新**]
- Python 版本：基准版本升级至 Python 3.11.3，最低支持版本为 Python 3.9；
- Django 框架：版本升级至4.2.16；
- PyPDF2 模块替换为 pypdf;
- Selenium 升级至 4.25.0；
- [**数据库支持版本更新**]
- MySQL数据库：支持 8.0 及以上版本；
- PostgreSQL数据库：支持 12 及以上版本；
- MariaDB数据库：支持 10.4 及以上版本；
- Oracle数据库：支持 19c 及以上版本；
- [**功能优化**]
- 优化文集最新文档选项卡文档URL链接；
- 优化首页文集列表文集URL；
- 优化404页面；
- 优化Markdown行内公式字体与文本保持一致；
- [**问题修复**]
- 修复login.html 以及 register.html 中的验证码URL问题；

### v0.9.3 2024-08-14

- [新增]用户Token获取指定文集信息接口；
- [新增]文集序列化器返回文集作者昵称和文集文档数量字段；
- [新增]配置文件支持对Session会话进行配置；
- [新增]支持从配置文件中关闭附件格式验证；
- [新增]站点默认搜索模式配置；
- [新增]个人中心Token管理的Token二维码显示；
- [修复]后台扫描未使用图片时分页未重置的问题；
- [修复]文集导出文件mrdoc.yaml文件结构不正确的问题；
- [修复]文档分享页面顶部和底部信息块内容样式错位的问题；
- [修复]后台页面信息块配置保存无效的问题；
- [修复]修复邮箱配置发送测试邮件异常的问题；
- [修复]登录页面重定向参数跳转漏洞；
- [修复]CNVD-C-2024-34161漏洞；
- [修复]用户tokenAPI删除文档接口不支持json请求体的问题；
- [优化]后台概览页面结构；
- [优化]后台管理和个人中心左侧主菜单；
- [优化]增强zip附件上传的安全验证；
- [优化]附件上传时的格式验证逻辑；
- [优化]XSS过滤；
- [优化]升级Vditor编辑器版本至3.10.4；
- [优化]用户TokenAPI获取文集文档列表接口以分页方式返回数据；
- [优化]文集页面目录大纲在超多文档时异步分页显示；
- [优化]异步加载文集目录的文档链接处理；
- [优化]升级jQuery库版本；
- [优化]优化后台站点设置项；
- [优化]支持文集协作用户分享非本人创建的文档；
- [优化]文档进行复制/移动时支持对目标文集进行搜索筛选；


### v0.9.2 2024-01-23

- [新增]用户Token获取文集层级目录接口新增文档数量数据； 
- [新增]用户Token删除文档（软删除）接口；
- [新增]用户Token验证Token接口；
- [新增]支持配置根路径域名验证文件等文本文件访问；
- [新增]后台管理扫描未使用图片功能；
- [修复]editor.md编辑器iframe视频渲染问题；
- [修复]文档分享页代码高亮失效的问题；
- [优化]用户Token Api接口的POST请求支持提交json数据；
- [优化]更新登录限制URL白名单；
- [优化]默认允许来自obsidian的跨域请求；
- [优化]用户Token修改文档接口可设置上级文档参数；
- [优化]文档页面转发弹出框样式；
- [优化]文集列表文集简介文本显示；
- [优化]editormd编辑器添加思维导图示例；
- [优化]更新依赖库版本；

### v0.9.1 2023-07-29

- [优化]全文搜索无结果时提示切换「精准搜索」；
- [优化]搜索页面文字提示；
- [优化]文档移动复制指定的上级文档可以为目标文集内任意已发布文档；
- [优化]注册和登录功能逻辑判断；
- [优化]增强上传URL类型图片的URL验证；

### v0.9.0 2023-05-24

- [修复]后台附件管理附件地址链接错误的问题；
- [优化]Editormd编辑器预览界面代码高亮效果与实际渲染效果保持一致；
- [优化]注册和登录页面显示备案号；
- [优化]邮件From头信息设置；
- [优化]Markdown图片无法加载时提示加载失败；

### v0.8.9 2023-04-24
- [修复]获取文档上下篇文档为空的问题；
- [优化]下线网页端文集导入功能，改由本地导入程序提供；
- [优化]更新登录限制URL白名单；
- [优化]文集内文档搜索结果摘要显示；
- [优化]uWSGI配置文件限制日志大小；
- [优化]文档搜索词高亮逻辑；
- [优化]从文集内文档搜索界面进入文档自带搜索词参数；
- [优化]文档页面样式；

### v0.8.8 2023-03-15

- [新增]用户 Token API 获取文档的上下篇文档接口；
- [新增]用户 Token API 获取个人文档列表接口；
- [新增]用户 Token API 获取文集目录接口；
- [优化]用户 Token API 新建文档接口支持指定文档上级；
- [优化]文档内下级文档链接形式为`/doc/xxx/`；

### v0.8.7 2023-02-15

- [新增]文档浏览页日间/夜间模式切换功能；
- [新增]配置文件支持配置 CSRF 可信来源；
- [修复]editor.md编辑器英文引号渲染自动为中文引号的问题；
- [修复]文集导出为 Markdown 压缩包时部分图片导出失败的问题；
- [修复]文档长代码展开功能失效的问题；
- [优化]文档搜索词高亮渲染逻辑；
- [优化]导出文集时支持导入文档内 `<img>`标签的本地图片；
- [优化]非公开文集下的文档均可由创建者进行文档分享；
- [优化]editor.md编辑器文档中代码块未指定编程语言的样式渲染；
- [优化]文集zip文件导入相关功能函数；

### v0.8.6 2023-01-15

- [新增]用户Token API文集列表接口文集创建时间字段；
- [新增]用户Token API文集列表接口文集文档数量字段；
- [新增]站点地图可通过配置文件关闭；
- [优化]删除用户时对用户所属内容的处理；
- [优化]文集作者可下载协作成员创建的文档；

### v0.8.5 2022-11-30

- [新增]邮箱配置信息测试发送功能；
- [新增]禁用更新检测功能及其配置项；
- [修复]修复部分设备 importlib-metadata 版本变动导致项目运行失败的问题；
- [优化]取消 iframe 白名单相关配置及限制；
- [优化]增加 card 类型代码块颜色位；
- [优化]合并 PR[#153](https://github.com/zmister2016/MrDoc/pull/153)；

### v0.8.4 2022-10-31

- [新增]配置文件X_FRAME配置选项支持被跨域嵌入iframe；
- [新增]`/project/xxx/`形式的文集URL；
- [修复]标签文档页代码不高亮、不可复制的问题；
- [优化]全站文档搜索页面精准搜索和全文搜索切换方式；

### v0.8.3 2022-09-30

- [修复]个人中心个人配置编辑器默认选中项不显示的问题；
- [修复]带跳转参数登录成功后不会跳转至相应URL的问题；
- [修复]文集导入中文名称乱码的问题；
- [优化]后台管理左边侧栏名称；
- [优化]个人中心 token 管理页面的文字提示；
- [优化]合并PR[!29 优化dockerfile](https://gitee.com/zmister/MrDoc/pulls/29)
- [优化]调整文档URL形式为/doc/xxx；

### v0.8.2 2022-08-31

- [新增]Editor.md编辑器代码块一键复制功能；
- [修复]文档分享中在线表格不自适应浏览器宽高的问题；
- [修复]editormd编辑器序列图不渲染的问题；
- [优化]导入本地TXT文本文件后文档名称包含点号的问题；
- [优化]取消文档页面的打赏弹出框；
- [优化]后台新增用户和管理员的异常信息提示；
- [优化]附件白名单配置文字提示；
- [优化]个人中心导出文集弹出框样式；
- [优化]文档编辑器附件选择窗口的附件管理跳转链接；

### v0.8.1 2022-07-31

- [修复]某些情况下上传图片重复覆盖的问题；
- [优化]更新搜索主页底部版权信息；
- [优化]默认uwsgi配置；
- [优化]移除editormd编辑器已废弃emoji语法的表情选项卡；
- [优化]文档编辑器跳转到文档模板管理的链接；
- [优化]版本更新检测功能，移除默认更新提醒弹出框；
- [优化]手机移动端页面 iframe 样式；

### v0.8.0 2022-06-30

- [修复]editor.md编辑器时间线内mark标记不渲染的问题；
- [修复]用户token api 修改文档接口权限验证有误的问题；
- [修复]Firefox浏览器下登录、注册等页面导致电脑CPU飙升的问题；
- [优化]文集页面直接跳转到个人中心文集管理页面功能；
- [优化]文档页面直接跳转到个人中心文档管理页面功能；
- [优化]新建文档页面直接跳转到个人中心文集管理、文档管理页面功能；
- [优化]修改文档页面直接跳转到个人中心文档管理页面功能；
- [优化]首页底部MrDoc标识，调整为「Powered By MrDoc」；
- [优化]文档模板编辑页面（新建/修改）到个人中心各菜单的跳转；

### v0.7.9 2022-05-31

- [新增]站点跨域支持；
- [修复]Markdown文档中附件文件名包含空格时无法正确解析的问题；
- [修复]全文搜索高亮富文本文档时导致异常的问题；
- [修复]文档回收站相关文档过滤器导致页面异常的问题；
- [修复]开启全站登录后文档分享中的图片不显示的问题；
- [修复]用户token api 无法上传URL图片的问题[!28](https://gitee.com/zmister/MrDoc/pulls/28)；
- [修复]Debug调试模式下静态文件500异常的问题；
- [修复]部分情况下文档摘要导致文集页响应卡顿的问题；
- [修复]异步加载文集左侧目录产生错误的问题；
- [优化]首页底部样式；
- [优化]取消Editor.md编辑器emoji语法；
- [优化]编辑器插入附件的文件名显示；
- [优化]Docker启动脚本，重建索引命令后台执行；
- [优化]用户token api新建文集接口返回文集ID；
- [优化]在线表格文档自适应浏览器窗口高度；
- [优化]添加log目录；
- [优化]同步Vditor编辑器版本至3.8.15；

### v0.7.8 2022-04-30

- [新增]个人中心文档管理「已删除文档」数量显示和跳转；
- [修复]管理员导出文集MD压缩包提示「文集不存在」的问题；
- [修复]部分指定文集新建文档时存在文集目录重复加载的问题；
- [修复]文集页面「最新文档」选项卡中富文本文档摘要显示为None的问题；
- [修复]管理员批量删除文档时部分文档删除不了的问题；
- [修复]个人中心文档数量不匹配的问题；
- [修复]首页新建文集的样式问题[#I50XRV](https://gitee.com/zmister/MrDoc/issues/I50XRV)；
- [优化]注册页面用户名输入框和用户名错误提示；
- [优化]个人中心文集成员管理中用户名的显示；
- [优化]用户token相关接口以适配桌面客户端0.1.9；
- [优化]首页底部样式；
- [优化]调整uwsgi超时时间配置；
- [优化]Markdown压缩包文集导入中文处理；
- [优化]系统配置默认自带移动端APP所需的跨域白名单；

### v0.7.7 2022-03-31

- [修复]Safari浏览器下文档页面底部部分按钮被遮挡的问题；
- [修复]文集页面目录大纲中文档名称超长时遮盖下方目录的问题；
- [修复]精准搜索文档时文档内容为空导致请求异常的问题；
- [优化]文档标题字段长度限制放宽至255个字符；
- [优化]在线表格文档的页面宽度调整为浏览器可视宽度；
- [优化]调整注销请求逻辑，避免可能的CSRF攻击；

### v0.7.6 2022-03-01

- [合并][!25](https://gitee.com/zmister/MrDoc/pulls/25)修复iceEditor截图粘贴上传
- [优化]文档页面转发按钮文字标识；
- [优化]升级Editor.MD编辑器Echarts组件版本至5.3.0；

### v0.7.5 2022-01-30

- [新增]后台管理-文集管理-文集成员修改页面；
- [新增]跨域相关配置参数读取；
- [修复]后台管理修改文集成员后跳转回个人中心文集列表页面的问题；
- [修复]开启「强制登录」后忘记密码链接不能访问的问题；
- [修复]Editor.md编辑器流程图错位的问题(更新flowchart.js版本)；
- [优化]更新 Vditor 编辑器组件版本至3.8.10；

### v0.7.4 2021-12-30

- [新增]接口对桌面客户端的支持；
- [修复]文集导出解析文档图片导致导出失败的问题；
- [修复]版本检测更新异常的问题；
- [修复]@符号导致Markdown链接解析异常的问题；
- [优化]取消框架层级的数据上传大小限制；
- [优化]登录错误次数超过6次将锁定10分钟；
- [优化]更新依赖库版本；
- [优化]优化后台管理图片管理图片预览；

### v0.7.3 2021-11-29

- [新增]用户 Token API 新增上传转存URL图片接口；
- [修复]导入文集zip文件后只能对一个文档进行操作的问题；
- [修复]文集列表文集简介撑开页面高度的样式问题;
- [优化]在线表格文档的页面宽度自适应；
- [优化]文集zip导入成功发布后的弹出框提示；
- [优化]编辑器插入图片弹出框图片分组按钮样式；
- [优化]用户token api新建文集对文集名称的校验；
- [优化]用户Token api 列表接口添加排序；

### v0.7.2 2021-10-30

- [新增]个人中心本地文档批量导入到文集功能；
- [修复]Markdown文集Zip压缩包文件导入文档名称乱码的问题；
- [修复]ice富文本编辑器中插入图片URL链接的XSS漏洞;
- [修复]base64图片上传时的图片格式验证问题；
- [优化]忘记密码输入错误次数超过5次将限制10分钟；
- [优化]「草稿」状态的文档可通过文档浏览URL预览草稿文档内容；
- [优化]文档排序值默认调整为9999；
- [优化]文档目录样式；
- [优化]登录注册验证码大小写忽略；
- [优化]上传URL图片接口校验图片格式；
- [优化]用户修改密码需要验证原有密码；

### v0.7.1 2021-09-29

- [新增]安全报告SECURITY.md；
- [修复]用户上传文件中yaml加载的安全漏洞；
- [修复]文集文档拖拽排序第三级文档排序失效的问题；
- [修复]附件限制在个人中心附件管理上传无效的问题；
- [修复]Markdown文集导入文档排序的问题；
- [修复]文集创建者和高级协作者无法复制/移动协作者创建的文档的问题；
- [优化]zip文集导入的处理；
- [优化]默认禁止上传SVG图片（有安全风险）；
- [优化]文档名称XSS过滤；
- [优化]站点管理和个人中心页面；
- [优化]文档全文搜索生成索引时的异常处理；

### v0.7.0 2021-08-31

- [新增]修改文档页面快捷键（Ctrl+S）保存;
- [新增]文集大纲广告位4；
- [修复]Editor.md编辑器标题链接不显示的问题；
- [修复]Vditor编辑器文档目录显示问题；
- [优化]修改文档页面「查看文档」功能；
- [优化]文档浏览页面「下载文档」样式；
- [优化]站内搜索logo；
- [优化]启用新的产品中文名称：觅思文档；
- [优化]文集列表首页底部样式；
- [优化]项目配置读取逻辑；

### v0.6.9 2021-07-26

- [新增]后台管理中心的图片管理和附件管理功能；
- [新增]站点搜索中文档搜索支持「全文搜索」和「匹配搜索」功能和切换开关；
- [新增]后台文档管理文档历史记录页面和接口；
- [修复]vditor编辑器粘贴多图片文本时图片只有一张图的问题;
- [修复]找回密码邮件发送失败的问题；
- [修复]后台管理用户管理用户无法搜索的问题；
- [修复]文档访问权限可绕过的问题；
- [修复]MySQL数据库下文档删除失败的问题；
- [优化]个人中心我协作的文集页面及功能；
- [优化]后台邮件服务器配置逻辑和页面展示；
- [优化]文档发布和修改的异常判断和处理；
- [优化]首页移动端控制栏样式；
- [优化]文集内搜索文档；
- [优化]后台文档管理文档编辑模式显示；
- [优化]后台图片管理图片预览功能；
- [优化]文档历史记录对比接口；
- [优化]403页面；
- [优化]图片上传格式处理；

### v0.6.8 2021-06-27

- [新增]文档页面支持OGP协议；
- [新增]后台站点设置文档长代码显示控制选项；
- [修复]开启「全站登录」后URL跳转异常的问题；
- [修复]Vditor编辑器编写的文档搜索高亮文档不解析的问题；
- [修复]Vditor编辑器粘贴上传图片异常的处理；
- [修复]开启「全站登录」后Token接口重定向到登录页面的问题；
- [优化]用户禁止同名文集创建，文集下禁止同名文档创建；
- [优化]文集导出异常提示；
- [优化]Vditor文档目录样式；
- [优化]同步LayUI组件库版本至2.6.8；
- [优化]同步PearAdminLayui组件库版本至3.8.3；
- [优化]文档编写页面保存逻辑；
- [优化]导出Markdown压缩包时文件名校验过滤；
- [优化]PDF导出的文档类型；

### v0.6.7 2021-05-29
- [新增]表格文档支持Excel文件(.xlsx格式)导入；
- [新增]后台管理用户管理的用户资料修改功能；
- [修复]XSS过滤漏洞；
- [修复]分享文档内容渲染问题；
- [修复]文集导入保存排序时部分文档状态未变的问题；
- [修复]管理员无法批量删除其他用户文集的问题；
- [优化]文档类型标识；
- [优化]文档标签相关页面；
- [优化]后台检测更新逻辑；
- [优化]文档分享码输入页面样式；

### v0.6.6 2021-04-11

- [新增]站点语言配置项，英文和繁体中文语言包；
- [新增]文集批量导出Markdown压缩包；
- [新增]首页文集列表访问码文集标识；
- [新增]在线表格类型文档支持；
- [修复]无法复制/移动文档到协作文集的问题；
- [修复]版本检测的问题；
- [优化]文集下载选项状态控制；
- [优化]用户注册和新增的逻辑判断与页面提示；


### v0.6.5 2021-03

- [新增]图片批量管理功能；
- [新增]Editor.md编辑器插入Unicode Emoji 表情符号；
- [优化]文集Markdown压缩包导入支持YAML层级关系声明元数据；
- [优化]文集导出Markdown压缩包包含文集元数据文件（yaml）
- [优化]后台可配置用户登录需验证码；
- [优化]附件上传格式大小写通配；
- [优化]文档全文搜索；
- [优化]个人中心和后台管理按钮样式与主题统一；
- [优化]后台管理的用户管理功能；
- [优化]文集导出PDF；
- [优化]文档编辑器界面布局；
- [优化]同步Vditor组件版本至3.8.2；
- [优化]文档搜索结果简易高亮；
- [优化]草稿状态的文档支持预览查看；
- [优化]页面跳转逻辑；
- [优化]Editor.md编辑器编写文档的文档目录滚动；
- [合并]dockerfile和Docker环境的启动脚本；

### v0.6.4 2021-02

- [优化]文集的高级权限协作用户可对文集文档进行排序；
- [优化]文集页面大纲目录样式；
- [优化]重置密码代码逻辑；
- [优化]更新图标字体，新增左侧文集大纲文档图标；
- [优化]Editor.md代码块样式和恢复工具栏标题；
- [优化]文档发布后的页面调整逻辑；
- [优化]文档编辑器页面新建文集后默认选中新建的文集；
- [优化]删除文集时进行二次确认；
- [修复]文档管理页面搜索文档获取协作文集列表错误的问题；
- [修复]管理员无法为非自己创建的文集添加协作用户的问题；
- [修复]Editor.md编辑器在移动端输入中文自动换行的问题；
- [修复]图片文件名包含空格时引用不显示的问题；
- [新增]获取当前版本号的URL和视图；
- [新增]用户Token新建文集接口；
- [新增]Markdown编辑器的Markdown文本高亮标记语法；
- [新增]首页文集置顶功能；
- [合并]GitHub [#61Editor.md编辑器引用块样式](https://github.com/zmister2016/MrDoc/pull/61)

### v0.6.3 2021-01

- [优化]文档编辑页面HTML模板；
- [修复]文档编辑器插入图片的异常；
- [升级]同步Vditor组件版本至3.7.1；
- [新增]富文本编辑器iceEditor;
- [优化]Vditor编辑模式下移动端输入体验;
- [新增]文集图标配置功能；
- [新增]Word(.docx格式)文档导入功能；
- [优化]文档编辑器界面样式和交互；
- [修复]仅有私密文集的站点游客可搜索到私密文集的问题；
- [新增]文集水印配置；
- [新增]文集文档收藏功能；
- [优化]首页样式；


### v0.6.2 2020-12

- [优化]个人中心和后台管理页面加载页面时间；
- [优化]文集文档页面左侧文集目录交互体验；
- [优化]Editor.md编辑器模式下图片上传异常交互；
- [优化]同步Vditor编辑器组件版本至3.6.6；
- [优化]HTML模板文件结构和代码结构；
- [优化]后台管理、个人中心的文集管理、文档管理界面切换为动态表格；
- [新增]个人中心文集文档拖拽排序功能；
- [新增]文档搜索全文搜索功能；
- [新增]个人中心文集管理的文集搜索功能；
- [新增]文档编辑器浏览器缓存功能；
- [合并]文集简介优化[!1](https://gitee.com/zmister/MrDoc/pulls/1)
- [合并]Editor.md编辑器自定义文档样式[#42](https://github.com/zmister2016/MrDoc/pull/42)

### v0.6.1 2020-11-16

- 优化文集介绍页面，文集简介支持Markdown渲染；
- 优化个人中心和后台管理界面样式；
- 优化文集协作用户的添加；
- 优化文档目录样式；
- 优化移动端文档页面样式
- 优化同步Vditor编辑器组件版本至3.6.2；
- 优化从图片库插入图片到文档编辑器的图片链接；
- 新增私密文集的文档分享功能；
- 新增个人中心文集管理批量删除功能；
- 新增Vditor编辑器模式下图片粘贴上传功能；
- 新增文档的下级文档目录展开功能；
- 修复附件上传的一些问题；
- 修复游客状态无法搜索标签的问题；


### v0.6.0 2020-10-18

- 新增站点名称、副标题、备案号、关键词等站点信息配置功能；
- 新增文集转让功能；
- 新增后台对文档图片缩略显示的配置；
- 新增Vditor编辑器模式插入文档模板功能；
- 新增Editormd编辑器模式下时间线语法的支持；
- 新增首页文集的排序配置，支持升序和降序配置；
- 修复导入文集的文档内容无法搜索的问题；
- 前台页面和后台页面默认显示用户昵称，用户昵称为空时显示用户名；
- 升级Vditor组件库版本至3.5.5；

### v0.5.9 2020-09-26

- 新增对Vditor编辑器的支持，个人中心可选择编辑器；
- 新增文档iframe域名白名单配置，后台可设置允许使用的外站iframe视频；
- 调整文集目录渲染方式，改为后端渲染；
- 新增文集目录定位跳转，在长目录下当前文档的目录显示在目录最顶端；
- 新增后台配置允许上传的附件格式和附件大小；
- 新增后台配置允许上传的图片大小；
- EditorMD编辑器模式下优化文档页面JS加载，按需加载各类JS文件，提高文档渲染速度；

### v0.5.8 2020-08-30

- 优化和调整首页功能链接和样式；
- 优化和调整文档浏览页面样式；
- 优化和调整文档编辑器页面样式；
- 优化和调整个人中心页面样式；
- 优化图片分组的新建的逻辑，避免同名分组的产生；
- 优化个人中心图片上传功能，在指定分组页面上传的图片将归属到特定图片分组；
- 优化用户注册逻辑，限制用户名类型和长度；
- 新增文档标签功能；
- 新增个人中心仪表盘页面功能；
- 新增个人中心个人资料修改页面功能；
- 新增后台管理新增管理员功能；
- 基于Token的API新增获取文集下文档列表和获取单篇文档接口；

### v0.5.7 2020-08

- 修复搜索的权限问题
- 修复文集协作的权限问题；
- 优化文档目录显示；
- 优化文集协作管理；
- 优化文档编辑器排版；

### v0.5.6 2020-07-31

- 修复Markdown编辑器插入图片、表格、音视频等内容时光标丢失的问题；
- 优化重构搜索功能，支持在搜索界面进行文集和文档搜索；
- 优化文档页面排版显示；
- 优化文档页面代码块超长超宽代码样式；
- 优化移动复制文档弹出框大纲超长的样式；
- 优化epub和PDF格式文件导出；
- 优化编辑器界面排版布局；
- 优化文档三级目录渲染错误的问题；

### v0.5.5 2020-07-20

- 禁用编辑器页面的列表目录和下拉目录语法解析
- Chrome扩展添加鼠标选择控制选项
- 优化文档样式
- 添加文集导入功能
- 优化文集目录加载速度
- 编辑器支持音视频外链和视频网站外链
- 编辑器添加字符统计功能
- 优化文档页面分享样式
- 优化文档编辑器排版布局
- 新增图片上传的URL链接插入

### v0.5.4

- 修复Chromium配置参数未启用的问题
- 修复后台电子邮箱配置的问题
- 优化文集文档浏览页面滚动条样式
- 优化大数量文档下目录加载导致的性能问题


### v0.5.3

- 添加编辑器引用JS的版本号
- 修复开启全站登录时登录注册页面样式丢失的问题
- 完善图片上传对图片大写后缀格式的支持
- 优化个人中心文档管理，支持按文集筛选文档
- 优化移动端阅读体验
- 修复编辑器行号挤压的问题
- 完善删除文档时的权限验证
- 文档页面添加图片放大镜功能
- 添加文档回收站功能

### v0.5.2 2020-05-24

- 添加Chrome内核浏览器扩展
- 添加API访问接口；
- 优化配置路径；
- 增强代码安全性；
- 优化个人中心图片、文档模板的默认排序；
- 优化注册邀请码最大使用次数验证；
- 添加Markdown编辑器对 Echarts 图表功能的支持；
- 支持文档的复制和移动到其他文集；

### v0.5.1 2020-05-08

- 优化个人中心交互体验；
- 添加站点异常报错的日志功能；
- 优化项目结构；
- 修改文档页面新增删除文档功能；
- 优化首页样式排版；
- 后台支持设置全站强制登录；

### v0.5.0 2020-05-02

- MrDoc正式中文取名：觅道文档；
- 文档编辑器添加Markdown折叠功能；
- 思维导图支持图形高度设置；
- 优化文集导出EPUB文件功能；
- 新增PDF文件导出功能；
- 新增一个广告位；
- 优化文集名称字符验证；


### v0.4.2 2020-04-20

- 添加思维导图功能的支持，可以在文档编辑器通过图标和`mindmap`标识代码块来创建脑图；
- 首页添加文集筛选、文集排序和文集网格/列表视图切换；
- 文档编辑器优化表格插入按钮，新增粘贴Excel内容转Markdown的功能；
- 优化交互体验；

### v0.4.1 

- 添加文档历史版本功能，可在修改文档时对比查看和选择恢复文档的历史版本；
- 优化文档阅读页面样式，调整悬浮的目录样式；
- 优化编辑器交互，增加所有网络请求的加载框显示；
- 优化文集阅读页面样式，新增文集创建的管理链接；

### v0.4 2020-04-06

- 新增附件功能，可在个人中心管理附件，在文档编辑器中上传和添加附件；
- 重构文档编辑页面布局，界面排版更加友好，涉及新建文档页面、修改文档页面、新建文档模板页面、修改文档模板页面；
- 添加首页文集搜索功能和分页功能；
- 优化文档编辑器，重写表格组件，文档表格可以先填写内容在插入到Markdown编辑器中，预览界面a标签链接以新窗口的方式打开；；
- 优化个人中心和后台管理文档搜索，支持文档内容和标题搜索；
- 优化个人中心和后台管理页面、首页和文集、文档浏览页面移动端样式；

### v0.3.4 2020-04-03

- 添加基于用户的API模块，支持通过用户Token获取文集、新建文档和上传图片；
- 优化文档编辑页面布局；
- 添加文集协作者功能，文集支持多用户协同协作了；
- 修改文档阅读页面的文档内链接新窗口打开；

### v0.3.3 2020-03-21

- 修复后台管理无法删除文档的错误；
- 修复后台新建无法新建文集的错误；
- 优化图片上传逻辑，新增后台图片管理功能，前端编辑器替换Editor.md自带的图片上传组件；
- 优化首页无文集时的样式，添加默认显示的图片；
- 优化首页文集无文档时，显示默认提示文字；
- 优化404页面，更换统一风格的404图片；
- 调整文档阅读页面目录使用悬浮弹出框显示；
- 增强安全性，替换前端请求字符串值中的特殊符号；

### v0.3.2 2020-03-12

- 修复访问码跳转文档404的错误；


### v0.3.1 2020-03-10

- 紧急修复sitemap导致的makemigrations错误；
- 修改文集下载导出模型外键字段类型；
- 调整文集和文档的URL结构；
- 更新依赖库文件；

### v0.3.0 2020-03-07

- 优化MD文件导出逻辑，修复文档中本地资源不存在引发异常的问题；
- 个人中心文集管理页面文集MD文件导出的交互；
- 去除首次请求的Cookie检查，避免正常文档产生404的问题；
- 优化首页文集列表样式，修复文集名称过长的显示问题，添加文集的最新文档；
- 添加文集的EPUB导出功能，支持全站启停文集的前台导出和作者对单一文集的前台导出控制；
- 升级Layui版本至2.5.6

### v0.2.12

- 优化Markdown编辑器的扩展工具栏按钮，未选择文本时点击“楷”按钮，光标移动到span标签中间；
- 优化文集内点击新建文档操作体验，在文集内点击【新建】按钮，跳转到文档新建页面后自动选择所属文集；
- 优化新建文档页面的布局，使之更适合在中等屏幕下的操作；
- 当Django的Debug设置为True时，后台会显示站点目前处于Debug调试模式；
- 添加站点地图sitemap功能；


### v0.2.11 2020-02-24

- 修复:删除文档导致其子文档找不到父级文档从而产生异常的Bug；
- 优化管理员界面文档管理的筛选功能,支持按文档状态进行筛选；
- 优化修改文档后的跳转判断；
- 优化文档阅读页面、新建文档页面和修改页面的无序列表样式；
- 优化文档阅读页面指定语言的代码块样式，去除prism代码高亮插件，避免其与editormd的样式冲突；
- 更改文档保存的HTML内容为预览时的HTMl而非editormd渲染的HTML；
- 添加Markdown编辑器对流程图和序列图的支持；
- 添加Markdown编辑器对部分HTML标签的识别和解析；


### v0.2.10 2020-02-22

- 优化修改文档页面的文档状态提示；
- 新增注册邀请码功能，可在后台配置管理；

### v0.2.9 2020-02-17

- 优化文本编辑器排版
- 优化文档发布成功时候的跳转路径
- 优化编辑器预览的样式
- 添加页脚信息
- 优化文档修改页面排版
- 添加文档编辑页面中文集的权限显示


### v0.2.8 2020-01-15

- 文档页添加上一篇文档和下一篇文档链接；
- 优化文集样式，私密文集会在首页和文集、文档页使用锁图标标识；
- 优化文档搜索页面样式；
- 在Django调试模式下(DEBUG=True)不启用统计代码和广告代码；

### v0.2.7 2020-01-01

- 添加文件权限控制功能，支持：公开、私密、指定用户可见、访问码可见4中权限模式；
- 优化部分样式；

### v0.2.6 2019-12-18

- 优化文档编写页面布局；
- 添加文档编写页面可插入本地文本文件内容的功能；
- 添加站点版本号信息

### v0.2.5

- 添加文档的草稿功能；
- 优化编辑页面退出时的提示；
- 优化个人中心和管理后台页面样式；

### v0.2.4 

- 优化文档编写页面结构
- 优化首页、文集列表页、文集页、文档浏览页、文档编写页在移动端的显示；

### v0.2.3 2019-12-08

- 优化Markdown内容目录样式；
- 修复文档修改时间不生效的Bug；
- 添加文档左侧目录可展开收缩功能，默认只显示第一级目录；
- 调整文集页显示逻辑，默认显示文集简介和文集目录大纲；
- 添加用户后台的文集导出功能，支持导出文集的Markdown文件压缩包；


### v0.2.2 2019-12-01

- 添加MrDoc全站favicon图标
- 添加后台配置关闭注册功能、启用邮箱功能、统计代码、广告代码等功能
- 添加通过邮箱找回密码功能
- 优化管理员界面退出后403的处理
- 优化文档浏览界面文档渲染加载逻辑

### 2019-11

- 添加404页面视图
- 完善首页文集列表简介样式
- 完善后台管理员对文集的权限逻辑

### 2019-08
MrDoc第一版发布

