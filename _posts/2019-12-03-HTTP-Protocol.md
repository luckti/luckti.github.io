---
title: "HTTP Protocol"
categories:
  - Notes
  - Web
  - Reading
tags:
  - Notes
  - HTTP
excerpt_separator: <!--more-->
last_modified_at: 2019-12-03T04:57:43-08:00
---
> 《图解HTTP》-上野宣著，于均良译。读书笔记，知识整理。
<!--more-->

# 重点知识思维导图
### TCP/IP的分层管理
![image-center]({{ '/imgs/web/TCP_IP-level.png' | absolute_url }}){:.align-center}
### TCP协议的三次握手
![image-center]({{ '/imgs/web/TCP_three-way_handshaking.png' | absolute_url }}){:.align-center}
### 告知服务器意图的HTTP方法
![image-center]({{ '/imgs/web/HTTP_method.png' | absolute_url }}){:.align-center}
### HTTP 返回结果状态码
![image-center]({{ '/imgs/web/HTTP_sate_code.png' | absolute_url }}){:.align-center}
### HTTP+加密+认证+完整性保护=HTTPS
HTTP的缺点：
- 通信使用的明文可能被窃听
- 不验证通信方的身份就可能遭遇伪装
- 无法证明报文的完整性

HTTPS就是身披SSL(Secure Socket Layer)外壳的HTTP：HTTP<->***SSL***<->TCP

HTTPS 混合加密机制
![image-center]({{ '/imgs/web/HTTPS_crypto.png' | absolute_url }}){:.align-center}

证明公开密钥正确性的证书：需要权威结构认证，维护费用提高。-> 各种浏览器都会自带捆绑常用的认证机构证书。

# 名词区分
### URI 和 URL
**URL**(Uniform Resource Locator): 表示资源的**地点**（互联网中所在的位置）<br>   -> http://www.baidu.com
{: .notice--info}
**URI**(Uniform Resource Identifier): 表示**某一**互联网资源 <br>   -> http://www.baidu.com/xxx/index.html
{: .notice--info}

### 通信数据转发程序：代理、网关、隧道
**代理**：一种转发功能的应用程序，接收有客户端发送的请求并转发给服务器，同时也接收服务器返回的响应并转发个客户端。<br>
PS: 代理有两种基本分类： 是否**使用缓存**；是否**修改报文**。
{: .notice--info}
**网关**：转发其他服务器通信数据的服务器，接收从客户端发来的请求时，它就像自己拥有资源的源服务器一样对请求进行处理。<br>
PS: 利用网关可以由HTTP请求转化为其他协议通信。
{: .notice--info}
**隧道**：在相隔甚远的客户端和服务器两者之间进行中转，并保持双方通信连接的的应用程序。
PS：通过隧道可以实现远距离服务器的安全通信。若隧道本身是**透明**的，客户端不会在意隧道的存在。
{: .notice--info}

