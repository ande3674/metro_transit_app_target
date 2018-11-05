from flask import Flask, render_template, request
import api

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/search')
def search():
    route = request.args.get('route')
    direction = request.args.get('direction')
    stop = request.args.get('stop')
    # Get valid route ID
    route_id = api.get_route_id(route)
    # Get valid direction ID
    dir_id = api.get_direction_id(direction, route_id)
    # Get valid stop ID
    stop_id = api.get_stop_id(stop, route_id, dir_id)

    # Handle errors
    if route_id == -1 or dir_id == -1 or stop_id == -1:
        time = 'Invalid data, try again'
    # Get time
    else:
        time = api.get_time_to_next_bus(route_id, dir_id, stop_id)

    return render_template('search.html', route=route.title(), dir=direction, stop=stop.title(), time=time)


if __name__ == '__main__':
    app.run()
