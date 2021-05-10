# svntemplr

SVN commit할 때 매번 비슷한 양식을 입력하는 것이 귀찮아서 만든 repo
svn-commit.tmp가 생성되는 것을 re-write method를 이용

make SVN commit-msg template use to svn-commit.tmp

Edit ~/.bashrc

~~~ bash
export SVN_EDITOR="python $HOME/svntemplr/templete-with-svn.py $HOME/svntemplr/commit-template svn-commit.tmp && vim svn-commit.tmp"
~~~
