# Judger 

[![Build Status](https://travis-ci.org/QingdaoU/Judger.svg?branch=newnew)](https://travis-ci.org/QingdaoU/Judger)

Judger for OnlineJudge 

[Document](https://docs.onlinejudge.me/#/judger/api)

[JudgeServer](https://github.com/QingdaoU/JudgeServer)

[OnlineJudge](https://github.com/QingdaoU/OnlineJudge)



## Usage

```
sudo apt-get install libseccomp-dev
mkdir build && cd build && cmake .. && make && sudo make install
```

A demo is available in `./demo/demo.py` . Remember to use "sudo" to execute. 

Required file:

`main.c`, uploaded by user;

`sample.in` and `sample.out`, the sample input and output. 

These files should be put in the same file with `demo.py`. 