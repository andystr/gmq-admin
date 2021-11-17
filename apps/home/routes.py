# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps import db
from apps.home import blueprint
from apps.home.models import vehiculo
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        #Accede a la base de datos de acuerdo a la ruta
        
        if template == 'vehiculos.html':
            vehiculos = db.session.query(vehiculo)
            return render_template("home/" + template, segment=segment, vehiculos=vehiculos)            
        elif template == 'contactos.html':
            return render_template("home/" + template, segment=segment)
        elif template == 'transacciones.html':
            return render_template("home/" + template, segment=segment)
        else:
            return render_template("home/" + template, segment=segment)
        
        # Serve the file (if exists) from app/templates/home/FILE.html
        #return render_template("home/" + template, segment=segment + complementos)
        

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None



