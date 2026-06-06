# Домашние задания по дисциплине «Алгоритмы и структуры данных»

## Состояние

- [![Lint & Typecheck](../../actions/workflows/lint-typecheck.yml/badge.svg)](../../actions/workflows/lint-typecheck.yml) — статический анализ
- [![Tests](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml) — тесты 

## Задания

### [00.Demo](00.Demo)

Шаблонное задание с модульными и интеграционными тестами.

### 01.InplaceSorting

- [01.InplaceSorting.c](01.InplaceSorting.c) посложнее
- [01.InplaceSorting.s](01.InplaceSorting.s) попроще

Сортировка на месте.

1. Разобраться, что там уже есть, что как и почему.
2. Реализовать не менее одного алгоритма сортировки за $O(N^2)$ и не менее одного за $O(N log N)$.
3. Добавить их запуск на массивах разной длины в качестве интеграционного теста.
4. Добавить юниттесты для них.

### [02.Base85](02.Base85)

1. Реализовать кодер и декодер.
2. Добавить юниттесты для разной длины разных строк, да попопдлее!

### ... Добавляйте следующие аналогично...

## Что рекомендуется установить

1. Разумеется, Git.
2. Linux. С ним легче пойдёт.
3. [uv](https://docs.astral.sh/uv/getting-started/installation/), и выполнить:
   - `$ uv venv`
   - `$ uv pip install -e .`
4. Visual Studio Code
   - [плагин для Python](https://open-vsx.org/extension/ms-python/python)
   - [плагин для uv](https://open-vsx.org/extension/the0807/uv-toolkit)
