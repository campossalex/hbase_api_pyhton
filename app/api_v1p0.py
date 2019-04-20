from flask import Blueprint, jsonify, request, g
from app import database
from app.exceptions import NotFoundException, NoJsonException
import happybase

blueprint = Blueprint(name='api_v1p0', import_name=__name__, url_prefix="/api/v1.0", template_folder='templates')


def validate_json(json):
    if not json or not hasattr(json, 'items'):
        raise NoJsonException()


@blueprint.route('/getEmp/<string:emp_id>', methods=['GET'])
def get_emp(emp_id):
    connection = happybase.Connection('localhost', transport='framed', protocol='compact')
    table = connection.table('emp_data')
    row = table.row(emp_id)
    if row is None:
        raise NotFoundException('Emp  %s not found' % emp_id)
    else:
        return jsonify(row)
