PIP := pip3
PACKAGE_NAME := pluribus

install: install_docs
	$(PIP) install .

uninstall: uninstall_docs
	$(PIP) uninstall -y $(PACKAGE_NAME)

.PHONY: install uninstall

install_docs: docs/pluribus.1 docs/pluribus-config.5
	@#It may be that the destination directory does not exist.
	@#So ensure it is created with mkdir first.
	mkdir -p /usr/local/share/man/man1/ && cp docs/pluribus.1 /usr/local/share/man/man1/
	mkdir -p /usr/local/share/man/man5/ && cp docs/pluribus-config.5 /usr/local/share/man/man5/
	mandb

uninstall_docs:
	rm -f /usr/local/share/man/man1/pluribus.1
	rm -f /usr/local/share/man/man5/pluribus-config.5
	mandb

.PHONY: install_docs uninstall_docs

#The double colon makes this a terminal match-anything rule.
#Make will consider it only if the prerequisite already exists.
%:: %.ronn
	ronn --roff $<

clean:
	@#Delete everything in the docs folder except the original ronn files and index.txt.
	find docs/ -type f ! -name "*.ronn" ! -name "index.txt" -exec rm -f {} +

.PHONY: clean
