---
layout: page
title: Links
description: 没有链接的博客是孤独的
keywords: 友情链接
comments: true
menu: 链接
permalink: /links/
---

> 有用的链接
- [小小福 LeetCode 频道](https://www.youtube.com/channel/UCCMpGENpr93ENbfdinP3QeQ/featured)


{% for link in site.data.links %}
  {% if link.src == 'www' %}
* [{{ link.name }}]({{ link.url }})
  {% endif %}
{% endfor %}
