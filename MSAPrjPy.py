from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_feedback():
    try:
        callback = request.args.get('callback')
    except:
        callback = ''
        pass
    if callback == '':
        return '[{"PropertyID":"NB00001","Feedback":101255,"Remark":"我是Python回发的一号","LastDate":"2017-01-01"},{"PropertyID":"NB00002","Feedback":101255,"Remark":"我是Python回发的二号","LastDate":"2017-01-01"},{"PropertyID":"NB00003","Feedback":101255,"Remark":"我是Python回发的三号","LastDate":"2017-01-01"}]'
    else:
        return callback+'([{"PropertyID":"NB00001","Feedback":101255,"Remark":"我是Python回发的一号","LastDate":"2017-01-01"},{"PropertyID":"NB00002","Feedback":101255,"Remark":"我是Python回发的二号","LastDate":"2017-01-01"},{"PropertyID":"NB00003","Feedback":101255,"Remark":"我是Python回发的三号","LastDate":"2017-01-01"}])'


if __name__ == '__main__':
    app.run()
