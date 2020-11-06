Creating a mobile_modem_exporter release
========================================

Tag, build and upload the new release
-------------------------------------
- First, update the version numbers in needed files:
    sed -i'' "s/0.1.0-dev/0.1.0/g" setup.py mobile_modem_exporter/mobile_modem_exporter.py docs/conf.py docs/usage.rst
- Then update release date in docs/changelog.rst.

Commit the above changes and push.

- Then tag the new release:
    git tag v0.1.0 -a -m "Release v0.1.0"
    git push origin v0.1.0

- Finally upload new release to pypi:
    python setup.py sdist
    twine upload dist/mobile_modem_exporter-0.1.0.tar.gz

Back to development
-------------------
- Bump version and add -dev to version numbers everywhere.
    sed -i'' "s/0.1.0/0.1.0-dev/g" setup.py mobile_modem_exporter/mobile_modem_exporter.py docs/conf.py docs/usage.rst
- Update changelog

Commit the above changes and push.

