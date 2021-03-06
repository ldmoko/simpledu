from flask import abort, render_template
from flask_login import current_user
from functools import wraps
from simpledu.models import User


def role_required(role):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			if not current_user.is_authenticated or current_user.role < role:
				# abort(404)
				return render_template('404.html'), 404
			return func(*args, **kwargs)
		return wrapper
	return decorator


staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)
