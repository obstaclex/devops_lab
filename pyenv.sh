# Install development-tools RedHat/CentOS
sudo yum install @development zlib-devel bzip2 bzip2-devel readline-devel sqlite \
    sqlite-devel openssl-devel xz xz-devel libffi-devel findutils -y

# Change homedir and install pyenv
username="${obstaclex}"

if [ -z $username ]; then
    sudo su root
else
    sudo su $username
fi
cd ~ && curl https://pyenv.run | bash

cat <<EOF | tee -a ~/.bash_profile
export PATH="~/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF
source .bash_profile

# Install required versions
versions=("3.7.8" "2.7.18")
for x in ${versions[@]}; do
    pyenv install $x
done

# Create virtualenv
pyenv virtualenv ${versions[0]} project_1
pyenv virtualenv ${versions[1]} project_2
