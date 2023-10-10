from flask import Flask,render_template,request
from text_summarization import summarizer
app =Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/summary',methods=['GET','POST'])
def summary():
  if request.method=='POST':
    Input_text=request.form['Input_text']
    summary,original_text,length_origin_text,length_summary_text=summarizer(Input_text)

  return render_template('summary.html',summary=summary,original_text=original_text,length_origin_text=length_origin_text,length_summary_text=length_summary_text)
if __name__=="__main__":
  app.run(debug=True)
