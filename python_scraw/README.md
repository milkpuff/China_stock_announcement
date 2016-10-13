## 该脚本从巨潮网络的服务器上将公告下载，并对公告进行规范命名，把每条公告的相关信息存入数据库中。
## 使用之前需要建好数据库的四张表，并把数据库的信息补充到相应位置。
## 所涉及的文件路径和日志路径可随项目需求进行调整。
## 公告命名方法为：
* 上市公司：股票代码（6位）+YYYYMMDD(8位)+ 当日当支股票公告的排序号(3位)
* 监管公告：监管代码(3或4位) ＋ YYYYMMDD（8位） ＋ 序号(2位)
## 运行方法参见代码最后一段
* 简单执行 python cninfo_main.py sse 即将当日上市公司的股票下载到默认位置，并更新数据库。