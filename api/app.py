from flask import Flask, render_template


app = Flask(__name__, static_folder='static', static_url_path='')

###############################
############ MAIN #############
###############################

@app.route('/')
def index():
    return render_template('index.html')

###############################
############ ERROR ############
###############################

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template("404.html"), 404


# @app.errorhandler(500)
# def page_not_found(e):
# 	return render_template("500.html"), 500

# @app.route('/404')
# def error_404():
#     return render_template('404.html')

# @app.route('/500')
# def error_500():
#     return render_template('500.html')


###############################
######## RUN TIME CODE ########
###############################
if __name__ == "__main__":
    app.run(debug=True)