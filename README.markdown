# Auto Encoding for Ruby

I hate the need to include #encoding: utf-8 on every Ruby file with non-ASCII characters. So I've created this plugin to save me from this boring task. It automatically adds an encoding declaration on the top of Ruby files when needed, and remove it when it's not necessary anymore. Simple as that.

## Installation

You have 2 options for installing Auto Encoding for Ruby: with or without Git.

### With Git

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X:

    ```shell
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ```

* Linux:

    ```shell
    cd ~/.Sublime\ Text 2/Packages/
    ```

* Windows:

    ```shell
    cd %APPDATA%/Sublime Text 2/Packages/
    ```

After this, you just need to clone this repository:

```shell
git clone git://github.com/lee-dohm/auto-encoding-for-ruby.git "Auto Encoding for Ruby"
```

### Without Git

Click on the nice cloud icon above, and download the zip file containing this plugin. Then unzip the file and move the resulting folder to your Packages directory.

## How to Use

Auto Encoding for Ruby will add a `# encoding: UTF-8` declaration on top of Ruby files on these situations:

* Just after you type the first non-ASCII character of the file;
* When you open a file with non-ASCII characters and no encoding declaration.

It will also remove the encoding declaration on the following cases:

* Just after you delete the last non-ASCII character;
* When you open a file with an encoding declaration but without non-ASCII characters.

In other words, just write your code as you would without the plugin and you'll be fine.

### Changing the Encoding Declaration Format

The format of the encoding declaration is configurable to any Ruby-allowable declaration.  Simply edit the `Auto Encoding For Ruby.sublime-settings` file in your User settings folder to be the declaration you prefer.

# Information

Source: https://github.com/lee-dohm/auto-encoding-for-ruby

Authors: [Elomar Nascimento dos Santos](https://github.com/elomarns), [Lee Dohm](https://github.com/lee-dohm)
