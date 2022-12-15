## Instructions

[美赛该怎么准备，我从来就没参与过，也不是很了解数学建模？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/358328223/answer/1007726078)

[COMAP: **Contest Registration and Instructions**](https://www.contest.comap.com/highschool/contests/himcm/instructions.html)

## Figuring

[Matplotlib 绘图标记 | 菜鸟教程 (runoob.com)](https://www.runoob.com/matplotlib/matplotlib-marker.html)

```python
colors = ['#8ECFC9', 'FFBE7A', 'FA7F6F', '82B0D2', 'BEB8DC', 'E7DAD2', '999999']
sns.set(palette = sns.hls_palette(10, l=0.7, s=0.4))
```

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

## Algorithm Todo List

- 层次分析

- 相关分析

- 多元线性回归

- 聚类

- 主成分分析

- ~~线性规划~~
