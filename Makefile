PIP := pip3
PACKAGE_NAME := pluribus

install:
	$(PIP) install .

uninstall:
	$(PIP) uninstall -y $(PACKAGE_NAME)

.PHONY: install uninstall
