#!/bin/bash

# 1. 删除当前目录下的 mooc-water-drop 开头的文件夹
echo "Step 1: 删除当前目录下的 mooc-water-drop 开头的文件夹"
find . -type d -name "mooc-water-drop*" -exec rm -rf {} + || exit 1

# 2. 克隆三个库
echo "Step 2: 克隆三个库"
git clone git@github.com:blackstoneblackstone/mooc-water-drop-pc.git || exit 1
git clone git@github.com:blackstoneblackstone/mooc-water-drop-mobile.git || exit 1
git clone git@github.com:blackstoneblackstone/mooc-water-drop-server.git || exit 1

# 3. 修改三个库的远程地址
echo "Step 3: 修改三个库的远程地址"
cd mooc-water-drop-pc && git remote set-url origin ssh://git@git.imooc.com:80/coding-643/water-drop-pc.git || exit 1
cd ..
cd mooc-water-drop-mobile && git remote set-url origin ssh://git@git.imooc.com:80/coding-643/water-drop-mobile.git || exit 1
cd ..
cd mooc-water-drop-server && git remote set-url origin ssh://git@git.imooc.com:80/coding-643/water-drop-server.git || exit 1
cd ..

# 4. 把三个库的 master 分支都 reset 到某一个提交记录
echo "请输入要 reset 的提交记录的 commit message:"
read commit_message

for repo in mooc-water-drop-pc mooc-water-drop-mobile mooc-water-drop-server
do
  cd $repo
  git reset --hard $(git log --all --grep="$commit_message" --format='%H' -n 1)
  cd ..
done

# 5. 修改三个库的所有提交记录的时间
echo "Step 5: 修改三个库的所有提交记录的时间"
for repo in mooc-water-drop-pc mooc-water-drop-mobile mooc-water-drop-server; do
    git -C $repo filter-branch -f --env-filter '
        export GIT_AUTHOR_NAME="Blackstone"
        export GIT_AUTHOR_EMAIL="601735416@qq.com"
        export GIT_AUTHOR_DATE="$(date +%Y-%m-%d) 00:00"
        export GIT_COMMITTER_DATE="$(date +%Y-%m-%d) 00:00"
    ' master
done

# 6. 强制提交三个库
# for repo in mooc-water-drop-pc mooc-water-drop-mobile mooc-water-drop-server
# do
#   cd $repo
#   git push -f origin master || exit 1
#   cd ..
# done

echo "所有步骤已完成"