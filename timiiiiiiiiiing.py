from flask import Flask, url_for, request
import os

app = Flask(__name__)



@app.route('/carousel')
def load_photo():
    return f"""
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <title>Пейзажи марса</title>
  </head>
  <body>
    <h1 style="text-align: center;"><strong>Пейзажи марса</strong></h1>
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="item active" data-bs-interval="10">
          <p style="text-align: center;">
            <img src="{url_for('static', filename='img/mars.jpg')}" style="width: 50%;">
          </p>
        </div>
        <div class="item" data-bs-interval="10">
          <p style="text-align: center;">
            <img src="{url_for('static', filename='img/mars_1.jpg')}" style="width: 50%;">
          </p>
        </div>
        <div class="item" data-bs-interval="10">
          <p style="text-align: center;">
            <img src="{url_for('static', filename='img/mars_2.jpg')}" style="width: 50%;">
          </p>
        </div>
      </div>
      <a class="left carousel-control" href="#myCarousel" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </body>
</html>

        """



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
