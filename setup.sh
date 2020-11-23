rm -rf  dist/*.gz
rm -rf  dist/*.whl
rm -rf  build/*
rm -rf  wkstock.egg-info/*
python3 setup.py sdist bdist_wheel