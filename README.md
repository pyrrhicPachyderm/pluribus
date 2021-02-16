# Pluribus

> **_NOTE:_**
> Pluribus is a work in progress.
> The following documents its intended aims, features, and usage, serving as a to-do list and specification as much as anything else.

Pluribus is a utility to help create multi-volume books in LaTeX.
It generates the volumes in separate PDF files, and as an omnibus edition.
Furthermore, it can generate pluribuses: editions containing any subset of volumes you select.
It manages the front and back matter, including the table of contents and index, within each volume and edition.
Lastly, by leveraging [`zref-xr`](https://ctan.org/pkg/zref), Pluribus facilitates references and hyperlinks within and between volumes.

## Installing Pluribus

To install Pluribus, clone this repository, `cd` into it, then run `sudo make install`.

To uninstall it, run `sudo make uninstall`.

## Using Pluribus

Pluribus is run to generate a Makefile, which in turn can be used with GNU make to compile your book's volumes, omnibus, and pluribuses.
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
The path to the configuration file must be provided as an argument to Pluribus when it is run.

Pluribus creates its own `.pluribus/` directory; by default, this lies alongside the created Makefile.
This directory, as well the Makefile generated by Pluribus, should be excluded from a project's version control system (for example, with a `.gitignore` file).
