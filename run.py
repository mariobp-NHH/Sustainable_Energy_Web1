from webse import app
from webse.users.utils import read_image

app.jinja_env.globals['func'] = read_image

if __name__ == '__main__':
    app.run(debug=True) 
  