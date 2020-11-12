python3 -m pip install setuptools
python3 -m pip install requests
git config --global user.email "no-reply@kamakepar.ru"
git config --global user.name "Server Transformer"
git add *
git commit -m "Upload"
git push
python3 main.py
