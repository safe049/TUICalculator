import curses
import unittest
import math
from unittest import mock

# 按钮类
class Button:
    def __init__(self, label, color_pair):
        self.label = label
        self.color_pair = color_pair
        self.x = 0
        self.y = 0

    def draw(self, stdscr, selected, max_y, max_x):
        # 计算边框的坐标
        border_y = self.y - 1
        border_x = self.x - 1
        label_width = max(len(self.label) + 2, 6)  # Minimum width for consistency

        # 确保绘制操作不会超出屏幕边界
        if border_y + 2 < max_y and border_x + label_width + 1 < max_x:
            if selected:
                # Draw filled background with gradient effect
                for i in range(3):
                    if border_y + i < max_y:
                        stdscr.addstr(border_y + i, border_x, ' ' * (label_width + 2),
                                      curses.A_REVERSE | curses.A_BOLD)
                # Draw centered text
                text_x = border_x + (label_width + 2 - len(self.label)) // 2
                if text_x < max_x:
                    stdscr.addstr(border_y + 1, text_x, self.label,
                                  curses.A_REVERSE | curses.A_BOLD)
            else:
                # Draw modern border with rounded corners
                if border_y < max_y:
                    stdscr.addstr(border_y, border_x, '╭' + '━' * label_width + '╮')
                if border_y + 1 < max_y:
                    stdscr.addstr(border_y + 1, border_x, '│' + ' ' * label_width + '│')
                if border_y + 2 < max_y:
                    stdscr.addstr(border_y + 2, border_x, '╰' + '━' * label_width + '╯')
                # Draw centered text
                text_x = border_x + (label_width + 2 - len(self.label)) // 2
                if text_x < max_x:
                    stdscr.addstr(border_y + 1, text_x, self.label, self.color_pair)

def update_button_positions(buttons, max_x):
    # Improved button layout with better spacing
    button_width = 10
    spacing = 3
    start_x = (max_x - (4 * (button_width + spacing))) // 2
    for i, button in enumerate(buttons):
        button.x = start_x + (i % 4) * (button_width + spacing)
        button.y = 8 + (i // 4) * 4

def draw_frame(stdscr, max_x, max_y):
    try:
        # Draw outer frame
        for y in range(max_y - 1):  # Subtract 1 to prevent writing to last line
            stdscr.addstr(y, 0, '║' + ' ' * (max_x - 3) + '║')  # Subtract 3 to account for border chars
        stdscr.addstr(0, 0, '╔' + '═' * (max_x - 3) + '╗')
        stdscr.addstr(max_y - 2, 0, '╚' + '═' * (max_x - 3) + '╝')
    except curses.error:
        pass

def add_math_prefix(expr):
    # 检查并添加 math. 前缀
    for func in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
        expr = expr.replace(func + '(', 'math.' + func + '(')
    return expr

def calculator(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Input/Output color
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Special buttons (C, Quit)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Advanced functions (sin, cos, etc.)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Normal buttons (0-9)

    input_str = ''
    result = ''
    buttons = [
        Button('1', curses.color_pair(4)), Button('2', curses.color_pair(4)), Button('3', curses.color_pair(4)), Button('+', curses.color_pair(4)),
        Button('4', curses.color_pair(4)), Button('5', curses.color_pair(4)), Button('6', curses.color_pair(4)), Button('-', curses.color_pair(4)),
        Button('7', curses.color_pair(4)), Button('8', curses.color_pair(4)), Button('9', curses.color_pair(4)), Button('*', curses.color_pair(4)),
        Button('0', curses.color_pair(4)), Button('C', curses.color_pair(2)), Button('=', curses.color_pair(4)), Button('/', curses.color_pair(4)),
        Button('Quit', curses.color_pair(2)),
        Button('sin', curses.color_pair(3)), Button('cos', curses.color_pair(3)), Button('tan', curses.color_pair(3)),
        Button('sqrt', curses.color_pair(3)), Button('log', curses.color_pair(3)), Button('exp', curses.color_pair(3)), Button('pi', curses.color_pair(3))
    ]

    current_selection = 0
    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Draw main frame
        draw_frame(stdscr, max_x, max_y)

        # Update button positions with centered layout
        update_button_positions(buttons, max_x)

        # Display header with modern style
        title = "TUICalculator"
        title_x = (max_x - len(title)) // 2
        if title_x >= 0:
            stdscr.addstr(2, title_x, title, curses.A_BOLD | curses.color_pair(1))

        # Display input/output area
        input_box_width = max_x - 8
        stdscr.addstr(3, 4, "╭" + "━" * input_box_width + "╮", curses.color_pair(2))
        stdscr.addstr(4, 4, f"│ Input: {input_str}" + " " * (input_box_width - 8 - len(input_str)) + "│", curses.color_pair(2))
        stdscr.addstr(5, 4, f"│ Result: {result}" + " " * (input_box_width - 9 - len(result)) + "│", curses.color_pair(2))
        stdscr.addstr(6, 4, "╰" + "━" * input_box_width + "╯", curses.color_pair(2))

        # Draw buttons
        for i, button in enumerate(buttons):
            button.draw(stdscr, i == current_selection, max_y, max_x)

        stdscr.refresh()

        try:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_selection >= 4:
                current_selection -= 4
            elif key == curses.KEY_DOWN and current_selection < len(buttons) - 4:
                current_selection += 4
            elif key == curses.KEY_LEFT and current_selection % 4 > 0:
                current_selection -= 1
            elif key == curses.KEY_RIGHT and current_selection % 4 < 3:
                current_selection += 1
            elif key == ord('\n'):
                button = buttons[current_selection]
                if button.label == 'Quit':
                    break
                elif button.label == 'C':
                    input_str = ''
                    result = ''
                elif button.label == '=':
                    try:
                        # 在计算前确保输入字符串是合法的
                        if input_str.count('(') > input_str.count(')'):
                            input_str += ')'
                        # 使用 add_math_prefix 函数处理输入字符串
                        input_str = add_math_prefix(input_str)
                        result = str(eval(input_str))
                        input_str = ''
                    except Exception as e:
                        result = f"Error: {str(e)}"
                elif button.label in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
                    if not input_str.endswith('math.'):
                        input_str += f"{button.label}("
                elif button.label == 'pi':
                    input_str += 'math.pi'
                else:
                    input_str += button.label
        except curses.error:
            pass

class CalculatorTests(unittest.TestCase):
    def test_button_init(self):
        with unittest.mock.patch('curses.initscr'):
            button = Button("Test", curses.color_pair(1))
            self.assertEqual(button.label, "Test")
            self.assertEqual(button.x, 0)
            self.assertEqual(button.y, 0)

    def test_basic_calculation(self):
        # Simulate calculations
        self.assertEqual(eval("2+2"), 4)
        self.assertEqual(eval("3*4"), 12)
        self.assertEqual(eval("10/2"), 5)
        self.assertEqual(eval("5-3"), 2)

    def test_complex_calculation(self):
        self.assertEqual(eval("2+3*4"), 14)
        self.assertAlmostEqual(eval("math.sin(math.pi/2)"), 1.0)
        self.assertAlmostEqual(eval("math.exp(1)"), math.e)

if __name__ == "__main__":
    curses.wrapper(calculator)
