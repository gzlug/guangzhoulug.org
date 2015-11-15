Title: R语言以及今年的GSoC
Slug: R Lang and GSoC 
Date:  2013-5-31
Category: Share
Tags: R, GSoC
Author: Jactry

作者：Qiang Kou  
原帖地址：https://groups.google.com/group/gzlug/browse_thread/thread/94898bb15b8ca2f?hl=zh-CN  

答应Qian Hong要跟大家分享一下GSoC的事情，7月就滚去北美读PhD了，六月聚会也不确定是否有时间，所以就发邮件给大家了。  

关于什么是R语言，见COS上的经典文章http://cos.name/2012/05/r-you-ready/  

由于data mining开始火，R也终于熬到了上位的时候。  

先聊聊圈子里的人，由于R依靠package构建整个生态圈的思路，圈子里的人一般是分三类的，R core team、contributer和user。  

user就是绝大部分用户咯，contributer就是在CRAN、bioconductor、Rmetrics等等地方提交package的兄弟们，R core team就是R的核心团队，人数不多，但负责维护R最底层和最核心的部分，负责升版本号的就是他们啦。  

既然要装B，自然就不能只停留在user这个水平，至少要开始写package，要开始contributer这条不归路。我只说一下我的思路，仅供非科班出身的朋友们参考。  

第一步，写package。其实很简单，你把自己平时用的最多的代码打包一下就OK了，当然最推荐的是R或C/C++，打包最容易，使用也最方便；  

第二步，提交package。CRAN上提交相对宽松一些，只要R CMD check这一步没问题，挂出来问题都不大。这也就是造成了CRAN上3000多个package水平参差不齐。bioconductor的审核要严格很多，package质量也就高很多。开发的过程中，推荐用github，R的devtools和Rstudio，至少现在写package比两年前要方便太多了；  

第三步，邮件列表，这个和贴吧灌水没什么区别；  

第四步，就是GSoC，从google code-in、google summer of code到google code jam，google在不遗余力地忽悠大家走上写代码的不归路。由于非科班出身和年龄问题，和我有关也就只有GSoC了。今年一共有177个开源组织参加，GCC、LLVM、KDE这些大型组织自然是gsoc里的大头。R project是gsoc最早参加的组织之一，今年起Bioconductor也正式加入。而且从google分配的slot来看，R project和Bioconductor已经接近GCC之类了。  

个人觉得，这是外围的业余开发者加入R社区最好的途径了。门槛不高，暑假里几乎可以把自己看作一个全职的开发人员了，而且有5000刀拿。R的contributer以大学教授和业界技术人员为主，在他们看来，三个月5000刀似乎有点太少了，所以他们不会和我争，所以今年我才侥幸拿到一个slot。  

下面两个链接分别是R project和bioconductor今年的项目。  

http://rwiki.sciviews.org/doku.php?id=developers:projects:gsoc2013  

http://bioconductor.org/developers/gsoc2013/  

R的偏后台，其中一个optimization的项目把我录了。bioconductor的shiny是我一直很喜欢的一个web前端，和mentor聊了聊，感觉自己的确没有前端经验，也就算了。  

我不是科班出身，计算机结构、操作系统之类的课程旁听过，作为一个没学会汇编，对底层的内存控制没什么感觉的人，混进R core team，我连想都没想过。  

走到这儿，其实作为一个contributer应该有的技能也就都具备了，以后还想继续混，也要看各位能不能在自己的领域里，用R解决些问题了。  

先聊这么多，六月聚会有机会再和各位聊。  
