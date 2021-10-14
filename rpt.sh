sudo su 

if [-f "/usr/bin/rstream" ]; then
echo 'Already Installed' 
elif [-f /usr/bin/git]; then 
git clone "https://github.com/Rupam027/":$2:".git" "/usr/bin"
else
apt install 



