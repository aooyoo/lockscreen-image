# 所屏应用图片库


## 约定

#### 手机型号代码

型号         |  代码
-------------|------
iPhone4      | i4
iPhone5      | i5
iPhone6      | i6
iPhone6 Plus | i6p


#### 交互数据规范

*   API采用REST URL
*   客户端把手机UDID和型号代码 以get params的形式加在url后面
*   客户端若需要POST数据，就按照各自API定义操作
*   服务端返回客户端的数据为json

    格式：

    {
        ret: 返回码,
        data: 返回数据
    }

    ret 0 表示成功，此时根据不同请求会（或不会）带有data字段
    ret 非0 表示失败，此时不会有data字段




## API

版本    |   时间        | 描述
--------|---------------|----------
v1.0    |   2015-01-17  | 创建


----------------


功能                   |   URL                                                            |  Method   |  Description           
-----------------------|------------------------------------------------------------------|-----------|-------------------------
登录                   | /login/                                                          | POST      | 每次APP打开后第一个请求.
获取背景 最热          | /background/hot/?bucket=<bucket-id>                              | GET       | 获取最热背景. 
获取背景 最新          | /background/new/?bucket=<bucket-id>                              | GET       | 获取最新背景. 
获取前景 最热          | /background/hot/?category=<category-id>&bucket=<bucket-id>       | GET       | 获取最热前景. 
获取前景 最新          | /background/new/?category=<category-id>&bucket=<bucket-id>       | GET       | 获取最新前景. 
获取前景分类           | /foreground/category/                                            | GET       | 获取前景分类.
收藏                   | /collect/                                                        | POST      |
下载                   | /download/                                                       | POST      |


--------


#### /login/

###### Request

POST Form:
*   udid:   udid
*   phone:  手机型号代码

###### Response

```
{
    'ret': 0,
    'data': {
        'secret-key': <KEY>
    }
}
```

后续请求需要把这个 KEY 加到HTTP HEADER中：

X-Secret-key0: KEY


--------

#### /background/hot/?bucket=<bucket-id>
#### /background/new/?bucket=<bucket-id>


###### Request

GET PARAM:
*   bucket: <bucket-id>

    bucket-id 是一个抽象概念，如果没有此参数，服务器返回是当前排序规则中前45（暂定）个元素.
    客户端每页显示多少，服务端不关心，并且客户端自己分页。

    当用户快要滑动到最后时，可以发送下一个请求，获取新的数据


###### Response

```
{
    'ret': 0,
    'data': {
        'next-bucket-id': <bucket-id>,
        'images': [url1, url2, url3,...]
    }
}
```

返回的<bucket-id>如果为数字，表示后续还有内容，如果为`NULL` ,表示后续没有内容


--------


#### /background/hot/?category=<category-id>&bucket=<bucket-id>
#### /background/new/?category=<category-id>&bucket=<bucket-id>

###### Request

GET PARAM:
*   category: 分类ID，如果没有这个参数，表示获取所有图片
*   bucket: 同上

###### Response

同上

#### /foreground/category/

获取前景分类
###### Request

无

###### Response

```
{
    'ret': 0,
    'data': [
        {
            'id': <分类ID>,
            'name': <分类名字>,
            'icon': <icon url>
        }
    
    ]
}
```



--------

#### /collect/

收藏

###### Request

POST Form:
*   background: <background-id>
*   foreground: <foreground-id>

###### Response

```
{
    'ret': 0
}
```

--------

#### /download/

下载

同上














