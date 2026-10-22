# 配置 zsh 的笔记

## 为什么要装

Ubuntu 默认用的是 bash，能用，但没那么顺手。zsh 好在：

- 命令打错会变红，打对是绿的，一眼看出来
- 以前打过的命令，再打前几个字母，右边会冒出灰色的完整命令，按 → 就能补全
- 按 Ctrl+R 可以搜以前敲过的命令

组长让配这个，也是想让我熟悉 Linux 的 shell。

顺便理清一个概念：**终端是那个黑窗口，shell 是窗口里读命令、执行命令的程序。** 换 shell 只是换"谁来读我的命令"，不会动我电脑里的任何文件。

## 我怎么装的

**第一步，装 zsh：**

```bash
sudo apt install -y zsh
```

**第二步，装 oh-my-zsh：**

它是个管理 zsh 主题和插件的工具，装上之后配置起来省事。

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

装的时候它会问 "Do you want to change your default shell to zsh?"。**我当时答的是 n**，因为我的 conda 还挂在 bash 上，要是这时候换了，python 和 openai 都会找不到。

**第三步，把 conda 接到 zsh：**

```bash
conda init zsh
```

弄完重开 zsh，提示符前面又出现 `(base)`，python 也还是 3.13，说明环境没丢。

**第四步，最后才换默认 shell：**

```bash
chsh -s $(which zsh)
```

然后注销重新登录。再打开终端，`echo $SHELL` 显示 `/usr/bin/zsh`，就说明成了。

**顺便装的：** 后来还装了 Powerlevel10k（让提示符好看的）、一个 Meslo 字体（不然图标会显示成方块）、还有几个插件（灰字提示、命令高亮、补全）。这些是锦上添花，不装也能用。

## 装完怎么用

- 打开终端，默认就是 zsh 了
- 打错命令会变红，打对是绿的
- 打到一半按 →，能补全以前敲过的整条命令
- `Ctrl + R` 搜历史命令
- 输 `exit` 或者按 `Ctrl + D` 退出

## 改了配置怎么生效

配置文件是 `~/.zshrc`。改完以后：

```bash
source ~/.zshrc
```

或者干脆：

```bash
exec zsh
```

## 踩过的坑

**1. 换完 zsh，(base) 没了，python 变成 3.10**

因为我的 conda 初始化写在 `.bashrc` 里，zsh 不读那个文件。补一句 `conda init zsh` 就好了。

**2. 提示符显示成一堆 Σ 和方块**

是字体的问题。装了 MesloLGS NF 之后，还得在终端里把字体选成它，不然等于没装。

**3. `echo $SHELL` 一直是 /bin/bash**

其实 `chsh` 已经改成功了（`getent passwd tw` 里显示的是 zsh），只是当前这个终端窗口是改之前开的，环境变量没刷新。注销重新登录就好了，关窗口没用。

## 我学到的

- 终端和 shell 不是一回事
- `.zshrc` 是 zsh 的配置文件，每次开终端都会读一遍
- 换 shell 不影响文件，只影响"谁来读命令"
- 想退回去，敲 `chsh -s /bin/bash`，再登录就回到 bash
