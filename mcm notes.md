## Instructions

[美赛该怎么准备，我从来就没参与过，也不是很了解数学建模？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/358328223/answer/1007726078)

[COMAP: **Contest Registration and Instructions**](https://www.contest.comap.com/highschool/contests/himcm/instructions.html)

## Coding

### Figuring

[Matplotlib 绘图标记 | 菜鸟教程 (runoob.com)](https://www.runoob.com/matplotlib/matplotlib-marker.html)

```python
colors = ['#8ECFC9', 'FFBE7A', 'FA7F6F', '82B0D2', 'BEB8DC', 'E7DAD2', '999999']
sns.set(palette = sns.hls_palette(10, l=0.7, s=0.4))
```

### Data Analysis

[python numpy 常用随机数的产生方法 - CSDN](https://blog.csdn.net/m0_37804518/article/details/78490709)
[Python中numpy数组的拼接、合并_赵至柔的博客-CSDN博客_numpy 拼接](https://blog.csdn.net/qq_39516859/article/details/80666070)
[Python数据分析之numpy数组全解析 - 奥辰 - 博客园 (cnblogs.com)](https://www.cnblogs.com/chenhuabin/p/11412818.html#_label3)
[十分钟入门 Pandas | Pandas 中文](https://www.pypandas.cn/docs/getting_started/10min.html)

## Essay

#### Framework

```
1 Overview（或者Background、Restatement）
2 Assumptions and Justification
3 Notation
4 Analysis and Modeling
5 Sensitivity Analysis
6 Strengths and Weaknesses
7 Practical Application（或者Future work）
```

## Type Setting

[LaTeX排版札记：part 4—插入图片（并排显示、自定义编号） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/32925549)

[LaTeX札记（二）：表格 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/07/06/latex-note-02/)

## Writing

[浩然：为时不晚！美赛最后一天就能让你跃升到M奖的绝招！- bilibili](https://www.bilibili.com/video/BV1HZ4y1d7xf/)
[【2022美赛大招】O奖揭秘怎样避免S奖？原来玄机在这里 - bilibili](https://www.bilibili.com/video/BV1LT4y1X78r) Note：这个说的是 MCM，即面向大学学生的比赛。看 Part 1, 3, 4 差不多了。
[【拿奖绝招】如何模仿美赛O奖论文？H奖究竟比O奖差在哪？ - bilibili](https://www.bilibili.com/video/BV15R4y1M7fX)

三个视频一共 1h 左右。

## O Essay Analysis

#### Summary Sheet Analysis

- Para 1
  - 前一半讲现状，类似于某 ETS 考试作文的引入，后面写两句 to solve this, we developed a model that ...

- Para 2
  - 讲我们的模型考虑了哪些因素，用了什么方法。也就是对于整个模型运行过程的一个概述。
  - example:
      To solve this problem, we build a comprehensive evaluation model and apply **Analytical Hierarchical Process (AHP)** and **Technique for Order Performance by Similarity to Ideal Solution(TOPSIS)** to gain the ranking list of the jobs for each typical fictional person. After acquiring the ranking list, we divide the jobs into groups through **cluster analysis** and recommend the jobs with the highest ranking in each group to the students. We also develop the concept and design of an app targeting high school students who would like to find a summer job. We propose its user-friendly features including artistic interfaces and relatively accurate results.

- Para 3 (Optional)
  - 细化讲整个模型的流程。也可以把**考虑因素**和**方法**分在两段里面写。

- Para 4 ---
  - 讲你的 application, adaptation, or model testing (or sensitivity analysis)。每个应该各占一段。比如说用一两句话说明一下为什么 model testing 是有效的，或者针对特殊情况的什么特点做了 adaptation。然后叙述结果。

- 当然还有 keywords。

#### 2020 A: The Best Summer Job

1. 10656
  - 语言非常好，是我完全写不出来的水平。用词值得借鉴。
  - **把一个问题分多个场景讨论**：比如 occupation 分成 jobs / internships
  - 模型很平，没啥意思。
  - 表做得比较 colorful，其实不好看，但是最后的 website 很好看。图不多。
  - **不是很懂为啥这玩意能 O**

2. 10701
  - 语言很亲民。
  - 用了一些经典基本的东西。层次分析、ranking、聚类。
  - 画了很多很好看的流程图。聚类的图画得很有趣，可能是加分项。
  - 用很多熟悉算法的时候当然要把算法流程讲一遍。

## Algorithm Todo List

- 层次分析
  - 似乎很重要。
  - 应用场景是，方案选择。
  - [数学建模第一讲 - 层次分析法AHP - 简书](https://www.jianshu.com/p/5c7af1537b3e)

- 相关分析
  - [数学建模笔记——相关系数 - 知乎](https://zhuanlan.zhihu.com/p/194254252)
  - 置信度分析那块，没很看懂。但是会用。

- 多元线性回归
  - 也就是，多元的线性回归。

- 聚类
  - 也就是，分类。
  - [Python数模笔记-Sklearn（2）聚类分析 - youcans](https://www.cnblogs.com/youcans/p/14751078.html)
    - 这个老哥博客写得很好啊。

- 主成分分析
  - 相当于样本空间降维。
    [数学建模——主成分分析(SPSS） - 知乎](https://zhuanlan.zhihu.com/p/63139206)

- 线性规划
  - 有个库叫 PuPL，线性规划万能。
  - [Python数模笔记-PuLP库（1）线性规划入门 - youcans](https://www.cnblogs.com/youcans/p/14714085.html)

- 综合评价体系
  - [数学建模之综合评价问题 - 知乎](https://zhuanlan.zhihu.com/p/109925628)

## Thoughts

- 美赛评分注重创新。搞点有意思的。但是其实我不是很懂什么才叫有意思。

- 很多东西的参数是可以直接人为钦定的。至少在 HiMCM。

- 论文好看和文字水平很重要。所以打算用 LaTeX。

- 对于算法，重要的是知道有这么个东西，了解其应用场景和局限性。细节部分，可以等用到了再去学。经典算法都有现成的库可以做，所以其实算法可以完全不用学。不过我还是喜欢学。

## Final Notes

- 排版和画图之类周边的东西 lyc 来做。

- sty **可以写的**部分有：
  - **这个部分和论文一起看** [[10701.pdf]]
  
  - Intro
  - Problem Restatement and Analysis / Background / Our work
  - Assumptions and Justification
  - 一些简单综合评价模型中，文字多的部分。其实有很多这种。比如 pdf 第 8-9 页。
  - Model Testing 的分析部分以及图表的分析。你看这个论文 model testing 写了八九页。
  - 后面一大堆。比如那个 app 的 user experience，strengths and weaknesses 还有 conclusion and future works。
  - 还有 summary sheet。
  - 这么看来好像基本全能写。那我为什么不直接说不能写的。
  - 呃还有。上面三个视频可以抽空看一下。

- 建模本不是一个有很强数学性的过程。只有算法的落地实现涉及数学。