# Auty

## Intro
    Auty是一个自动化测试的微框架

## Dirs
    1. actions文件夹：包含了和业务相关的包含可复用方法的脚本文件（根据业务的不同可以在actions文件夹下创建不同的业务文件夹）
    2. constants文件夹：包含了常量初始化的python脚本文件（根据业务划分可以再创建子文件夹或多个常量文件）
    3. data文件夹：包含了测试用的数据
    4. lib文件夹：包含了支持框架运行的python文件
    5. log文件夹：包含了运行测试过程中生成的日志文件
    6. results文件夹：包含了测试结果文件
    7. scripts文件夹：包含了scripts文件夹和selections文件夹
        * scripts文件夹下包含了测试脚本（可根据业务划分成多个子目录）
        * selections文件夹下包含了suite文件（包含了需要执行的脚本路径集合）
    8. utils文件夹：包含了和业务逻辑无关的包含可复用方法的脚本文件

## Files
    1. Auty文件夹下：
        __init__.py文件：包结构所必需文件（以下所有涉及可调用脚本的文件夹下均需有此文件）
        config.txt文件：Auty框架配置说明文件
        recovery.py文件：垃圾代码回收文件（用来回收执行测试过程中因故障未能自动删除的自动生成的代码）
        requirements文件：包含了框架所需要安装的python库信息
        setup.py文件：执行脚本以安装requirements文件中所包含的python库
        start.py文件：执行脚本以启动接口自动化测试
        
    2. lib文件夹下
        exe_deco.py文件：包含修饰脚本运行时方法的文件
        execute_selection.py文件：包含运行suite集合下脚本方法的文件
        generate_html.py文件：包含根据生成的csv格式测试结果文件生成html类型测试结果文件方法的文件
        generate_result.py文件：包含生成csv格式测试结果方法的文件
        read_selection.py文件：包含读取可执行的脚本列表方法的文件
        recovery_code.py文件：包含垃圾代码回收方法的文件
        write_log.py文件：包含生成日志文件方法的文件
        
    3. scripts文件夹下：
        create_selection.py文件：包含创建suite文件（all_scripts_selection.txt）方法的文件
        
## Steps
    1. 运行Auty/setup.py文件
    2. 编写接口测试python脚本并放到Auty/scripts/scripts目录（或子目录）下
    3. 运行Auty/scripts/create_selection.py文件生成Auty/scripts/all_scripts_selection.txt文件
    4. 修改Auty/scripts/all_scripts_selection.txt文件
    5. 自定义test_selection.txt文件（名字随意起）并放到Auty/scripts/selections文件夹下
    6. 运行Auty/start.py文件开始接口自动化测试
    7. 在Auty/results文件夹下生成的测试结果文件中查看测试结果
    
## More
* [python2](https://www.python.org/downloads/)
* [作者博客](http://www.cnblogs.com/LanTianYou/p/8313361.html)
* [Auty文档系列](http://www.cnblogs.com/LanTianYou/category/888691.html)
