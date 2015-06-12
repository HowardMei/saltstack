./getupstream.sh
set -ex
echo "upstream_develop =+ develop -> release -> master"
git checkout upstream_develop || exit 1
git checkout develop && git rebase -Xours upstream_develop || exit 1
git checkout release && git rebase -Xours develop || exit 1
git checkout master && git merge --no-edit -Xtheirs release || exit 1
set +ex
echo "git push --all origin -u  to push all changes to remote"
