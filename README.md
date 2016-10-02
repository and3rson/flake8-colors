# flake8-colors
ANSI colors highlight for Flake8

## Installation

1. Install plugin:

    ```
    pip install flake8-colors
    ```

2. Use the following example format in your `.flake8` file:

    ```
    format = ${cyan}%(path)s${reset}:${yellow_bold}%(row)d${reset}:${green_bold}%(col)d${reset}: ${red_bold}%(code)s${reset} %(text)s
    ```

3. Enjoy!

  ![Example image](https://habrastorage.org/files/0a7/cf5/47c/0a7cf547cd03457385c23691a4f29869.png)
  
## Usage

There are three forms of tags:

  - ${COLOR}
  - ${COLOR_MODIFIER}
  - ${TAG}

Colors:

  - black
  - red
  - green
  - yellow
  - blue
  - purple
  - cyan
  - white
  
Modifiers:

  - fg
  - bold
  - underline
  - bg

Tags:

  - bold
  - underline
  - reset

# Credits

Inspired by [flake8-format-ansi](https://github.com/jayvdb/flake8-format-ansi/)

# Contribution

Just do whatever you want to do.
