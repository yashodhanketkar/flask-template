import functools
import sys
from waitress import serve
from src import create_app


def server_handler(server):
    @functools.wraps(server)
    def wrapper(**kwargs):
        try:
            return server(**kwargs)

        except KeyboardInterrupt:
            print("Server closing gracefullly.")

        except Exception as err:
            print("Server closed due to ", err)

    return wrapper


@server_handler
def dev_server(app):
    app.run(debug=True, host="0.0.0.0", port="5000")


@server_handler
def prod_server(app):
    serve(app, host="0.0.0.0", port="5000")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit

    match sys.argv[1]:
        case "--dev" | "-d":
            dev_server(app=create_app())
        case "--prod" | "-p":
            prod_server(app=create_app())
        case _:
            raise
