# Houdini Themes

A collection of themes for Houdini created using a templating system to generate
color scheme configs from theme JSON files.

## Installation

To install copy the configs from the `config` directory to the config directory
in the Houdini Preferences location: `~\houdini\houdini21.0\config`

To set a monospace font, copy `source/resources` to that same location.

## Previews

These are some of the themes that are included in the package.

<details>
<summary>One Dark Two</summary>

![One Dark Two](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/one_dark_two.png)

</details>

<details>
<summary>Monokai</summary>

<https://monokai.pro>

![Monokai](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/monokai.png)

</details>

<details>
<summary>Nord</summary>

<https://nordtheme.com>

![Nord](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/nord.png)

</details>

<details>
<summary>Catppuccin</summary>

<https://catppuccin.com>

![Catppuccin Frappe](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/catppuccin_frappe.png)

![Catppuccin Macchiato](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/catppuccin_macchiato.png)

![Catppuccin Mocha](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/catppuccin_mocha.png)

</details>

<details>
<summary>Atom One</summary>

<https://atom.io>

![Atom One](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/atom_one.png)

</details>

<details>
<summary>GitHub</summary>

<https://github.com>

![GitHub Dark](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/github_dark.png)

</details>

<details>
<summary>Dracula</summary>

<https://draculatheme.com/>

![Dracula](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/dracula.png)

</details>

<details>
<summary>Blender</summary>

<https://blender.org>

![Blender](https://raw.githubusercontent.com/beatreichenbach/houdini-themes/refs/heads/main/.github/assets/blender.png)

</details>

## Create Configs

Create a venv:
```shell
python -m venv venv
```

Install dependencies (Windows):
```shell
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Install dependencies (Linux):
```shell
. venv\bin\activate
python -m pip install -r requirements.txt
```

Create configs to the output directory:
```shell
python theme.py
```

Create configs directly to the houdini directory:
```shell
python theme.py "~\houdini\houdini21.0\config"
```

## License

MIT License. Copyright 2024 - Beat Reichenbach.
See the [License file](LICENSE) for details.