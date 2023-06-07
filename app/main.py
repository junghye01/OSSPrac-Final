from flask import Flask, redirect,render_template,request

app=Flask(__name__)

#data=dict()
data_list=[]

@app.route('/',methods=['GET'])
def student():
    
    return render_template('main.html')


@app.route('/submit',methods=['POST'])
def submit():
    data=list()
    data.append(request.form.get('name'))
    data.append(request.form.get('StudentNumber'))
    data.append(request.form.get('major'))
    data.append(request.form.get('email_id')+'@'+request.form.get('email_addr'))
    data.append(request.form.get('Gender'))
    

    
    lst=['Python','Java','HTML','C++']

    lst2=[]

    for x in lst:
        if request.form.get(x):
            lst2.append(x)
    programming=','.join(lst2)
    data.append(programming)

    data_list.append(data)
    data_list.sort(key=lambda x: x[1])
    
    print('add row한 후',data_list)
    return redirect('/result')
   


@app.route('/result',methods=['GET','POST'])
def result():
    
    if request.method=='POST':
        if request.form.get('action')=='reset':
            data_list.clear()
           # print('초기화 됨 ')
           # print('초기화된후',data_list)
            return redirect('/')
        else:

        
            for x in data_list:
                if request.form.get(x[1]):
                    
                    data_list.remove(x)
                    print('삭제된후',data_list)
            return render_template('result.html',result=data_list)
    else:
        return render_template('result.html', result=data_list)
   

    
                



if __name__=='__main__':
    app.run(debug=True)