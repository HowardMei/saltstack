git branch -r -d origin/0.11
git branch -r -d origin/0.12
git branch -r -d origin/0.13
git branch -r -d origin/0.14
git branch -r -d origin/0.15
git branch -r -d origin/0.16
git branch -r -d origin/0.17
git branch -r -d origin/2014.1
git branch -r -d origin/2014.7
git branch -r -d origin/no_ipv6
git branch -r -d origin/pillar_mod
git branch -r -d origin/remove_old_style
git branch -r -d origin/revert-18148-six_docs_build
git branch -r -d origin/revert-18643-develop
git branch -r -d origin/revert-18687-develop
git branch -r -d origin/revert-18792-issue17963
git branch -r -d origin/revert-19318-develop
git branch -r -d origin/revert-19423-fix_blockdev_test
git branch -r -d origin/revert-19571-hotfix/setup-salt-paths
git branch -r -d origin/seegno-enhancement/file-source-hash-doc
git push origin --delete 0.11 0.12 0.13 0.14 0.15 0.16 0.17 2014.1 2014.7 no_ipv6 pillar_mod remove_old_style revert-18148-six_docs_build \
revert-18643-develop revert-18687-develop revert-18792-issue17963 revert-19318-develop revert-19423-fix_blockdev_test \
revert-19571-hotfix/setup-salt-paths seegno-enhancement/file-source-hash-doc
git branch -r -d upstream/0.11
git branch -r -d upstream/0.12
git branch -r -d upstream/0.13
git branch -r -d upstream/0.14
git branch -r -d upstream/0.15
git branch -r -d upstream/0.16
git branch -r -d upstream/0.17
git branch -r -d upstream/2014.1
git branch -r -d upstream/2014.7
git branch -r -d upstream/no_ipv6
git branch -r -d upstream/pillar_mod
git branch -r -d upstream/remove_old_style
git branch -r -d upstream/revert-18148-six_docs_build
git branch -r -d upstream/revert-18643-develop
git branch -r -d upstream/revert-18687-develop
git branch -r -d upstream/revert-18792-issue17963
git branch -r -d upstream/revert-19318-develop
git branch -r -d upstream/revert-19423-fix_blockdev_test
git branch -r -d upstream/revert-19571-hotfix/setup-salt-paths
git branch -r -d upstream/seegno-enhancement/file-source-hash-doc
git push --all --force origin -u
