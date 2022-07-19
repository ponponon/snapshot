Python 使用 selenium+chromedriver+chrome 实现网页截图

具体参考这篇文章: [docker 打包 selenium+chromedriver+chrome 遇到的坑和解决方案](https://segmentfault.com/a/1190000042181376)

# python 虚拟环境

## 安装 pipenv

mac:

```shell
brew install pipenv
```

debian/ubuntu

```shell
apt install pipenv
```

pip

```shell
pip install pipenv
```

## 安装虚拟机环境

```shell
pipenv install
```

## 激活虚假环境

```shell
pipenv shell
```

# Docker 相关

## 构建镜像

```
make build
```

> 如果没有 make 就安装一下

## 运行

```shell
docker-compose up
```
