# Graph_Python
 数据结构「图」的 Python 实现。

## 说明

这是我以前学习「图」的时候写的一些 Python 源码。
主要参考了《算法导论》、《算法》还有 MIT 的 *[6.006: Introduction to Algorithms (Fall 2011)](https://courses.csail.mit.edu/6.006/fall11/)* 课程。

## 项目文件

```
.
├── graph_adj.py    # 邻接矩阵表示的图
├── graph_class.py  # 类表示的图
├── DFS.py          # 基于类表示的图的 DFS
├── BFS.py          # 基于类表示的图的 BFS
├── tinyG.txt       # 一个很小的图
├── mediumG.txt     # 一个中等大小的图
├── largeG.txt.zip  # 一个很大的图
├── tinyG.png       # tinyG 的直观图形表示
├── mediumG.png     # mediumG 的图的直观图形表示
└── README.md
```

-  `*.txt` 是表示图的数据，来自《算法》的资料，可以用 graph_adj.py 读取。（largeG.txt 太大了，超过100MB了，被我压缩成了zip）。
- `*.png` 是 graph_adj.py 生成的图的直观图形表示。

## 开放源代码

Apache License

Copyright 2020 CDFMLR