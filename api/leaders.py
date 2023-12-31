from flask import Blueprint
from typing import Dict, List
from database.statservice import get_rating_db

leaders_bp = Blueprint('leaders', __name__)


@leaders_bp.route('/leaders/<string:level>', methods=['get'])
def get_top_5_leaders(level: str = 'all') -> Dict[str, List[Dict[int, int]]]:
    top_5_users = get_rating_db(level)

    return {'level': level, 'leaders': top_5_users}
