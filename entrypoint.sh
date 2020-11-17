file_path=`pwd`
command="python3 ${file_path}/paperhunt.py $@"

echo "Setting up requirements to use paperhunt"
pip3 install -qr requirements.txt

alias paperhunt=$command
echo "paperhunt is ready to use"
