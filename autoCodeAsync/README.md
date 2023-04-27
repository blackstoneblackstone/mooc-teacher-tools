# 批量操作 Git 仓库脚本

这个脚本用于批量操作三个 Git 仓库：`mooc-water-drop-pc`、`mooc-water-drop-mobile` 和 `mooc-water-drop-server`。它执行以下操作：

1. 删除当前目录下的以 `mooc-water-drop` 开头的文件夹。
2. 克隆三个库。
3. 修改三个库的远程地址。
4. 把三个库的 `master` 分支都 reset 到某一个提交记录。
5. 修改三个库的所有提交记录的时间。
6. 强制提交三个库。

## 使用方法

将此脚本保存为一个名为 `batch_git_operation.sh` 的文件，然后通过终端运行：

```bash
chmod +x batch_git_operation.sh
./batch_git_operation.sh
```

在运行脚本时，它将提示您输入要将三个库的 master 分支重置到的提交记录的 commit message。输入 commit message，然后按 Enter 键继续。

请注意，脚本中的第 6 步（强制提交三个库）已被注释掉。在实际使用时，确保取消注释以实际执行该操作。

警告：此脚本会强制推送更改，可能导致丢失历史记录。在使用此脚本之前，请确保对您的仓库进行了备份。