# Because we have __init__.py in website folder, we can import create_app 
# function from website folder because website is now a package.

from website import create_app

app = create_app()

if __name__ == '__main__': # only run app if this file is ran directly
    app.run(debug=True) # debug=True will automatically restart server when changes are made to code (would turn off in production)