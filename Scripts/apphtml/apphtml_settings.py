# vim: fileencoding=utf-8
"""
AppHtml settings
@author Toshiya NISHIO(http://www.toshiya240.com)
"""

settings = {
    'aff': "",
    'cnt': 8,
    'scs': {
        'iphone': 320,
        'ipad': 320,
        'mac': 480
    },
    'template': {
        '1) フル表示(SSフル+説明付)':u"<h2><span class='appTitle'><a href='${linkshareurl}' target='itunes_store'>${appname}</a></span></h2>\n<span class='appIcon'><img width='175' height='175' class='appIconImg' src='${icon175url}' style='border-radius: 38px;-moz-border-radius: 38px;-webkit-border-radius: 38px;margin: 0px 0px 15px 5px;'></span><br>\n<span class='appVersion'>バージョン: ${version}</span><br><span class='appPubDate'>リリース日: ${pubdate}</span><br>\n<span class='appPrice'>現在の価格: ${price}</span><br>\n<span class='appSize'>サイズ: ${appsize}</span><br style='clear: both;'>\n<span class='appCategory'>カテゴリ: ${category}</span><br>\n<span class='appSeller'>販売元: <a href='${selleritunes}' target='itunes_store'>${seller}</a></span><br>\n<span class='appCurVerRating'>現在のバージョンの評価: ★${curverrating}（${curreviewcnt}）</span><br>\n<span class='appAllVerRating'>全てのバージョンの評価: ★${allverrating}（${allreviewcnt}）</span><br>\n<span class='appUniv'>${univ}</span>\n<span class='appGamecenter'>${gamecenter}</span>\n<br>\n<span class='appDescNew'><strong>What’s New</strong></span><br>\n${descnew}<br>\n<br>\n${image1} ${image2} ${image3} ${image4} ${image5}<br>\n<br>\n${univimage1} ${univimage2} ${univimage3} ${univimage4} ${univimage5}<br>\n<br>\n<span class='appDesc'><strong>Description</strong></span><br>${desc}<br>\n<span><a href='${linkshareurl}' target='itunes_store'><img src='${storeButton}' style='vertical-align:bottom;' alt='App'></a></span>",
        '2) フル表示(SS2枚)':u"<h2><span class='appTitle'><a href='${linkshareurl}' target='itunes_store'>${appname}</a></span></h2>\n<span class='appIcon'><img width='175' height='175' class='appIconImg' src='${icon175url}' style='border-radius: 38px;-moz-border-radius: 38px;-webkit-border-radius: 38px;margin: 0px 0px 15px 5px;'></span><br>\n<span class='appVersion'>バージョン: ${version}</span><br>\n<span class='appPubDate'>リリース日: ${pubdate}</span><br>\n<span class='appPrice'>現在の価格: ${price}</span><br>\n<span class='appSize'>サイズ: ${appsize}</span><br style='clear: both;'>\n<span class='appCategory'>カテゴリ: ${category}</span><br>\n<span class='appSeller'>販売元: <a href='${selleritunes}' target='itunes_store'>${seller}</a></span><br>\n<span class='appCurVerRating'>現在のバージョンの評価: ★${curverrating}（${curreviewcnt}）</span><br>\n<span class='appAllVerRating'>全てのバージョンの評価: ★${allverrating}（${allreviewcnt}）</span><br>\n<span class='appUniv'>${univ}</span>\n<span class='appGamecenter'>${gamecenter}</span>\n<br>\n${image1} ${image2}<br>\n<span><a href='${linkshareurl}' target='itunes_store'><img src='${storeButton}' style='vertical-align:bottom;' alt='App'></a></span>",
        '3) 大アイコン表示': u"<h2><span class='appTitle'><a href='${linkshareurl}' target='itunes_store'>${appname}</a></span></h2>\n<span class='appIcon'><img width='175' height='175' class='appIconImg' src='${icon175url}' style='border-radius: 38px;-moz-border-radius: 38px;-webkit-border-radius: 38px;margin: 0px 0px 15px 5px;'></span><br>\n<span class='appVersion'>バージョン: ${version}</span><br>\n<span class='appPubDate'>リリース日: ${pubdate}</span><br>\n<span class='appPrice'>現在の価格: ${price}</span><br>\n<span class='appSize'>サイズ: ${appsize}</span><br style='clear: both;'>\n<span class='appCategory'>カテゴリ: ${category}</span><br>\n<span class='appSeller'>販売元: <a href='${selleritunes}' target='itunes_store'>${seller}</a></span><br>\n<span class='appCurVerRating'>現在のバージョンの評価: ★${curverrating}（${curreviewcnt}）</span><br>\n<span class='appAllVerRating'>全てのバージョンの評価: ★${allverrating}（${allreviewcnt}）</span><br>\n<span class='appUniv'>${univ}</span>\n<span class='appGamecenter'>${gamecenter}</span>\n<br>\n<span><a href='${linkshareurl}' target='itunes_store'><img src='${storeButton}' style='vertical-align:bottom;' alt='App'></a></span>",
        '4) 中アイコン表示': u"<span class='appIcon'><img class='appIconImg' width='100' height='100' src='${icon100url}' style='float:left;border-radius: 22px;-moz-border-radius: 22px;-webkit-border-radius: 22px;margin: 0px 15px 15px 5px;'></span>\n<span class='appName'><strong><a href='${linkshareurl}' target='itunes_store'>${appname}</a></strong></span><br>\n<span class='appVersion'>バージョン: ${version}</span><br>\n<span class='appPrice'>現在の価格: ${price}</span><br>\n<span class='appSize'>サイズ: ${appsize}</span><br style='clear: both;'>\n<span class='appCategory'>カテゴリ: ${category}</span><br>\n<span class='appSeller'>販売元: <a href='${selleritunes}' target='itunes_store'>${seller}</a></span><br>\n<span class='appAllVerRating'>全てのバージョンの評価: ★${allverrating}（${allreviewcnt}）</span><br>\n<span class='appUniv'>${univ}</span>\n<span class='appGamecenter'>${gamecenter}</span>\n<br>\n<span><a href='${linkshareurl}' target='itunes_store'><img src='${storeButton}' style='vertical-align:bottom;' alt='App'></a></span>",
        '5) 小アイコン表示': u"<span class='appIcon'><img width='75' height='75' class='appIconImg' src='${icon75url}' style='float:left;border-radius: 16px;-moz-border-radius: 16px;-webkit-border-radius: 16px;margin: 0px 15px 15px 5px;'></span>\n<span class='appName'><strong><a href='${linkshareurl}' target='itunes_store'>${appname}</a></strong></span><br>\n<span class='appVersion'>バージョン: ${version}</span><br>\n<span class='appPrice'>現在の価格: ${price}</span><br>\n<span class='appCategory'>カテゴリ: ${category}</span><br>\n<span class='appSeller'>販売元: <a href='${selleritunes}' target='itunes_store'>${seller}</a></span><br>\n<span class='appUniv'>${univ}</span>\n<span class='appGamecenter'>${gamecenter}</span>\n<br style='clear: both;'>\n<span><a href='${linkshareurl}' target='itunes_store'><img src='${storeButton}' style='vertical-align:bottom;' alt='App'></a></span>",
        '6) リンクのみ': u"<span class='appTitle'><a href='${linkshareurl}' target='itunes_store'>${title} - ${seller}</a></span>"
    }
}