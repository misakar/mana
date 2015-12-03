mana 重构
===

    mana 现在还不够强大，只是实现了最基本的功能，mana的最终目的是在后端做成
    和django的命令一样强大，同时支持前端快速创建mock数据,
    一键导入mock模版到数据库生成测试数据库

## 现在的mana

    存在的问题

### 1: 代码的实现过分依赖系统命令,导致系统兼容性不好,同时整套配置不灵活

    一些系统命令要调用python的模块手写, 比如创建文件的touch,
    Windows上并没有这个函数
    对于配置的灵活性需可以采用正则表达式实现

### 2: 对于后端只实现了基础的功能，还需要:

    1. 一个命令集成flask_login
    2. 自带 admin site
    3. 更智能的处理数据库(当前数据库的处理功能还足够)

### 3: 对于前端，要更加方便前后端交互

    使用mana进行前后端交互
    前端:
        $ mana init project --fe=true
    后端:
        $ mana init project --be=true
    json数据一键导入数据库
        $ mana import xxx.json to xxx.sqlite
        [利用request.json写入: 数据库实现方法]

### 4: 性能

    一些地方最好可以改成C++处理

### 5: 目标: django
