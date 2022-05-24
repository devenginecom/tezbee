# 准备工作

在个人的PC上我们需要准备下面的工具：

1. Python3 
2. pip
3. virtualenv
4. node 

因为Smartpy是一个用于编写Tezos智能合约的eDSL，通过Python直接编写Tezos合约，那么我们需要准备好Smartpy的开发环境

## CLI 工具

Smartpy 团队为我们提供了CLI工具，让我们更加方便的进行测试和部署合约。

```
sh <(curl -s https://smartpy.io/cli/install.sh)
```

然后我们让他可以在任意的地方执行

```
export PATH=$PATH:~/smartpy-cli
```

## Smartpy 开发依赖

首先准备好 virtualenv 环境，然后完成samrtpy的安装工作

```
virtualenv .env
```

直接安装 

```
source .env/bin/activate
pip install smartpy
```