---
title: "[C++]类型转换和类型强制转换"
categories:
  - Notes
tags:
  - Notes
excerpt_separator: <!--more-->
last_modified_at: 2020-09-01T04:36:07-08:00
---
**Type Conversion and Casting**
> - 强烈建议在代码中坚持只使用新式的类型强制转换
> - 尽量少使用转型操作，尤其是dynamic_cast，耗时较高，会导致性能的下降，尽量使用其他方法替代。
<!--more-->

## 赋值语句的类型转换
```c++
int number {};
// f 标识为单精度浮点型，F效果一样。如果没有f则是double类型
flaot decimal {2.5f};
number = decimal;
```

自动进行类型转换，存在丢失信息的风险。

## 老式的类型强制转换

显示强制转换为： <br>
`(dst_type)expression`  <br>
-> `strips_per_roll = (int)(roollLength / height)`

> PS: 使用老式的类型强制转换更容易出错——它们往往不能清楚地说明你的意图，可能得不到期望的结果。=> 强烈建议在代码中坚持只使用新式的类型强制转换（见下文）。

## 新式的类型强制转换
新式的类型强制转换有三种类型：
- `static_cast` 静态地检查类型强制转换（在**编译**程序时检查）
- `dynamic_cast` 动态地检查类型强制转换（在**执行**程序时检查）
- `reinterpret_cast` **无条件**的强制转换
- `const_cast` 用于去除指针的常量属性

语句格式(以 `static_cast` 为例)为： <br>
`static_cast<dst_type>(expression)` <br>
->  `strips_per_roll = static_cast<int>(roollLength / height)`

> PS: 尽量少使用转型操作，尤其是dynamic_cast，耗时较高，会导致性能的下降，尽量使用其他方法替代。

## 使用场景举例[^1] [^2] [^3]
[^1]:[官方教程](http://www.cplusplus.com/doc/tutorial/typecasting/)
[^2]:[static_cast和dynamic_cast详解](https://blog.csdn.net/u014624623/article/details/79837849)
[^3]:[【c++】强制类型转换-static_cast、dynamic_cast、reinterpret_cast、和const_cast](https://blog.csdn.net/qq_40416052/article/details/82558451)

### `static_cast`
static_cast可以在指向相关类的指针之间执行转换，不只是upcast（从pointer-to-derive 到 pointer-to-base），还可以进行向下转换（从pointer-to-base到pointer-to-derive ）。在运行时不执行检查，以保证被转换的对象实际上是目的地类型的完整对象。因此，由程序员来确保转换是安全的。另一方面，它不会产生动态转换的类型安全检查的开销。

特点：

1. 用于类层次结构中基类（父类）和派生类（子类）之间指针或引用的转换。
  - 进行上行转换（把派生类的指针或引用转换成基类表示）是安全的；
  - 进行下行转换（把基类指针或引用转换成派生类表示）时，由于没有动态类型检查，所以是不安全的。
2. 用于基本数据类型之间的转换，如把int转换成char，把int转换成enum。
3. 把空指针转换成目标类型的空指针。
4. 把任何类型的表达式转换成void类型。

> 注意：static_cast不能转换掉expression的const、volatile、或者__unaligned属性
   
```c++
class Base {};
class Derived: public Base {};
Base * a = new Base;
Derived * b = static_cast<Derived*>(a);
```
### `dynamic_cast`
dynamiccast只能用于指针和对类（或void*）的引用。它的目的是为了确保类型转换的结果指向目标指针类型的有效完整对象。

dynamic_cast主要用于类层次间的上行转换和下行转换，还可以用于类之间的交叉转换（cross cast）。

在类层次间进行上行转换时，dynamic_cast和static_cast的效果是一样的；在进行下行转换时，dynamic_cast具有类型检查的功能，比static_cast更安全。dynamic_cast是唯一无法由旧式语法执行的动作，也是唯一可能耗费重大运行成本的转型动作。

特点：

1. 用于有继承关系的类指针间的转换
2. 用于有交叉关系的类指针间的转换
3. 具有类型检查的功能
4. 需要虚函数的支持

```c++
// dynamic_cast
#include <iostream>
#include <exception>
using namespace std;

class Base { virtual void dummy() {} };
class Derived: public Base { int a; };

int main () {
  try {
    Base * pba = new Derived;
    Base * pbb = new Base;
    Derived * pd;

    pd = dynamic_cast<Derived*>(pba);
    if (pd==0) cout << "Null pointer on first type-cast.\n";

    pd = dynamic_cast<Derived*>(pbb);
    if (pd==0) cout << "Null pointer on second type-cast.\n";

  } catch (exception& e) {cout << "Exception: " << e.what();}
  return 0;
}
```
### `reinterpret_cast`
reinterpret_cast可以将任何指针类型转换为任何其他指针类型，甚至是不相关的类。 操作结果是从一个指针到另一个指针的值的简单二进制副本。 允许所有指针转换：既不检查指向的内容，也不检查指针类型本身。

它还可以从整数类型转换指针。这个整型值表示指针的格式是特定于平台的。唯一的保证是，一个指针被投射到一个足够大的整数类型，保证能够将其转换回一个有效的指针。

特点：

1. 用于指针类型间的强制转换	 
2. 用于整数和指针类型间的强制转换

```c++
class A { /* ... */ };
class B { /* ... */ };
A * a = new A;
B * b = reinterpret_cast<B*>(a);
```

### `const_cast`
这种类型的转换操纵指针所指向的对象的常量，要么被设置要么被移除。 例如，为了将const指针传递给期望非const参数的函数：
```c++
// const_cast
#include <iostream>
using namespace std;

void print (char * str)
{
  cout << str << '\n';
}

int main () {
  const char * c = "sample text";
  print ( const_cast<char *> (c) );
  return 0;
}
```