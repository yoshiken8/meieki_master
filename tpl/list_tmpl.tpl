<html>
<head>
    <meta http-equiv="content-type" charset="utf-8">
    <link type="text/css" href="/static/css/stylesheet2.css" rel="stylesheet">
</head>
<body>


<div class="header">
	<div class=" header-logo">Meieki Master</div>
	<div class="header-list">
	  <ul>
		<li><a href="/">HOME</a></li>
		<li><a href="/list">みんなの投稿</a></li>
		<li>お問い合わせ</li>
	  </ul>
	</div>
  </div>
<h3>みんなの名古屋駅に関する口コミ投稿一覧</h3>
<form action="" method="post">
<br>
<a href='/add' >新規投稿はこちらから</a>
<table border="1">
% for board in list:
  <tr>
    <td>
    <p style="background-color:#87CEFA;">
    {{board["id"]}} : {{board["name"]}}&emsp;{{board["date"]}}&emsp;<a href="/del/{{board['id']}}">投稿削除</a>&emsp;
    </p>
    {{board["comment"]}}</td>
  </tr>
% end
</table>
</body>
</html>