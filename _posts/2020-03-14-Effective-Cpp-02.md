---
title: "尽量以 const, enum, inline 替换 #define"
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
last_modified_at: 2020-03-14T08:37:19-08:00
---
>《Effective C++》- Scott Meyers著，侯捷译。<br><br>
>   条款 02: Prefer `const`s, `enum`s, and `inline`s to `#define`s.
> - 对于单纯常量，最好以`const`对象或`enum`s替换`#define`s。
> - 对于形似函数的宏（macros），最好改用`inline`函数替换`#define`s。
<!--more-->