# svntemplr
make SVN commit-msg template use to svn-commit.tmp

Edit ~/.bashrc

~~~ bash
export SVN_EDITOR="python $HOME/eyedi-templete/templete-with-svn.py $HOME/eyedi-templete/commit-template svn-commit.tmp && vim svn-commit.tmp"
~~~
