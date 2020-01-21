# Pluribus

> **_NOTE:_**
> Pluribus is a work in progress.
> The following documents its intended aims, features, and usage, serving as a to-do list and specification as much as anything else.

Pluribus is a utility to help create multi-volume books in LaTeX.
It generates the volumes in separate PDF files, and as an omnibus edition.
Furthermore, it can generate pluribuses&mdash;editions containing any subset of volumes you select.
It manages contents tables and indices within every volume and edition.
Lastly, by leveraging [`zref-xr`](https://ctan.org/pkg/zref), Pluribus facilitates references and hyperlinks within and between volumes.

## Installing Pluribus

To install Pluribus, clone this repository, `cd` into it, then run `make install`.

To uninstall it, run `make uninstall`.
It is installed using `pip3`, so you can also uninstall it using `pip3 uninstall pluribus`.

## Using Pluribus

Pluribus is run to generate a Makefile, which in turn can be used to compile your book's volumes, omnibus, and pluribuses.
By default, it generates a standalone Makefile.
However, it may be configured to generate a set of rules that can be incorporated into a project's overarching Makefile.

In order to use Pluribus, each volume should be written as a LaTeX file including only the main matter.
This is all the content that would be placed between LaTeX's `\mainmatter` and `\backmatter` commands.
The front matter and back matter are managed separately by Pluribus.
Each main matter file is loaded in LaTeX using the [`\import`](https://ctan.org/pkg/import) command.
As such, it may lie in any location on the file system, and can safely `\input`, `\include`, `\includegraphics`, or `\subimport` files relative to its own location.

Pluribus relies on a configuration file, in the [TOML](https://github.com/toml-lang/toml) format.
This can be used to modify the behaviour of Pluribus, such as selecting between a standalone and partial Makefile.
More importantly, however, the configuration file defines the volumes to be managed by Pluribus.
The path to the configuration file must be provided as an argument to Pluribus, when it is run.
The contents of configuration file are detailed [below](#user-content-the-configuration-file).

Pluribus creates its own `.pluribus/` directory; by default, this lies alongside the provided configuration file.
This directory, as well the Makefile generated by Pluribus, should be excluded from a project's version control system (for example, with a `.gitignore` file).

### Command Line Argument

Pluribus takes exactly one argument: the path to the configuration file.
Every path in the configuration file should be relative to the location of the configuration file itself.
As such, it does not matter where Pluribus is run from; only which config file is is run upon.
Additionally, by default, the `.pluribus/` directory and the resulting Makefile are created alongside the configuration file.

### The Configuration File

Pluribus' configuration file uses the [TOML](https://github.com/toml-lang/toml) format.
Note that this means you can use `#` to begin a comment within it.

Pluribus' configuration file can be divided into two parts.
The first consists of simple key-value pairs, separated by an `=` sign, that modify the overall behaviour of Pluribus.
These should be at the beginning of the file, entirely before the second part.
The list of available options is given [below](#user-content-configuration-options).

The second part details the various volumes to be managed by Pluribus.
The information about each volume begins with the tag for the volume, in square brackets.
For example `[the-first-volume]`.
Every subsequent key-value pair defines a property of that volume.
Some of these properties are mandatory, and must be included for every volume.
The list of properties is given [below](#user-content-volume-properties).

#### Volume Properties

Two of the volume properties are mandatory: `title` and `content`.
`title` is a string, used as the title for the volume, set using LaTeX's `\title` command.
`content` is also a string, used as a file path.
This file must be a `.tex` file, containing the main matter for the volume.

#### Reserved Volumes

Some volume tags are reserved by Pluribus: `all`, `omnibus`, and `pluribus`.
If these are used, these do not define new volumes.

##### Volume `all`

Any properties set in this volume are set for all other volumes, including `omnibus` and `pluribus`.
Any of these properties are overwritten for a given volume if they are set specifically in that volume's entry.

##### Volume `omnibus`

##### Volume `pluribus`

#### Configuration Options

The following configuration options are available.
These should be set above any of the volume definitions.
- [`makefile`](#user-content-makefile)
- [`makefile_standalone`](#user-content-makefile)
- [`documentclass` and `documentclass_options`](#user-content-documentclass-and-documentclass_options)
- [`disable_safety`](#user-content-disable_safety)

##### `makefile`
This string simply sets the path of the Makefile created by Pluribus, relative to the configuration file.
The default is `Makefile`.

##### `makefile_standalone`
This sets whether the Makefile created by Pluribus is intended to stand alone or not; whether it features an `all` rule.
It defaults to `true`.

##### `documentclass` and `documentclass_options`
These two strings are used for the first line of each LaTeX file:
```
\documentclass[<documentclass_options>]{<documentclass>}
```
For example, you might use:
```
documentclass = "memoir"
documentclass_options = "a4paper,10pt"
```
The defaults are:
```
documentclass = "book"
documentclass_options = ""
```

##### `disable_safety`
Pluribus ordinary refuses to overwrite a Makefile which was not itself created by Pluribus.
It inserts a comment in the first line of its own Makefiles to identify this.
Setting `disable_safety = true` overrides this behaviour, allowing Pluribus to overwrite manually created Makefiles.
