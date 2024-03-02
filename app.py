from env import SQL, FLASK_ENUM
import pymysql
from flask import Flask, request, redirect, render_template, url_for,session
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__, static_url_path='/static')
app.secret_key = FLASK_ENUM.SECRET_KEY

@app.route('/')
def home():
    conn = pymysql.connect(
    host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, db=SQL.DB_NAME, charset='utf8'
    )

    cursor = conn.cursor()
    
    barcode = '123456789'
    sql = "INSERT INTO popcorn_user (name, phone_number, bank, menu, cord) VALUES (%s, %s, %s, %s, %s)"
    values = ('장*준', '01033333333', '국민은행', 'menu_value', barcode)
    cursor.execute(sql, values)
    conn.commit()

    conn.close()
    return "저장완료"

@app.route('/search_code',methods=['GET','POST'])
def search_code():
    
    code = request.form.get('code')
    
    print(code)


    session['code'] = code

    conn = pymysql.connect(
    host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, db=SQL.DB_NAME, charset='utf8'
    )

    cursor = conn.cursor()

    sql = "SELECT menu FROM popcorn_user WHERE cord = %s"
    
    cursor.execute(sql,(code,))
    results = cursor.fetchall()
    print(results)

    conn.close()

    if results:
        state = "정상쿠폰입니다."

    else:
        state = "이미사용한 쿠폰입니다."

    return render_template('index.html',next=results,state=state)

@app.route('/delete_code',methods=['GET','POST'])
def delete_code():

    conn = pymysql.connect(
    host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, db=SQL.DB_NAME, charset='utf8'
    )

    cursor = conn.cursor()

    code_num = session.get('code')

    query = f"""
    UPDATE popcorn_user
    SET cord = 0
    WHERE cord = {code_num};
    """

    cursor.execute(query)

    conn.commit()

    conn.close()

    state = "삭제하였습니다."
    
    return render_template('index.html',state=state)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)