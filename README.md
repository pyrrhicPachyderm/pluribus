# Pluribus

> **_NOTE:_**
> Pluribus is a work in progress.
> The following documents its intended aims, features, and usage, serving as a to-do list and specification as much as anything else.

Pluribus is a utility to help create multi-volume books in LaTeX.
It generates the volumes in separate PDF files, and as an omnibus edition.
Furthermore, it can generate pluribuses&mdash;editions containing any subset of volumes you select.
It manages contents tables and indices within every volume and edition.
Lastly, by leveraging [`zref-xr`](https://ctan.org/pkg/zref), Pluribus facilitates references and hyperlinks within and between volumes.

## Using Pluribus

Pluribus consists of a script that generates a Makefile, which in turn can be used to compile your book's volumes, omnibus, and pluribuses.
By default, it generates a standalone Makefile.
However, it may be configured to generate a set of rules that can be incorporated into a project's overarching Makefile.
