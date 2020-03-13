import sqlite3

# items.dbとつなぐ(なければ作られる)
conn = sqlite3.connect('board.db')
c = conn.cursor()

# テーブル作成
c.execute("create table board(id, name, date, comment)")

# 投入
c.execute("insert into board values(1,'管理人','2020年1月1日 1:23:54','ここに投稿が表示されます')")
c.execute("insert into board values(2,'管理人','2020年1月2日 8:11:10','節度を持った投稿を心掛けましょう')")

# 確定
conn.commit()
conn.close()