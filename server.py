import sqlite3, datetime
from bottle import route, run, template, request, redirect, debug, static_file, get, TEMPLATE_PATH

TEMPLATE_PATH.append('./tpl')
dbname="root.db"
@get("/static/css/<filepath:re:.*\.(jpg|png|gif|ico|svg|css)>")
def css(filepath):
    return static_file(filepath, root="static/css")

# / にアクセスしたら index関数が呼ばれる
@route("/")
def index():
    # 画面に表示されて欲しいHTMLを戻す
    return template('welcome.html')

@route("/input")
def def_input():
    # 画面に表示されて欲しいHTMLを戻す
    #return template('guide.html')
    return template('input.html')

@route("/guide")
def view_guide():
    # 画面に表示されて欲しいHTMLを戻す
    #return template('guide.html')
    return template('guide.html')

@route("/list")
def view_list():
    # board.dbとつなぐ(なければ作られる)
    conn = sqlite3.connect('board.db')
    c = conn.cursor()
    c.execute("select id,name,date,comment from board order by id")
    list = []
    for row in c.fetchall():
        list.append({
            "id": row[0],
            "name": row[1],
            "date": row[2],
            "comment": row[3]
        })
    conn.close()
    # 表示はテンプレートを戻す
    return template('list_tmpl.tpl', list=list)


@route("/add", method=["GET", "POST"])
def add_item():
    if request.method == "POST":
        # POSTアクセスならDBに登録する
        # フォームから入力されたアイテム名の取得
        name = request.POST.getunicode("name")
        comment = request.POST.getunicode("comment")
        conn = sqlite3.connect('board.db')
        c = conn.cursor()
        # 現在の最大ID取得(fetchoneの戻り値はタプル)
        new_id = c.execute("select max(id) + 1 from board").fetchone()[0]
        date = datetime.datetime.now()
        dt_now=str(date.year)+"年"+str(date.month)+"月"+str(date.day)+"日 "+str(date.hour)+":"+str(date.minute)+":"+str(date.second)
        c.execute("insert into board values(?,?,?,?)", (new_id, name, dt_now, comment))
        conn.commit()
        conn.close()
        return template('redirect.html')
    else:
        # GETアクセスならフォーム表示
        return template('add_tmpl.tpl')

@route("/del/<id:int>")
def del_item(id):
    conn = sqlite3.connect('board.db')
    c = conn.cursor()
    # 指定されたidを元にDBデータを削除
    c.execute("delete from board where id=?", (id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/list")

@route("/root")
def def_root():
    html='<!DOCTYPE html><body><img width="600" height="600" src="https://map.yahooapis.jp/course/V1/routeMap?appid=dj00aiZpPVdETXM1a3h6RjNCSiZzPWNvbnN1bWVyc2VjcmV0Jng9MTM-&route='
    # point1=request.forms.getunicode("point1")
    # point2=request.forms.getunicode("point2")
    point1="名鉄名古屋駅"
    point2="名鉄ニューグランドH"
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    sql='SELECT*FROM points order by id ASC'
    for n in c.execute(sql):
        print(n[1]+n[2])
        if(n[1]==point1):
            data1=n[2]+","+n[3]
    for n in c.execute(sql):
        print(n[1])
        if(n[1]==point2):
            data2=n[2]+","+n[3]
    conn.close()
    
    html+=data1+","+data2
    html+='|color:0000ffff&width=600&height=600"><div><a href="/"><input type="submit" value="TOPへ"></div><div><a href="/guide"><input type="submit" value="ルート案内へ"></div></body></html>'
    return html

# サーバを起動
run(host='localhost', port=8080, debug=True, reload=True)