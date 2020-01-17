# Pluribus

Pluribus is a utility to help create multi-volume books in LaTeX.
It generates the volumes in separate PDF files, and as an omnibus edition.
Furthermore, it can generate pluribuses&mdash;editions containing any subset of volumes you select.
Lastly, by leveraging [zref-xr](https://ctan.org/pkg/zref), Pluribus facilitates references and hyperlinks within and between volumes.

Pluribus uses the build automation tool Make.
It can be easily incorporated into a project's overarching Makefile, or made to stand alone.
