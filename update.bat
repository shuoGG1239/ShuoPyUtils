python setup.py bdist_wheel
pip uninstall shuogg
pip install ./dist/shuogg-0.1-py3-none-any.whl
rmdir /s/q build
rmdir /s/q shuogg.egg-info