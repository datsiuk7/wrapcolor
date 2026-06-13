# wrapcolor

🇺🇸 [English](#english) | 🇺🇦 [Українська](#українська)

---

<a name="english"></a>
## English

A universal ANSI-colorizer for Python: an extremely simple and convenient way to style text in the console.
Supports 8/16 base colors, 256-color palette (xterm), and TrueColor (RGB), as well as font styles.

- Lightweight and dependency-free (optional: `colorama` for Windows)
- Convenient `color` instance with ready-to-use codes and utilities
- Works with any library that outputs to the terminal (logging, click, argparse, etc.)

### Installation

```bash
pip install wrapcolor
# (optional for Windows console/PowerShell)
pip install colorama
```

If you are on Windows, it is recommended to initialize colorama at startup:

```python
try:
    from colorama import justFixWindowsConsole
    justFixWindowsConsole()
except Exception:
    pass
```

### Quick Start

```python
from wrapcolor import color

print(color.paint("Hello!", fg="red", styles=["bold"]))
print(color.rgb(255, 100, 0) + "TrueColor text" + color.reset)
print(color.bg_idx(24) + "256-color background" + color.reset)
```

### Usage Examples

#### 1) Base text colors
```python
from wrapcolor import color

print(color.red + "Red" + color.reset)
print(color.green + "Green" + color.reset)
print(color.bright_blue + "Bright blue" + color.reset)
```

#### 2) Background colors
```python
from wrapcolor import color

print(color.bg_yellow + color.black + "Black on yellow" + color.reset)
print(color.bg_bright_red + color.white + "White on bright red" + color.reset)
```

#### 3) Font styles
```python
from wrapcolor import color

print(color.bold + "Bold" + color.reset)
print(color.italic + "Italic" + color.reset)
print(color.underline + "Underline" + color.reset)
print(color.inverse + "Inverse" + color.reset)
print(color.strike + "Strikethrough" + color.reset)
```

#### 4) Combining styles and colors
```python
from wrapcolor import color

print(color.red + color.bold + "Red bold" + color.reset)
print(color.bright_green + color.underline + "Green underline" + color.reset)
```

#### 5) Convenient paint()
```python
from wrapcolor import color

print(color.paint("OK", fg="green", styles=["bold"]))
print(color.paint("WARNING", fg="bright_yellow", bg="bg_black", styles=["underline"]))
print(color.paint("ERROR", fg="bright_white", bg="bg_red", styles=["bold"]))
```

Advantage of `paint()` — it automatically adds `reset` at the end.

#### 6) wrap() template for reusable formatting
```python
from wrapcolor import color

warn = color.wrap(color.bright_yellow + color.bold)
err  = color.wrap(color.bg_red + color.white + color.bold)

print(warn.format("Warning message"))
print(err.format("Error message"))
```

#### 7) 256-colors (xterm)
```python
from wrapcolor import color

for i in range(16, 32):
    print(color.idx(i) + f" idx({i}) " + color.reset, end=" ")
print()

for i in [196, 202, 208, 214, 220, 226]:
    print(color.idx(i) + "●" + color.reset, end=" ")
print()

print(color.bg_idx(24) + color.bright_white + "Text on idx(24) background" + color.reset)
```

#### 8) TrueColor (RGB)
```python
from wrapcolor import color

print(color.rgb(12, 200, 155) + "RGB foreground" + color.reset)
print(color.bg_rgb(20, 20, 20) + color.bright_cyan + "Bright on dark background" + color.reset)
```

#### 9) Helper functions for statuses
```python
from wrapcolor import color

def ok(msg):
    return color.paint(msg, fg="green", styles=["bold"])

def warn(msg):
    return color.paint(msg, fg="bright_yellow")

def err(msg):
    return color.paint(msg, fg="bright_white", bg="bg_red", styles=["bold"]) 

print(ok("Done"))
print(warn("Warning"))
print(err("Failure"))
```

#### 10) Integration with logging
```python
import logging
from wrapcolor import color

class ColorFormatter(logging.Formatter):
    LEVEL_COLOR = {
        logging.DEBUG: color.dim,
        logging.INFO: color.bright_green,
        logging.WARNING: color.bright_yellow,
        logging.ERROR: color.bright_red,
        logging.CRITICAL: color.bg_red + color.white + color.bold,
    }
    def format(self, record):
        base = super().format(record)
        code = self.LEVEL_COLOR.get(record.levelno, "")
        return f"{code}{base}{color.reset}" if code else base

h = logging.StreamHandler()
fmt = ColorFormatter("%(levelname)s: %(message)s")
h.setFormatter(fmt)
log = logging.getLogger("demo")
log.addHandler(h)
log.setLevel(logging.DEBUG)

log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")
```

#### 11) Respect NO_COLOR and TTY
```python
import os, sys
from wrapcolor import color as _color

USE_COLOR = sys.stdout.isatty() and os.getenv("NO_COLOR") is None

class _NoColor:
    reset = ""
    bold = dim = italic = underline = inverse = strike = ""
    black = red = green = yellow = blue = magenta = cyan = white = ""
    bright_black = bright_red = bright_green = bright_yellow = ""
    bright_blue = bright_magenta = bright_cyan = bright_white = ""
    bg_black = bg_red = bg_green = bg_yellow = bg_blue = bg_magenta = bg_cyan = bg_white = ""
    bg_bright_black = bg_bright_red = bg_bright_green = bg_bright_yellow = ""
    bg_bright_blue = bg_bright_magenta = bg_bright_cyan = bg_bright_white = ""
    @staticmethod
    def idx(n): return ""
    @staticmethod
    def bg_idx(n): return ""
    @staticmethod
    def rgb(r,g,b): return ""
    @staticmethod
    def bg_rgb(r,g,b): return ""
    @classmethod
    def paint(cls, text, *, fg=None, bg=None, styles=None): return str(text)
    @classmethod
    def wrap(cls, code): return "{}"

color = _color if USE_COLOR else _NoColor()

print(color.paint("This works even without colors", fg="green"))
```

#### 12) Tips and nuances
- If you combine codes manually, don't forget to add `color.reset` at the end.
- `paint()` and `wrap()` automatically append `reset`, making them convenient for safe formatting.
- Not all terminals support 256/TrueColor — on older systems, colors may be downgraded.

### API Reference (Short)

Objects and methods are available via:
```python
from wrapcolor import color, _Color
```

- Style attributes: `bold`, `dim`, `italic`, `underline`, `inverse`, `strike`
- 8 foreground colors: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- Bright variants: `bright_black` .. `bright_white`
- Backgrounds: `bg_black` .. `bg_white`, `bg_bright_black` .. `bg_bright_white`
- Methods:
  - `idx(n: int) -> str` — 256-colors (0..255) foreground
  - `bg_idx(n: int) -> str` — 256-colors (0..255) background
  - `rgb(r,g,b) -> str` — TrueColor (0..255) foreground
  - `bg_rgb(r,g,b) -> str` — TrueColor (0..255) background
  - `paint(text, *, fg=None, bg=None, styles=None) -> str` — safely wraps text and adds reset
  - `wrap(code: str) -> str` — returns a `"{code}{}\x1b[0m"` template for reusable `format()`

### Compatibility
- Python 3.10+
- Linux/macOS/Windows (colorama recommended for Windows)

### Why wrapcolor?
- Minimalistic interface: use properties or utilities.
- Imposes no dependencies.
- Works well with existing libraries.

### License
MIT

### Contributing
Issues/PRs are welcome.

---

<a name="українська"></a>
## Українська

Універсальний ANSI-«кольоризатор» для Python: надзвичайно простий та зручний спосіб стилізувати текст у консолі.
Підтримує 8/16 базових кольорів, 256‑кольорову палітру (xterm) та TrueColor (RGB), а також стилі шрифту.

- Легкий і без залежностей (опційно: `colorama` для Windows)
- Зручний екземпляр `color` із готовими кодами та утилітами
- Працює з будь‑якою бібліотекою, що виводить у термінал (`logging`, `click`, `argparse` тощо)

### Встановлення

```bash
pip install wrapcolor
# (опційно для Windows консоль/PowerShell)
pip install colorama
```

Якщо ви на Windows, рекомендовано ініціалізувати colorama на старті:

```python
try:
    from colorama import justFixWindowsConsole
    justFixWindowsConsole()
except Exception:
    pass
```

### Швидкий старт

```python
from wrapcolor import color

print(color.paint("Привіт!", fg="red", styles=["bold"]))
print(color.rgb(255, 100, 0) + "TrueColor текст" + color.reset)
print(color.bg_idx(24) + "Фон 256‑кольорів" + color.reset)
```

### Приклади використання

#### 1) Базові кольори тексту
```python
from wrapcolor import color

print(color.red + "Червоний" + color.reset)
print(color.green + "Зелений" + color.reset)
print(color.bright_blue + "Яскраво‑синій" + color.reset)
```

#### 2) Кольори фону
```python
from wrapcolor import color

print(color.bg_yellow + color.black + "Чорний на жовтому" + color.reset)
print(color.bg_bright_red + color.white + "Білий на яскраво‑червоному" + color.reset)
```

#### 3) Стилі шрифту
```python
from wrapcolor import color

print(color.bold + "Жирний" + color.reset)
print(color.italic + "Курсив" + color.reset)
print(color.underline + "Підкреслений" + color.reset)
print(color.inverse + "Інверсія" + color.reset)
print(color.strike + "Закреслений" + color.reset)
```

#### 4) Комбінування стилів і кольорів
```python
from wrapcolor import color

print(color.red + color.bold + "Червоний жирний" + color.reset)
print(color.bright_green + color.underline + "Зелений підкреслений" + color.reset)
```

#### 5) Зручний paint()
```python
from wrapcolor import color

print(color.paint("OK", fg="green", styles=["bold"]))
print(color.paint("УВАГА", fg="bright_yellow", bg="bg_black", styles=["underline"]))
print(color.paint("ПОМИЛКА", fg="bright_white", bg="bg_red", styles=["bold"]))
```

Перевага `paint()` — воно автоматично додає `reset` наприкінці.

#### 6) Шаблон wrap() для багаторазового використання
```python
from wrapcolor import color

warn = color.wrap(color.bright_yellow + color.bold)
err  = color.wrap(color.bg_red + color.white + color.bold)

print(warn.format("Попередження"))
print(err.format("Помилка"))
```

#### 7) 256‑кольорів (xterm)
```python
from wrapcolor import color

for i in range(16, 32):
    print(color.idx(i) + f" idx({i}) " + color.reset, end=" ")
print()

for i in [196, 202, 208, 214, 220, 226]:
    print(color.idx(i) + "●" + color.reset, end=" ")
print()

print(color.bg_idx(24) + color.bright_white + "Текст на фоні idx(24)" + color.reset)
```

#### 8) TrueColor (RGB)
```python
from wrapcolor import color

print(color.rgb(12, 200, 155) + "RGB передній план" + color.reset)
print(color.bg_rgb(20, 20, 20) + color.bright_cyan + "Яскравий на темному" + color.reset)
```

#### 9) Допоміжні функції для статусів
```python
from wrapcolor import color

def ok(msg):
    return color.paint(msg, fg="green", styles=["bold"])

def warn(msg):
    return color.paint(msg, fg="bright_yellow")

def err(msg):
    return color.paint(msg, fg="bright_white", bg="bg_red", styles=["bold"]) 

print(ok("Готово"))
print(warn("Увага"))
print(err("Збій"))
```

#### 10) Інтеграція з logging
```python
import logging
from wrapcolor import color

class ColorFormatter(logging.Formatter):
    LEVEL_COLOR = {
        logging.DEBUG: color.dim,
        logging.INFO: color.bright_green,
        logging.WARNING: color.bright_yellow,
        logging.ERROR: color.bright_red,
        logging.CRITICAL: color.bg_red + color.white + color.bold,
    }
    def format(self, record):
        base = super().format(record)
        code = self.LEVEL_COLOR.get(record.levelno, "")
        return f"{code}{base}{color.reset}" if code else base

h = logging.StreamHandler()
fmt = ColorFormatter("%(levelname)s: %(message)s")
h.setFormatter(fmt)
log = logging.getLogger("demo")
log.addHandler(h)
log.setLevel(logging.DEBUG)

log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")
```

#### 11) Поважайте NO_COLOR і TTY
```python
import os, sys
from wrapcolor import color as _color

USE_COLOR = sys.stdout.isatty() and os.getenv("NO_COLOR") is None

class _NoColor:
    reset = ""
    bold = dim = italic = underline = inverse = strike = ""
    black = red = green = yellow = blue = magenta = cyan = white = ""
    bright_black = bright_red = bright_green = bright_yellow = ""
    bright_blue = bright_magenta = bright_cyan = bright_white = ""
    bg_black = bg_red = bg_green = bg_yellow = bg_blue = bg_magenta = bg_cyan = bg_white = ""
    bg_bright_black = bg_bright_red = bg_bright_green = bg_bright_yellow = ""
    bg_bright_blue = bg_bright_magenta = bg_bright_cyan = bg_bright_white = ""
    @staticmethod
    def idx(n): return ""
    @staticmethod
    def bg_idx(n): return ""
    @staticmethod
    def rgb(r,g,b): return ""
    @staticmethod
    def bg_rgb(r,g,b): return ""
    @classmethod
    def paint(cls, text, *, fg=None, bg=None, styles=None): return str(text)
    @classmethod
    def wrap(cls, code): return "{}"

color = _color if USE_COLOR else _NoColor()

print(color.paint("Це працює навіть без кольорів", fg="green"))
```

#### 12) Підказки та нюанси
- Якщо поєднуєте коди вручну, не забудьте в кінці додати `color.reset`.
- `paint()` та `wrap()` самі додають `reset`, що зручно для безпечного форматування.
- Не всі термінали підтримують 256/TrueColor — на старих системах кольори можуть знижуватись.

### Довідка API (скорочено)

Об’єкти й методи доступні з:
```python
from wrapcolor import color, _Color
```

- Атрибути стилів: `bold`, `dim`, `italic`, `underline`, `inverse`, `strike`
- 8 кольорів переднього плану: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- Яскраві варіанти: `bright_black` .. `bright_white`
- Фон: `bg_black` .. `bg_white`, `bg_bright_black` .. `bg_bright_white`
- Методи:
  - `idx(n: int) -> str` — 256‑кольорів (0..255), передній план
  - `bg_idx(n: int) -> str` — 256‑кольорів (0..255), фон
  - `rgb(r,g,b) -> str` — TrueColor (0..255) передній план
  - `bg_rgb(r,g,b) -> str` — TrueColor (0..255) фон
  - `paint(text, *, fg=None, bg=None, styles=None) -> str` — безпечно обгортає текст і додає `reset`
  - `wrap(code: str) -> str` — повертає шаблон `"{code}{}\x1b[0m"` для багаторазового `format()`

### Сумісність
- Python 3.10+
- Linux/macOS/Windows (для Windows бажано `colorama`)

### Чому wrapcolor?
- Мінімалістичний інтерфейс: використовуй властивості або утиліти
- Не нав’язує залежностей
- Добре працює з існуючими бібліотеками

### Ліцензія
MIT

### Внесок
Issue/PR вітаються.