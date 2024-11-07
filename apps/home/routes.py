# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import logging
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db  # Add this import for database connection
# Configure logging
logging.basicConfig(level=logging.DEBUG)


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

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

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


@blueprint.route('/data', methods=['GET'])
@login_required
def data():
    # Create a new database connection
    connection = db.engine.raw_connection()
    cursor = connection.cursor()

    # Example query to retrieve parentcontactidname, parentaccountidname, and emailaddress_y from 'sales' table
    query = "SELECT parentcontactidname, parentaccountidname, emailaddress_y FROM sales"
    cursor.execute(query)
    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('home/tables.html', customers=customers)

@blueprint.route('/product', methods=['GET'])
@login_required
def product():
    # Create a new database connection
    connection = db.engine.raw_connection()
    cursor = connection.cursor()

    # Example query to retrieve productname, priceperunit, and quantityopp from 'products' table
    query = "SELECT productname, priceperunit, quantityopp FROM sales"
    cursor.execute(query)
    products = cursor.fetchall()
        # Check if the data retrieval was successful
   

    cursor.close()
    connection.close()

    return render_template('home/map.html', products=products)

@blueprint.route('/customer/<string:customer_id>', methods=['GET'])
@login_required
def customer_details(customer_id):
    # Create a new database connection
    connection = db.engine.raw_connection()
    cursor = connection.cursor()

    # Example query to retrieve the desired customer details
    query = """
    SELECT parentcontactidname, emailaddress_y, mobilephone, address1_composite, postalcode, parentaccountidname, jobtitle
    FROM sales
    WHERE parentcontactidname = %s
    """
    cursor.execute(query, (customer_id,))
    customer_details = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template('home/typography.html', customer=customer_details)


