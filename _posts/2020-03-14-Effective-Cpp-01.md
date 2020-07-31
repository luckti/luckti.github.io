---
title: "视 C++ 为一个语言联邦"
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
last_modified_at: 2020-03-14T01:13:56-08:00
---
>《Effective C++》- Scott Meyers著，侯捷译。<br><br>
>   条款 01: View C++ a federation of languages.<br><br>
> 【C / Object-Oriented C++ / Template C++ / STL】四部分组成了C++语言联邦。
> C++ 高效编程守则视状况而变化，取决于你是用C++的哪一个部分。
<!--more-->

### 四种次语言
- **C** <br> C是C++的基础。C的局限：没有模板（templates），没有异常（exception是），没有重载（overloading）......
- **Object-Oriented C++** <br> 面向对象之古典守则在C++上的最直接实施。classes，封装（encapsulation）、继承（inheritance）、virtual 函数（动态绑定）......
- **Template C++** <br> C++ 的泛型编程（generic programing）部分。=> 模板元编程（TMP，template metaprograming）。TMP相关规则很少与C++主流编程互相影响。
- **STL** <br> 一个template 程序库。对容器（container）、迭代器（iterators）、算法（algorithms）、函数对象（function objects）的规约有极佳的紧密配合和协调。

***pass-by-value*** vs ***pass-by-reference***
- **C** 次语言内，***pass-by-value*** 通常比 ***pass-by-reference*** 高效。
- **OO/template C++** 中，***pass-by-reference***-const 往往更好。
- **STL** 中，由于迭代器和函数对象都是在C指针之上塑造出来的，所有此时 ***pass-by-value*** 通常更好。

***more*** ...