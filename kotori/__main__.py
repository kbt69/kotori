import importlib
import kotori
import os

from bottle import route, run, response, static_file
from kotori import chat_url
from kotori.web_modules import ALL_MODULES

IMPORTED = {}
for module_name in ALL_MODULES:
	imported_module = importlib.import_module("kotori.web_modules." + module_name)
	if not hasattr(imported_module, "__mod_name__"):
		imported_module.__mod_name__ = imported_module.__name__

	if not imported_module.__mod_name__.lower() in IMPORTED:
		IMPORTED[imported_module.__mod_name__.lower()] = imported_module
	else:
		raise Exception("Can't have two modules with the same name! Please change one")

@route('/')
def index():
	response.status = 303
	response.set_header('Location', chat_url)

@route('/favicon.ico', method=["GET", "POST"])
def favicon():
	filename = "favicon.ico"
	return static_file(filename, root="img", download=filename)

print("----------------------------------------------------------------")
print(" Loaded Web Modules : ["+", ".join(ALL_MODULES)+"]")
print("----------------------------------------------------------------")
print()
print(" ---[Kotori Services is Running...]---")
print()
print(" Thanks for using my bot :)")
print()

if __name__ == "__main__":
	run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))