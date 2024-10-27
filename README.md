# TUICalculator - 一款简单的终端计算器


[English Version](#TUICalculator---A-Simple-Terminal-Calculator)
## 项目介绍

TUICalculator 是一个基于 Python 的终端计算器，采用现代化的界面设计，支持多种基本和高级数学运算。该计算器使用 `curses` 库构建，具有友好的用户交互界面，能够在终端中运行，适合各种平台。

## 功能特点

- 支持基本运算（加、减、乘、除）
- 高级数学函数支持（如：sin、cos、tan、sqrt、log、exp）
- 简单的用户输入和输出显示
- 可通过按键导航选择按钮
- 清除输入和结果的功能
- 可通过 'Quit' 按钮退出应用程序

## 技术栈

- Python 3.x
- `curses` 库

## 安装与运行

1. 确保你的系统中已安装 Python 3.x。
2. 将代码下载或克隆到本地计算机。
3. 在终端中运行以下命令：

   ```bash
   python3 calc.py
   ```
   或者
   ```bash
   ./calc
   ```

5. 通过键盘导航选择按钮并输入数学表达式。

## 使用示例

- 按下数字键或运算符键进行输入。
- 按下 `C` 清除当前输入。
- 按下 `=` 计算结果。
- 按下 `Quit` 退出程序。

## 测试

该项目包含单元测试，用于验证数学函数的前缀添加功能。可通过运行以下命令执行测试：

```bash
python3 calc.py --test
./calc --test
```

## 贡献

欢迎提交问题和请求！

## License

MIT License

---


# TUICalculator - A Simple Terminal Calculator

[中文版](#TUICalculator---一款简单的终端计算器)

## Project Overview

TUICalculator is a Python-based terminal calculator that features a modern interface design, supporting a variety of basic and advanced mathematical operations. Built using the `curses` library, this calculator provides a user-friendly interactive interface and can run in the terminal across various platforms.

## Features

- Supports basic operations (addition, subtraction, multiplication, division)
- Advanced mathematical function support (e.g., sin, cos, tan, sqrt, log, exp)
- Simple user input and output display
- Key navigation for button selection
- Functionality to clear input and results
- Exit the application using the 'Quit' button

## Tech Stack

- Python 3.x
- `curses` library

## Installation and Running

1. Ensure you have Python 3.x installed on your system.
2. Download or clone the code to your local machine.
3. Run the following command in your terminal:
```bash
   python3 calc.py
```
   or
```bash
   ' ./calc '
```

4. Use keyboard navigation to select buttons and input mathematical expressions.

## Usage Example

- Press number or operator keys for input.
- Press `C` to clear the current input.
- Press `=` to compute the result.
- Press `Quit` to exit the program.

## Testing

This project includes unit tests to verify the prefix addition functionality for mathematical functions. You can run the tests with the following command:
```bash
python3 calc.py --test
./calc --test
```
## Contributing

Feel free to submit issues and requests!

## License

MIT License
