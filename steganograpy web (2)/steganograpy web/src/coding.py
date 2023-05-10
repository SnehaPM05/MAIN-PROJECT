import os
from flask import *
from werkzeug.utils import secure_filename
from stegano import lsb
from src.dbconnection import *
import datetime
app=Flask(__name__)
app.secret_key="ouytr"

@app.route("/")
def log():
    return render_template("lognindex.html")


@app.route('/logincode',methods=['post'])
def logincode():
    un=request.form['textfield']
    ps=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(un,ps)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalied");window.location='/'</script>'''
    elif res['type']=="HR":
        return redirect('Homepage-HR.html')
    elif res['type']=="TL":
        session['lid']=res['lid']
        return redirect('Homepage-TL.html')

    elif res['type']=="TM":
        session['lid'] = res['lid']
        return redirect('Homepage-TM.html')
    else:
        return '''<script>alert("invalied");window.location='/'</script>'''


@app.route("/Add And manage TL.html")
def AddandmanageTL():
    q="SELECT * FROM `team_lead`"
    res=selectall(q)
    return render_template("Add And manage TL.html",val=res)

@app.route("/Add And manage TM.html")
def AddandmanageTM():
    q="SELECT * FROM `team_member` WHERE tid=%s"
    res=selectall2(q,session['lid'])
    return render_template("Add And manage TM.html",val=res)

@app.route("/Add And manage TM-2.html",methods=['post'])
def manageTM():
    return render_template("Add And manage TM-2.html",)
@app.route("/AddTM", methods=['post'])
def AddTM():
    FirstName=request.form["textfield"]
    LastName=request.form["textfield2"]
    Age=request.form["textfield3"]
    Email = request.form["textfield4"]
    Phone = request.form["textfield5"]
    UserName = request.form["textfield6"]
    Password = request.form["textfield7"]
    q="INSERT INTO `login` VALUES(NULL,%s,%s,'TM')"
    val=(UserName,Password)
    id=iud(q,val)
    qry3="INSERT INTO `team_member` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val3=(id,FirstName,LastName,Age,Email,Phone,session['lid'])
    iud(qry3,val3)
    return '"<script>alert("Added successfully!!");window.location=" Add And manage TM.html "</script>"'

@app.route("/edit_tm")
def edit_tm():
    id=request.args.get('id')
    session['ETM_id']=id
    qry="SELECT *  FROM `team_member` WHERE `lid`=%s"
    res=selectone(qry,id)
    return render_template("EDIT_TM.html",val=res)

@app.route("/edit_tm2", methods=['post'])
def edit_tm2():
    FirstName=request.form["textfield"]
    LastName=request.form["textfield2"]
    Age=request.form["textfield3"]
    Email = request.form["textfield4"]
    Phone = request.form["textfield5"]
    qry1="UPDATE `team_member` SET `Fname`=%s,`Lname`=%s,`age`=%s,`email`=%s,`phone`=%s WHERE `lid`=%s"
    val1=(FirstName,LastName,Age,Email,Phone,session['ETM_id'])
    iud(qry1,val1)
    return '"<script>alert("Edited successfully!!");window.location=" Add And manage TM.html "</script>"'

@app.route("/delete_TM")
def delete_TM():
    id=request.args.get('id')
    qry="DELETE FROM `team_member` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry1,id)
    return '"<script>alert("deleted successfully!!");window.location=" Add And manage TM.html "</script>"'

@app.route("/Add Work And assign TL-1.html")
def workassign():
    q1="SELECT * FROM `worktable` JOIN team_lead ON `worktable`.`teamlead`=`team_lead`.lid"
    res=selectall(q1)
    return render_template("Add Work And assign TL-1.html",val=res)

@app.route("/Add Work And assign TL-2.html",methods=['post'])
def assign():
    qry="SELECT * FROM `team_lead`"
    res=selectall(qry)
    return render_template("Add Work And assign TL-2.html",val=res)

@app.route("/Add_Work",methods=['post'])
def Add_Work():
    WorkType = request.form["textfield"]
    Image = request.files["file"]
    fn=secure_filename(Image.filename)
    Image.save(os.path.join('static/work',fn))
    TeamLead= request.form["select"]
    # Date=request.form["textfield4"]
    Date_to_be_completed= request.form["textfield5"]
    # Status=request.form["textfield6"]
    qry2 = "INSERT INTO worktable VALUES(NULL,%s,%s,%s,%s,curdate(),'pending')"
    val2 = (WorkType,fn,TeamLead,Date_to_be_completed)
    iud(qry2,val2)
    return '"<script>alert("Added successfully!!");window.location="/Add Work And assign TL-1.html "</script>"'


@app.route("/Allocate.html")
def allocate():
    id=request.args.get('id')
    session['W_ID']=id
    q="SELECT * FROM `team_member` WHERE `tid`=%s"
    res=selectall2(q,session['lid'])
    qry="SELECT * FROM `worktable` WHERE `teamlead`=%s"
    res1=selectall2(qry,session['lid'])
    return render_template("Allocate.html",val=res)


@app.route("/Allocate",methods=['post'])
def allocate1():
    id=request.args.get('id')
    tl=request.form['select2']
    worl=request.form['textfield']
    date=request.form['textfield2']
    qry="INSERT INTO `assign` VALUES(NULL,%s,%s,CURDATE(),%s,'pending',%s) "
    val=(session['W_ID'],tl,worl,date)
    iud(qry,val)
    return '"<script>alert("allocated successfully!!");window.location="/View Work and allocate to TM.html "</script>"'


@app.route("/Homepage-HR.html")
def homepagehr():
    return render_template("Homepage-HR.html")

@app.route("/Homepage-TL.html")
def homepageTL():
    return render_template("Homepage-TL.html")

@app.route("/Homepage-TM.html")
def homepageTM():
    return render_template("Homepage-TM.html")

@app.route("/Manage TL.html",methods=['post'])
def manageTL():
    return render_template("Manage TL.html")

@app.route("/Manage TL1.html",methods=['post'])
def manageTL1():
    FirstName=request.form["textfield"]
    LastName=request.form["textfield2"]
    Age=request.form["textfield3"]
    Email = request.form["textfield4"]
    Phone = request.form["textfield5"]
    UserName = request.form["textfield6"]
    Password = request.form["textfield7"]
    qry="INSERT INTO login VALUES(NULL,%s,%s,'TL')"
    val=(UserName,Password)
    id=iud(qry,val)
    qry1="INSERT INTO team_lead VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),FirstName,LastName,Age,Email,Phone)
    iud(qry1,val1)
    return '"<script>alert("Added successfully!!");window.location=" Add And manage TL.html "</script>"'

@app.route("/EDIT_TL1")
def EDIT_TL1():
    id=request.args.get('id')
    session['ETL_id']=id
    qry="SELECT * FROM `team_lead` WHERE `lid`=%s"
    res=selectone(qry,id)
    return render_template("TL_EDIT.html",val=res)

@app.route("/EDIT_TL2",methods=['post'])
def EDIT_TL2():
    FirstName=request.form["textfield"]
    LastName=request.form["textfield2"]
    Age=request.form["textfield3"]
    Email = request.form["textfield4"]
    Phone = request.form["textfield5"]
    qry1="UPDATE `team_lead` SET `Fname`=%s,`Lname`=%s,`age`=%s,`email`=%s,`phone`=%s WHERE `lid`=%s "
    val1=(FirstName,LastName,Age,Email,Phone,session['ETL_id'])
    iud(qry1,val1)
    return '"<script>alert("Edited successfully!!");window.location=" Add And manage TL.html "</script>"'

@app.route("/delete_TL")
def delete_TL():
    id=request.args.get('id')
    qry="DELETE FROM `team_lead` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry1,id)
    return '"<script>alert("deleted successfully!!");window.location=" Add And manage TL.html "</script>"'







@app.route("/Update daily report-TM.html")
def dailyreport():
    return render_template("Update daily report-TM.html")

@app.route("/UpdatereportTM",methods=['post'])
def UpdatereportTM():
    date = request.form['textfield']
    q= "SELECT * FROM `assign` JOIN `team_member`ON `team_member`.`lid`=`assign`.`tmid` WHERE `assign`.`date`=%s"
    res = selectall2(q, (date))
    return render_template("Update daily report-TM.html",val=res)

@app.route("/Update work Status.html")
def workstatus():
    return render_template("Update work Status.html")

@app.route("/UpdateworkStatus",methods=['post'])
def workstatus1():
    date=request.form['textfield']
    qry="SELECT * FROM `assign`  JOIN `worktable`ON `worktable`.`wid`=`assign`.`wid` WHERE worktable.`teamlead`=%s AND `assign`.`date`=%s"
    res=selectall2(qry,(session['lid'],date))
    return render_template("Update work Status.html",val=res)




@app.route("/view and update report-TL.html")
def report():
    return render_template("view and update report-TL.html")

@app.route("/viewreport",methods=['post'])
def viewreport():
    date=request.form['textfield']
    q="SELECT `assign`.`work`,`worktable`.`date`,`team_member`.`fname`,team_member.`lname`,assign.`status` FROM `assign`  JOIN `worktable`ON `worktable`.`wid`=`assign`.`wid`JOIN `team_member` ON `assign`.`tmid`=`team_member`.`lid` WHERE assign.`date`=%s"
    res=selectall2(q,date)
    return render_template("view and update report-TL.html",val=res)






@app.route('/updatework',methods=['get','post'])

def updatework():
    id=request.args.get('id')
    session['awid']=id
    return render_template("updatework.html")


@app.route('/updateworkkk',methods=['get','post'])
def updateworkkk():
    status=request.form['textfield']
    qry="UPDATE assign SET STATUS=%s WHERE aid=%s"
    val=(status,session['awid'])
    iud(qry,val)
    return '''<script>alert("updated");window.location="view Assigned work-TM.html#about"</script>'''



@app.route("/view Assigned work-TM.html")
def assignedwrk():

    q = "SELECT * FROM `assign` JOIN `team_member`ON `team_member`.`lid`=`assign`.`tmid`  JOIN `worktable` ON `assign`.wid=`worktable`.wid WHERE `assign`.`tmid`=%s "
    res = selectall2(q,session['lid'])
    print(res,"=====")

    for i in res:
        clear_message = lsb.reveal("static/work/" + i['image'])
        print(clear_message,"=====================")
        i['msg'] = clear_message


    return render_template("viewassign.html",val=res)

# @app.route("/viewwork",methods=['post'])
# def viewwork():
#     q = "SELECT  `assign`.`work`,`assign`.`date`,`assign`.`datetocom`,`team_member`.`fname`,`lname` FROM `team_member` WHERE `assign`.`tmid`=`team_member`.`tmid`"
#     res = selectall(q)
#     return render_template("view Assigned work-TM.html",val=res)

@app.route("/View completed Work.html")
def compltdwrk():
    q="SELECT * FROM `worktable` WHERE STATUS='completed'"
    res=selectall(q)
    return render_template("View completed Work.html",val=res)

@app.route("/View Ongoing WorkReport.html")
def ongoingwrk():
    qry1="select * from team_lead"
    res1=selectall(qry1)
    return render_template("View Ongoing WorkReport.html",val1=res1)


@app.route("/searchreport",methods=['post'])
def searchreport():
    date=request.form['select']
    qry1= "select * from team_lead"
    res1 = selectall(qry1)
    q="SELECT `report`.*,team_member.* FROM `report` JOIN `team_member` ON `report`.`lid`=`team_member`.`lid` WHERE `team_member`.`tid`=%s"
    res=selectall2(q,date)
    return render_template("View Ongoing WorkReport.html",val=res,val1=res1)



@app.route("/View Team-Member.html")
def viewtm():
    q="SELECT * FROM `team_member`"
    res=selectall(q)
    return render_template("View Team-Member.html",val=res)

@app.route("/View Work and allocate to TM.html")
def viewWrkandallocate():
    q="SELECT * FROM `worktable` WHERE `teamlead`=%s"
    res=selectall2(q,session['lid'])
    return render_template("View Work and allocate to TM.html",val=res)

@app.route("/status.html")
def status():
    id=request.args.get('id')
    session['aid']=id
    return render_template("statusedit.html")

@app.route("/status",methods=['post'])
def status1():
    status=request.form['textfield']
    qry="UPDATE `assign` SET `status`=%s WHERE `aid`=%s"
    iud(qry,(status,session['aid']))
    return '"<script>alert("updated successfully!!");window.location="Update work Status.html"</script>"'

@app.route("/workstatusTM.html")
def workstatusTM():
    return render_template("workstatusTM.html")

@app.route("/updatestatus",methods=['post'])
def updatestatus():
    date = request.form['textfield']
    q="SELECT * FROM `worktable` JOIN `team_lead` ON `team_lead`.`lid`=`worktable`.`teamlead` WHERE `worktable`.`date`=%s "
    val = date
    res=selectall2(q,val)
    return render_template("workstatusTM.html",val=res)

@app.route("/status11.html")
def status11():
    id=request.args.get('id')
    session['aid']=id
    return render_template("statuseditTM.html")

@app.route("/status22",methods=['post'])
def status22():
    status=request.form['textfield']
    qry="UPDATE `assign` SET `status`=%s WHERE `aid`=%s"
    iud(qry,(status,session['aid']))
    return '"<script>alert("updated successfully!!");window.location="Update daily report-TM.html"</script>"'




















@app.route('/addrep',methods=['get','post'])
def addrep():
    return render_template("addreport.html")

@app.route('/addrepp',methods=['get','post'])
def addrepp():
    title = request.form['textfield']
    qp = request.files['file']
    fname = secure_filename(qp.filename)
    qp.save('static/report/' + fname)
    qry = "insert into report values(null,%s,%s,%s,curdate())"
    val = (title,fname,session['lid'])
    iud(qry, val)
    return '''<script>alert("success");window.location="addrep#about"</script>'''

@app.route('/viewrep',methods=['get','post'])
def viewrep():
    qry="SELECT *FROM team_member"
    res=selectall(qry)
    return render_template("viewreport.html",val=res)


@app.route('/viewrepp',methods=['get','post'])
def viewrepp():
    name=request.form['select']
    qry="SELECT *FROM team_member"
    res=selectall(qry)
    qr="SELECT * FROM `report` WHERE lid=%s"
    v=(name)
    r=selectall2(qr,v)

    return render_template("viewreport.html",val=res,val1=r)






@app.route('/assignedworkviw',methods=['get','post'])
def assignedworkviw():
    qry="SELECT * FROM `worktable` WHERE teamlead=%s"
    res=selectall2(qry,session['lid'])
    return render_template("TLviewassign.html",val=res)





@app.route('/allocatetoteammember',methods=['get','post'])
def allocatetoteammember():
    id=request.args.get('id')
    session['wid']=id
    qry="SELECT * FROM team_member where tid=%s"
    res=selectall2(qry,session['lid'])
    return render_template("assignmember.html",val=res)

@app.route('/assignworkkkmember',methods=['get','post'])

def assignworkkkmember():
    fn=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    member=request.form['select2']
    workk = request.form['textfield']
    date = request.form['textfield2']
    # qp = request.files['file']
    qp = request.files['file']
    msg=request.form['msg']

    fname=fn+".png"
    qp.save("sample.png")
    qp = lsb.hide("sample.png",msg)
    qp.save('static/work/' + fname)
    qr="update worktable set status='Allocated' where wid=%s"
    iud(qr,session['wid'])
    qry="insert into assign values(null,%s,%s,curdate(),%s,'pending',%s,%s)"
    val=(session['wid'],member,workk,date,fname)
    iud(qry,val)
    return '''<script>alert("success");window.location="assignedworkviw#about"</script>'''






@app.route("/viewworkstatusmem")
def viewworkstatusmem():
    qry1="select * from team_member where tid=%s"
    res1=selectall2(qry1,session['lid'])
    return render_template("viewstatus.html",val1=res1)


@app.route("/searchstatus",methods=['post'])
def searchstatus():
    date=request.form['select']
    qry1= "select * from team_member where tid=%s"
    res1 = selectall2(qry1,session['lid'])
    q="SELECT assign.*,worktable.work_type FROM `worktable` JOIN `assign` ON worktable.wid=assign.wid WHERE assign.tmid=%s"
    res=selectall2(q,date)
    return render_template("viewstatus.html",val=res,val1=res1)





app.run(debug=True)