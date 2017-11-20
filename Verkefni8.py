import bottle
from bottle import route, run, error, request, post, response, app, template
from beaker.middleware import SessionMiddleware
#Bryngeir Ari & Páll Gunnar
#16.10.17
# Muna að fara í File->settings->project:verkefni8->project interpreter->og installa beaker

#Vorum ekki að fatta þetta almennilega

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route('/')#heimasíðan
def index():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    bryngeir=' %d' % s["test"]
    return template(""" 
         <!DOCTYPE html>
        <html>
            <head>
                <title>Vefverslun Valgeirs</title>
                <meta charset="utf-8">
            </head>
        <body>
        <form method="post" action="/saveList">
           <h2>Vörur</h2><br>
            <h4>Heimsóknir : {{bryngeir}} </h4>
            <input type='checkbox' name='verd' value='Epli'>Epli frá Gansu <br>
            <input type='checkbox' name='verd' value='Mus'>Mús frá Kongó<br>
            <input type='checkbox' name='verd' value='Almanak'>Almanak<br>
            <input type='checkbox' name='verd' value='vefsida'>vefsíðu<br>
            <input type="submit" name="submit" value="Karfa">
            </fieldset>
        </body>
        </html>
    """,

    bryngeir=bryngeir)
@route('/saveList', method='post')
def save_list():
    forms = request.forms.getall('verd')

    staerd=0
    if len(forms) ==1:
       staerd = 1200
    if len(forms)==2:
        staerd = 2400
    if len(forms)==3:
        staerd = 3600
    if len(forms)==4:
        staerd=4800

    Allen=staerd+1200

    return template(""" 
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Vefverslun Valgeirs</title>
                    <link rel='stylesheet' href='/static/styles.css'>
                    <meta charset="utf-8">
                </head>
            <body>
            <h2>Pöntun:</h2>
            <h4>Þú valdir : {{forms}}</h4>
            <h4>Heildarverð: {{Allen}}</h4>
            <form action ='/takkfyrir'>
                <input type='submit' name='Kaupa' value='Kaupa'>
            </form>
            <form action='/'>
                <input type='submit' name='Til baka' value='Til baka'>
            </form>
            </body>
            </html
            """,

    forms=forms, Staerd=staerd, Allen=Allen)

@route('/takkfyrir')
def takk():
    return"""
    <title>Vefverslun Valgeirs</title>
    <h1>Takk fyrir að versla hjá okkur</h1>
    """

    


run(host='localhost', port=8080, debug=True, reloader=True, app=app)  # keyrir server


