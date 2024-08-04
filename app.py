from flask import Flask, render_template, request
from src.DataExtractionAndNLP.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.DataExtractionAndNLP.pipeline.stage_02_pre_cleaning import PreCleaningPipeline
from src.DataExtractionAndNLP.pipeline.stage_03_cleaning import CleaningPipeline
from src.DataExtractionAndNLP.pipeline.stage_04_post_cleaning import PostCleaningPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET']) # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/Extract&Analyse',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            url = request.form['url']
            Class_type = request.form['class_type']
            Class_name = request.form['class_name']

            data = [url, Class_type, Class_name]
            data[2]=data[2].replace(" ", ".")


            data_ingestion = DataIngestionPipeline()
            data_ingestion.main(data)
            pre_cleaning = PreCleaningPipeline()
            metrics = pre_cleaning.main(data)
            cleaning = CleaningPipeline()
            cleaning.main(data)
            post_cleaning = PostCleaningPipeline()
            metrics = post_cleaning.main(metrics, data)

            return render_template('results.html', metrics = metrics)
        except Exception as e:
            print('The Exception message is: ',e)
            return f'something is wrong, {e}'
    else:
        return render_template('index.html')
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug=True)
    # app.run(host="0.0.0.0", port= 8080)