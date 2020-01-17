# Pluribus

> **_NOTE:_**
> Pluribus is a work in progress.
> The following documents its intended aims, features, and usage, serving as a to-do list and specification as much as anything else.

Pluribus is a utility to help create multi-volume books in LaTeX.
It generates the volumes in separate PDF files, and as an omnibus edition.
Furthermore, it can generate pluribuses&mdash;editions containing any subset of volumes you select.
It manages contents tables and indices within every volume and edition.
Lastly, by leveraging [zref-xr](https://ctan.org/pkg/zref), Pluribus facilitates references and hyperlinks within and between volumes.

Pluribus uses the build automation tool Make.
It can be easily incorporated into a project's overarching Makefile, or made to stand alone.
