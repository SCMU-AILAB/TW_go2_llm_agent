# git 操作练习笔记

## 一开始的印象

觉得 git 命令多、术语多，看不懂。后来发现日常其实就那几条，剩下的都是"用到再查"。

## git 是什么

一句话：**给项目拍照存档。**

- 改文件
- `git add`：把要存的改动挑出来
- `git commit`：按下快门，拍一张快照存进历史
- `git push`：把快照传到 GitHub

每张"照片"都有一个编号，还带着你写的一句说明。以后想回到哪一版，都找得到。

## 我练过、也真在用的六条

| 命令 | 干什么 |
|---|---|
| `git status` | 看现在什么状态（迷糊了就敲它） |
| `git add -A` | 把改动放进"待提交" |
| `git commit -m "说明"` | 拍一张快照 |
| `git log --oneline -3` | 看最近 3 条历史 |
| `git push` | 推到 GitHub |
| `git pull` | 把别人的新改动拉下来 |

## 红区、绿区、干净

这是我第一次看懂的"状态"：

- 改了文件，还没 add → **红色**（尚未暂存的变更）
- `git add` 之后 → **绿色**（要提交的变更）
- `git commit` 之后 → **干净的工作区**

**红 → 绿 → 干净**，就是 add 和 commit 的全部意义。

## 我实际走过的一遍

1. 在 `README.md` 末尾加一行
2. `git status` → 看到 README.md 变红
3. `git add -A` → 再 `git status`，变绿了
4. `git commit -m "docs: 练习 git 命令"` → 提示 1 file changed
5. `git status` → 干净
6. `git push` → 推到 GitHub
7. `git log --oneline -3` → 最上面就是我刚提交的那条

## 分支是什么

- `main` 是主干道
- 新建一个分支，就是从这个点岔出去一条路，不影响主干
- **不合并的话，分支上的东西不会进 main**
- 合并之后，main 才有那些改动

我一开始以为"推了分支就等于进 main 了"，其实不是，得单独合并。

## 我踩过的坑

**1. 粘贴命令时混进怪符号**

有时粘多行命令，终端会插进 `^[[200~` 或 `~`，命令就报"找不到命令"。**一行一行敲最稳。**

**2. 连不上 GitHub**

`Failed to connect to github.com port 443`。国内需要代理。给 git 单独配：

```bash
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
```

**3. token 被写进了 remote 地址**

`git remote -v` 里能看到 `https://用户名:ghp_xxxx@github.com/...`。这样 token 是明文躺在配置里的，不安全，应该换成干净地址。

**4. 文件名里带引号**

`print("hello world").py` 这种名字，运行时会因为引号被吃掉而"找不到文件"。**文件名只用字母、数字、下划线。**

**5. 路径写重复了**

`cd ~/home/tw/桌面/...` 报错。因为 `~` 本身就是 `/home/tw`，再拼 `/home/tw` 就重了。正确是 `cd ~/桌面/...`。

## 我学到的

- 改文件不等于存档，得 add + commit 才算
- 提交信息要写清楚，以后回看全靠它
- push 之前先 pull，不然容易冲突
- 分支不会自动进 main，要合并
- 出问题先 `git status`，它会告诉你现在什么状况
