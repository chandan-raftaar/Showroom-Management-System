from os import name
import re
import psycopg2
from flask import Flask,render_template,url_for,request,redirect,flash

app = Flask(__name__)
app.secret_key="super secret key"

con = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "vehicle_mgmt",
    user = "postgres",
    password = "PESCS122"
)

cur = con.cursor()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

#users
@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/owner")
def owner():
    return render_template("owner.html")

@app.route("/agent")
def agent():
    return render_template("agent.html")

#tables
@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/customer")
def customer():
    return render_template("customer.html")
@app.route("/employeeOwner")
def employeeOwner():
    return render_template("employeeOwner.html")
@app.route("/queriesowner")
def queriesowner():
    return render_template("queriesowner.html")
@app.route("/queriesemp")
def queriesemp():
    return render_template("queriesemp.html")
@app.route("/queriesagent")
def queriesagent():
    return render_template("queriesagent.html")
# sales
@app.route("/sales/insert",methods = ['GET','POST'])
def insertsales():
    if request.method == 'POST':
        obj = request.form
        sid = obj['saleid']
        eid = obj['empid']
        mid = obj['mfgid']
        cid = obj['custid']
        stat = obj['status']
        tax = obj['tax']
        ord = obj['odate']

        cur.execute("insert into sales values({0},{1},'{2}',{3},'{4}',{5},'{6}')".format(sid,eid,mid,cid,stat,tax,ord))
        con.commit()
        return render_template("done.html")
    else:
        return render_template("insertsales.html")

@app.route("/agent/sales")
def agentsales():
    return render_template("agentsales.html")

@app.route("/sales/view")
def viewsales():
    cur.execute("ROLLBACK")
    cur.execute("select * from sales")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    

    return render_template('view.html',content = [rows,col])

@app.route("/sales/select",methods = ['GET','POST'])
def selectsales():
    if request.method == 'POST':
        sid = request.form['saleid']
        cur.execute("select * from sales where sale_id = {0}".format(sid))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("selectsales.html")



#cutomer
@app.route("/customer/insert",methods = ['GET','POST'])
def insertcust():
    if request.method == 'POST':
        obj = request.form
        cid = obj['cid']
        fname = obj['fname']
        minit = obj['minit']
        lname = obj['lname']
        cno = obj['cno']
        g = obj['g']
        loc = obj['loc']
        state = obj['state']
        city = obj['city']
        pin = obj['pin']
        mailid = obj['email']
        cur.execute("insert into customer values({0},'{1}','{2}','{3}',{4},'{5}','{6}','{7}','{8}','{9}','{10}')".format(cid,fname,minit,lname,cno,g,loc,state,city,pin,mailid))
        con.commit()
        flash('Customer Added Successfully')
        return render_template("done.html")
    else:
        return render_template("insertcust.html")

@app.route("/customer/view")
def viewcust():
    cur.execute("select * from customer")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/customer/select",methods = ['GET','POST'])
def selectcust():
    if request.method == 'POST':
        cid = request.form['cid']
        cur.execute("select * from customer where cust_id = {0}".format(cid))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("selectcust.html")

#dealer
@app.route("/dealer")
def dealer():
    return render_template("dealer.html")

@app.route("/dealer/insert",methods = ['GET','POST'])
def insertdealer():
    if request.method == 'POST':
        obj = request.form
        did = obj['did']
        name = obj['name']
        cno = obj['cno']
        cur.execute("insert into showroom owner values({0},'{1}',{2})".format(did,name,cno))
        con.commit()
        flash('Dealer Added Successfully')
        return render_template("done.html")
    else:
        return render_template("insertdealer.html")

@app.route("/dealer/view")
def viewdealer():
    cur.execute("select * from showroom owner")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/dealer/select",methods = ['GET','POST'])
def selectdealer():
    if request.method == 'POST':
        did = request.form['did']
        cur.execute("select * from showroom owner where d_id = {0}".format(did))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("selectdealer.html")
#showroom
@app.route("/showroom")
def showroom():
    return render_template("showroom.html")

@app.route("/showroom/insert",methods = ['GET','POST'])
def insertshowroom():
    if request.method == 'POST':
        obj = request.form
        sid = obj['sid']
        did = obj['did']
        cno = obj['cno']
        loc = obj['loc']
        stat = obj['state']
        city = obj['city']
        pin = obj['pin']
        cur.execute("insert into showroom values({0},{1},{2},'{3}','{4}','{5}','{6}')".format(sid,did,cno,loc,stat,city,pin))
        con.commit()
        flash('Showroom Added Successfully')
        return render_template("done.html")
    else:
        return render_template("insertshowroom.html")

@app.route("/showroom/view")
def viewshowroom():
    cur.execute("select * from showroom")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/showroom/select",methods = ['GET','POST'])
def selectshowroom():
    if request.method == 'POST':
        sid = request.form['sid']
        cur.execute("select * from showroom where s_id = {0}".format(sid))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("selectshowroom.html")

#owner
@app.route("/employeeOwner/insert",methods = ['GET','POST'])
def insertemployee():
    if request.method == 'POST':
        obj = request.form
        eid = obj['sid']
        sid = obj['did']
        name = obj['cno']
        desg = obj['loc']
        salary = obj['state']
        

        cur.execute("insert into employee values({0},{1},'{2}','{3}',{4})".format(eid,sid,name,desg,salary))
        con.commit()
        flash('Employee Added Successfully')
        return render_template("done.html")
    else:
        return render_template("insertemployee.html")
@app.route("/employeeOwner/view")
def viewemployee():
    cur.execute("select * from employee")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/employeeOwner/select",methods = ['GET','POST'])
def selectemployee():
    if request.method == 'POST':
        sid = request.form['empid']
        cur.execute("select * from employee where emp_id = {0}".format(sid))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("selectemployee.html")

@app.route("/queriesowner/Show the employees with their total number of sales")
def query1():
    cur.execute("select emp_id,count(*) from sales group by emp_id")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/queriesowner/Show the number of sales persons in each showroom")
def query2():
    cur.execute("select count(*), s_id from employee where designation='Sales Person' group by s_id")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/queriesowner/all employees",methods = ['GET','POST'])
def query7():
    if request.method == 'POST':
        sid = request.form['sid']
        cur.execute("select * from employee where s_id = {0}".format(sid))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template('showroomid.html')

@app.route("/queriesagent/salesmade",methods = ['GET','POST'])
def query3():
    if request.method == 'POST':
        year = request.form['yr']
        cur.execute("select s_id,count(*) from sales,employee where sales.emp_id = employee.emp_id and cast(sales.order_date as varchar) like '{0}%' group by s_id".format(year))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template('year.html')

@app.route("/queriesagent/salescompany",methods = ['GET','POST'])
def query4():
        cur.execute("select substr(mfg_id,1,2) as alpha,count(*) from sales group by substr(mfg_id,1,2)")
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])


@app.route("/queriesagent/Show maximum showroom sales")
def query5():
    cur.execute("select s_id,count(*) from sales,employee where sales.emp_id = employee.emp_id group by s_id order by count desc fetch FIRST ROW only;")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])

@app.route("/queriesagent/which showroom the best employee belongs to")
def query6():
    cur.execute("select s_id,emp_id from employee where emp_id = (select emp_id from (select emp_id,count(sale_id) as sc from sales group by emp_id) sub order by sc desc fetch FIRST ROW only);")
    rows = cur.fetchall()
    col = [desc[0] for desc in cur.description]
    return render_template('view.html',content = [rows,col])



#queries for employee:
@app.route("/queriesemp/Show the most often car buyers",methods = ['GET','POST'])
def eq1():
    if request.method == 'POST':
        eid = request.form['eid']
        cur.execute("select s_id from employee where emp_id = {0}".format(eid))
        res1 = cur.fetchall()
        sid = res1[0][0]
        cur.execute("select sales.cust_id,count(*) from sales,employee where sales.emp_id = employee.emp_id and s_id = {0} group by cust_id".format(sid))
        rows = cur.fetchall()

        col = [desc[0] for desc in cur.description]
        
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("empid.html")

@app.route("/queriesemp/payment pending",methods = ['GET','POST'])
def eq2():
    if request.method == 'POST':
        eid = request.form['eid']
        cur.execute("select s_id from employee where emp_id = {0}".format(eid))
        res1 = cur.fetchall()
        sid = res1[0][0]
        cur.execute("select sales.cust_id from sales,employee where sales.emp_id = employee.emp_id and s_id = {0} and status = 'PENDING'".format(sid))
        res2 = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [res2,col])
    else:
        return render_template("empid.html")

@app.route("/queriesemp/vehicletype",methods = ['GET','POST'])
def eq3():
    if request.method == 'POST':
        eid = request.form['eid']
        type = request.form['type']
        # return f"<h1>{eid}</h1>"
        cur.execute("select s_id from employee where emp_id = {0}".format(eid))
        res1 = cur.fetchall()
        sid = res1[0][0]
        cur.execute("select mfg_id,v_name,s_id from vehicle where v_desc like '%{0}%' and s_id = {1}".format(type,sid))
        res2 = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [res2,col])
    else:
        return render_template("vehicletype.html")

@app.route("/queriesemp/available",methods = ['GET','POST'])
def eq4():
    if request.method == 'POST':
        eid = request.form['eid']
        cur.execute("select s_id from employee where emp_id = {0}".format(eid))
        res1 = cur.fetchall()
        sid = res1[0][0]
        cur.execute("select * from vehicle where s_id = {0}".format(sid))
        res2 = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [res2,col])
    else:
        return render_template("empid.html")

@app.route("/queriesemp/alternateshowroom",methods = ['GET','POST'])
def eq5():
    if request.method == 'POST':
        name = request.form['name']
        cur.execute("select showroom.s_id,location,state,city,contact_no from showroom,vehicle where showroom.s_id = vehicle.s_id and v_name = '{0}'".format(name))
        rows = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [rows,col])
    else:
        return render_template("vehiclename.html")

@app.route("/queriesemp/serviecenter",methods = ['GET','POST'])
def eq6():
    if request.method == 'POST':
        loc = request.form['loc']
        cur.execute("select s_id,location,contact_no from showroom where location like '%{0}%'".format(loc))
        res2 = cur.fetchall()
        col = [desc[0] for desc in cur.description]
        return render_template('view.html',content = [res2,col])
    else:
        return render_template("location.html")


if __name__ == "__main__":
    app.run(debug=True)

cur.close()
con.close()

