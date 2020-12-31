---
layout: page
title: Wiki
description: 人越学越觉得自己无知
keywords: 维基, Wiki
comments: false
menu: 维基
permalink: /wiki/
---

<div>
    <b>欢迎大家支持我的频道</b>
    <br>
    <img src="/images/wiki/pay_venmo.png" width="250">
    <br>
    <img src="/images/wiki/pay_wechat.png" width="250">
</div>

<ul class="listing">
{% for wiki in site.wiki %}
{% if wiki.title != "Wiki Template" %}
<li class="listing-item"><a href="{{ site.url }}{{ wiki.url }}">{{ wiki.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
