# Cliclok
## Command line clocking

As of v0.0.1, cliclock features a stopwatcher (based on [chapter
15](https://automatetheboringstuff.com/chapter15/), of the great
[ATBS](http://automatetheboringstuff.com/)) and a timer. More coming.

## Concept

Cliclock helps you track how long time you use in a task, but it doesn't track
you (stopwatcher). It should interrupt your workflow to let you know that the
span of time you provided is gone (timer). Interruptions any kind of alarm or
clue should be as abrupt or as subtle as the user needs.

## Prerequisites

* Python 3.\* 

It was written in python 3.6.3 and Linux, but should "just work" in any system
with python 3.\*. Or else, open an issue. o/

## Installation

Clone the repository, or just grab the `cliclock.py` file.

## Usage

Call the script passing the desired command.

| Command | Usage | Description |
|---------|-------|-------------|
|`stopw`  | `$ python cliclock.py stopw` | Run a stopwatch. |
|`timer`  | `$ python cliclock.py timer 2` | Run a timer that will expire in two minutes. |

### Stopwatch

The stopwatch will keep track of each loop. Press `enter` to finish one and
start another, press `ctrl-c` to stop it.

### Timer

When using the `timer` command, provide an amount of minutes. As of this initial
version, it will open your default browser and - in a new tab (if possible) - 
`www.duckduckgo.com` when the time is over.

## Bugs, issues and contributions

..., feedback and criticisms are welcome. Just shoot! (:

## TODO

- [X] Add Readme
- [X] v0.0.1
- [ ] Add tests
- [ ] Refactoring
- [ ] v0.0.2
- [ ] Add config file support
- [ ] v0.0.3
- [ ] Add different actions to when timer stops
- [ ] v0.0.4
- [ ] Stopw custom loops
- [ ] v0.0.5

## License
### The Unlicense

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
