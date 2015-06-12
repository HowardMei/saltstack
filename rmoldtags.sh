git tag --delete $(git tag -l | awk '/^v0(.*)$/ {print $1}')
git ls-remote --tags origin | awk '/^(.*)v0(.*[0-9])$/ {print ":"$2}' | xargs git push origin
git tag --delete $(git tag -l | awk '/^v2014.*(.*)$/ {print $1}')
git ls-remote --tags origin | awk '/^(.*)v2014.*(.*[0-9])$/ {print ":"$2}' | xargs git push origin
git tag --delete $(git tag -l | awk '/^v2015.2(.*)$/ {print $1}')
git ls-remote --tags origin | awk '/^(.*)v2015.2(.*[0-9])*$/ {print ":"$2}' | xargs git push origin
git push --tags --force origin -u
