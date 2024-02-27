"""
# encoding: utf-8
@version: ??
@author: zst
@site: 
@software: PyCharm
@file: run.py
@time: 2024/2/28 3:03
"""


class Choose:

    def __init__(self, name=""):
        self.choose = name
        self.data = {"c": '''#include<stdio.h>
    int main(void) {
        printf("Hello World!\n");
        return 0;
}''', "java": '''public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}''', "python": '''print("Hello World")''',"php":'''<?php
echo "Hello World";
?>''',"c++":'''#include<iostream>
Using namespace std;
int main()
{
    cout << "\nHello World!";
    return 0;
}''' ,"c#":'''using System;
namespace helloWorld
{
    class HelloWorld
    {
        static void Main(String[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}''',"vb":'''subsub main
msgbox "Hello World!"
end sub
}''',"r":'''cat("helloworld")''',"go":'''package main
import "fmt"
func main() {
    fmt.Println("Hello World!")
}'''}

    def print_data(self):
        result=self.data.get(self.choose.lower())
        if result:
            print(result)
        else:
            print("语言暂不支持，或没有这种语言！")
ch=Choose("java")
# ch.choose="c"
ch.print_data()