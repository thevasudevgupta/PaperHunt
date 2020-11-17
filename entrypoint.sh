file_path=`pwd`
command="python3 ${file_path}/paperhunt.py $@"

echo "Setting up requirements to use paperhunt"
pip3 install -qr requirements.txt

python -m spacy download en_core_web_md

alias paperhunt=$command
echo "paperhunt is ready to use"
