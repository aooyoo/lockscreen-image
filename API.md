
#### 交互数据规范

*   客户端需要启用http cookie
*   客户端若需要POST数据，就按照各自API定义的数据进行, 发送的是标准HTML 表单
*   服务端返回客户端的数据为json

    格式：

    ```
    {
        ret: 返回码,
        data: 返回数据
    }
    ```

    *   ret 0 表示成功，此时根据不同请求会（或不会）带有data字段
    *   ret 非0 表示失败，此时不会有data字段




## API

版本    |   时间        | 描述
--------|---------------|----------
v1.0    |   2015-01-17  | 创建
v1.1    |   2015-01-22  | 修改

----------------


功能                  |   URL                                                            |  Method   |  Description           
----------------------|------------------------------------------------------------------|-----------|-------------------------
登录                  | `/login/`                                                        | POST      | 每次APP打开后第一个请求.
获取背景 最热         | `/background/hot/?bucket=<bucket-id>`                            | GET       | 获取最热背景. 
获取背景 最新         | `/background/new/?bucket=<bucket-id>`                            | GET       | 获取最新背景. 
获取前景 最热         | `/foreground/hot/?category=<category-id>&bucket=<bucket-id>`     | GET       | 获取最热前景. 
获取前景 最新         | `/foreground/new/?category=<category-id>&bucket=<bucket-id>`     | GET       | 获取最新前景. 
获取前景分类          | `/foreground/category/`                                          | GET       | 获取前景分类.
收藏                  | `/collect/`                                                      | POST      |
取消收藏              | `/uncollect/`                                                    | POST      |
下载                  | `/download/`                                                     | POST      |
获取收藏的前背景组合  | `/collect/show/?bucket=<bucket-id>`                              | GET       |
反馈                  | `/feedback/`                                                     | POST      |


--------


#### `/login/`

###### Request

POST Form:
*   udid:   udid
*   phone:  手机型号代码

###### Response

```
{
    'ret': 0,
    'data': {
        'version': <version>,               # 最新版本
        'copyright': <copyright text>       # 版权申明
    }
}
```

login 过后，根据response， 客户端http client 应该自动设置cookie


--------

#### `/background/hot/?bucket=<bucket-id>`
#### `/background/new/?bucket=<bucket-id>`


###### Request

GET PARAM:
*   bucket: <bucket-id>

    bucket-id 是一个抽象概念，如果没有此参数，服务器返回是当前排序规则中前45（暂定）个元素.
    客户端每页显示多少，服务端不关心，并且客户端自己分页。


    当用户快要滑动到最后时，可以发送下一个请求（请求中的bucket-id为当前返回中的next_bucket_id），获取新的数据


###### Response

```
{
    'ret': 0,
    'data': {
        'next_bucket_id': <bucket-id>,
        'images': [
            {
                'ID': <image id>,
                'url': <image url>
            },
            {
                'ID': <image id>,
                'url': <image url>
            },
            ...
        ]
    }
}
```

返回的`<bucket-id>`如果为数字，表示后续还有内容，如果为`NULL` ,表示后续没有内容


--------


#### `/foreground/hot/?category=<category-id>&bucket=<bucket-id>`
#### `/foreground/new/?category=<category-id>&bucket=<bucket-id>`

###### Request

GET PARAM:
*   category: 分类ID，如果没有这个参数，表示获取所有图片
*   bucket: 同上

###### Response

同上


--------


#### `/foreground/category/`

获取前景分类
###### Request

无

###### Response

```
{
    'ret': 0,
    'data': [
        {
            'ID': <分类1 ID>,
            'name_zh': <分类1 中文名字>,
            'name_en': <分类1 英文名字>,
            'icon': <icon1  url>
        },
    
        {
            'ID': <分类2 ID>,
            'name_zh': <分类2 中文名字>,
            'name_en': <分类2 英文名字>,
            'icon': <icon2  url>
        },

        ...
    
    ]
}
```

**NOTE:** 默认ID为2的分类是 我的收藏


--------

#### `/collect/`

收藏

###### Request

POST Form:
*   background: `<background-id>`
*   foreground: `<foreground-id>`

###### Response

```
{
    'ret': 0
}
```

--------

#### `/uncollect/`

取消收藏

###### Request

同上

###### Response

同上




--------

#### `/download/`

下载

同上


--------

#### /collect/show/

获取已经收藏的前背景组合

###### Request
GET PARAM:
*   bucket: 同上

###### Response

```
{
    'ret': 0,
    'data': {
        'next-bucket-id': <bucket-id>,
        'items': [
            {
                'background': {
                    'ID': <ID>,
                    'url': <url>,
                }
                'foreground': {
                    'ID': <ID>,
                    'url': <url>,
                }
            },

            {
                'background': {
                    'ID': <ID>,
                    'url': <url>,
                }
                'foreground': {
                    'ID': <ID>,
                    'url': <url>,
                }
            },

            ...
        ]
    }
}

```

返回按照收藏时间排序，最新收藏排在前面


--------

#### `/feedback/`

反馈

###### Request
POST Form:
*   email: 用户邮箱 - 可选
*   country: 用户国家 - 可选 （最好是自动检测手机地区设置，自动获取国家）
*   content: 反馈的内容 - 比选

###### Response

```
{
    'ret': 0,
}
```



## 错误代码

见 [errorcode.json](/errorcode.json)

