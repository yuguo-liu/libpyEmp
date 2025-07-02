#!bin/bash
mkdir build
cd build
cmake ../src
make
cp pyEmp*.so ../pyEmp

cd ..

pip wheel . --wheel-dir=dist
pip install dist/pyemp-0.1.0-py3-none-any.whl