---
layout: page
title: Donation
description: 人越学越觉得自己无知
keywords: Donation
comments: false
menu: 捐赠
permalink: /donation/
---


<div>
    <b>捐赠 | Donation</b>
    <br>
    如果您喜欢我们的内容，欢迎捐赠小小福! 
    <br>
    If you like my blog, donations are welcome.
    <br>
    <!-- Venmo donation -->
    <img src="/images/donation/pay_venmo.png" width="250">
    <br>
    <!-- Wechat donation -->
    <img src="/images/donation/pay_wechat.png" width="250">
    <br>
    <!-- Donation from Paypal -->
    <div>
        <form action="https://www.paypal.com/donate" method="post" target="_top">
        <input type="hidden" name="cmd" value="_donations" />
        <input type="hidden" name="business" value="7NHRKFZH4J59S" />
        <input type="hidden" name="currency_code" value="USD" />
        <input type="image" src="https://www.paypalobjects.com/zh_XC/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="使用PayPal按钮进行捐赠" />
        <img alt="" border="0" src="https://www.paypal.com/zh_US/i/scr/pixel.gif" width="1" height="1" />
        </form>
    </div>
</div>
<br>
<br>
<br>



<div>
    <b>信用卡 | Credit Card Opening</b>
    <br>
    <table>
        <tr>
            <td>
                <img src="/images/donation/freedomunlimitedcard.png" width="250">
                <img src="/images/donation/freedomflexcard.png" width="250">
            </td>
        </tr>
        <tr>
            <td>
                <b><u><a href = "https://www.referyourchasecard.com/18f/Z5C0M0EEFS">Chase Freedom Card</a></u></b>
                <br>
                ($200 Cash back) No Annual Fee
            </td> 
        </tr>
    </table>
</div>
<br>
<br>
<br>



<div>
    <b>股票账号 | Stock Account Opening</b>
    <br>

    <table>
        <tr>
            <td>
                <img src="/images/donation/robinhood.png" width="250">
            </td>
        </tr>
        <tr>
            <td>
                <b><u><a href ="https://join.robinhood.com/zhentax">Robinhood</a></u></b>
                <br>
                Up to $220.79 Free Stocks, No Commission Fee
            </td> 
        </tr>
    </table>

</div>
<br>
<br>
<br>



 




<ul class="listing">
{% for wiki in site.wiki %}
{% if wiki.title != "Wiki Template" %}
<li class="listing-item"><a href="{{ site.url }}{{ wiki.url }}">{{ wiki.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
