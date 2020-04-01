# svntemplr
make SVN commit-msg template use to svn-commit.tmp

Edit ~/.bashrc

~~~ bash
export SVN_EDITOR="python $HOME/svntemplr/templete-with-svn.py $HOME/svntemplr/commit-template svn-commit.tmp && vim svn-commit.tmp"
~~~
