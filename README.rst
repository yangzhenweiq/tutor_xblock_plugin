opencraft-poll xblock for cms 

需要安装tutor工具，https://docs.tutor.overhang.io/

目前安装tutor 使用的源码安装，在tutor/plugins/目录下使用:

   git clone ... xpoll.

使用源码安装：

   pip install -e .

安装步骤:

     - tutor plugins list
     - tutor plugins enable xpoll
     - tutor config save
     - tutor images build openedx
     - tutor local quickstart 

创建超级用户：

    - tutor local createuser --superuser yourname youremail

导入demo课程：

    - tutor local importdemocourse
     
在studio 课程 advanced settings下面：

   在Advanced Module List 添加 'poll'




     
     


