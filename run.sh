#!/usr/bin/bash
export FLASK_APP=init.py
export FLASK_DEBUG=1
export FLASK_BLOG_SECRET='fghfytdfuyfdjhdyhgkuguyjhik'
export FLASK_BLOG_DB_URL='sqlite:///../site.db'
flask run