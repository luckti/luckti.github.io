---
title: "尽可能使用 const"
# image: 
#   path: /imgs/ 
#   thumbnail: /imgs/ 
categories:
  - Notes
  - 读书笔记
tags:
  - Effective C++
  - C++
excerpt_separator: <!--more-->
last_modified_at: 2020-03-14T08:37:23-08:00
---
>《Effective C++》- Scott Meyers著，侯捷译。<br><br>
>   条款 03: Use const whenever possible.<br>
> - 将某些东西声明为const可帮助编译器侦测出错误用法。const 可被施加于任何作用域内的对象、函数参数、函数返回类型、成员函数本体。
> - 编译器强制实施 bitwise constness，但你编写程序时应该使用“概念上的常量性”（conceptual constness)。
> - 当 const 和 non-const 成员函数有着实质等价的实现时，令 non-const 版本调用 const 版本可避免代码重复。
<!--more-->
