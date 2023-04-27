# mooc-teacher-tools
慕课网讲师工具包

## waterMarkForPDF 
pptx 加水印，并转化为 pdf

## autoCodeAsync
批量操作 Git 仓库脚本
> 当你需要按照章节去更新你的代码的时候，可以使用该脚本。
他做了以下几件事：
- 删除当前目录下的以 `mooc-water-drop` 开头的文件夹。
- 克隆三个库。
- 修改三个库的远程地址。
- 把三个库的 `master` 分支都 reset 到某一个提交记录。
- 修改三个库的所有提交记录的时间。
- 强制提交三个库。

