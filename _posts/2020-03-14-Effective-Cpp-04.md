---
title: "确定对象被使用前已先被初始化"
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
last_modified_at: 2020-03-14T08:38:45-08:00
---
>《Effective C++》- Scott Meyers著，侯捷译。<br><br>
>   条款 04: Make sure that objects are initialized before they're used.<br>
> - 为内置型对象进行手工初始化，因为 C++ 不保证初始化它们。
> - 构造函数最好使用成员初值列（member initialization list），而不要在构造函数本体内使用赋值操作（assignment）。初值列列出的成员变量，其排列次序应该和它们在 class 中的声明次序相同。
> - 为免除“跨编译单元之初始化次序”问题，请以 local static 对象替换 non-local static 对象。
<!--more-->