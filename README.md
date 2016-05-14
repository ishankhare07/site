# site
site implementing websockets using tornado and future implementation of mongodb

# installation
1. Clone with
  ```shell
  git clone git@github.com:ishankhare07/site.git
  git submodule update --init --recursive
  ```

2. Setup virtualenv
  ```shell
  cd site/server;virtualenv venv; source venv/bin/activate; pip install -r requirements.txt
  ```

3. Start server
  ```shell
  python main.py    # start the websocket server process
  cd ../website/ws/; python -m SimpleHTTPServer   # start serving the web page
  ```

4. Open chat -> goto [http://localhost:8000/ws.html](http://localhost:8000/ws.html)
