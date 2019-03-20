cat <<EOF > ~/.pypirc
[distutils]
index-servers = local
[local]
repository: https://pillarproject.jfrog.io/pillarproject/api/pypi/pypi
username: $ARTIFACTORY_PUBLISHING_USER
password: $ARTIFACTORY_PUBLISHING_PASSWORD
EOF

echo "Created .pypirc file: Here it is: "
ls -la ~/.pypirc
