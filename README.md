# Презентація з неперервних розподілів

Вихідний код презентації з теми "Основні неперервні розподіли" для дисципліни "Теорія ймовірності та математична статистика"

Підготував Суботін Ігор, МПІ-241

Репозиторій побудований на основі [manim-revealjs-example](https://github.com/Elteoremadebeethoven/manim-revealjs-example/).
Сам проект використовує бібліотеку візуалізації [Manim](https://github.com/ManimCommunity/manim), створену ютубером [3Blue1Brown](https://www.youtube.com/@3blue1brown) для своїх відео. Вигляд презентації надає фреймворк [reveal.js](https://github.com/hakimel/reveal.js) в поєднанні з плагіном [manim-revealjs](https://github.com/RickDW/manim-revealjs).

## Встановлення
Для істалювання встановіть залежності python 3. 
```
pip install -r requirements.txt
```
Також можливо необхідно встановити [FFmpeg](https://ffmpeg.org/download.html#build-windows) та [TinyTeX](https://yihui.org/tinytex/). Більш детально про встановлення manim [в офіційній документації](https://docs.manim.community/en/stable/installation/windows.html)

## Запуск
Для запуску відкрийте файл starter.bat, який відрендерить всі відео та запустить простий веб-сервер на python
Дивний факт про роботу відео, що браузери основані на Chromium потребують заголовку accept-ranges:bytes для корректного відображення слайдів, саме тому тут використовуєсться [трохи покращений веб-сервер](https://github.com/danvk/RangeHTTPServer).