mkdir public
mkdir staticfiles_build
cd staticfiles_build
> file.txt
cd ../public
> file.txt
cd ../
python3 -m pip freeze
python3 start_frontend.py
