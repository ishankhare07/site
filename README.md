# site
site implementing websockets using tornado and future implementation of mongodb

# installation
1. Clone with
  ```shell
  git clone git@github.com:ishankhare07/site.git
  git clone git@github.com:ishankhare07/website.git
  ```

2. Setup virtualenv and start server
  ```shell
  cd site/server;virtualenv venv; source venv/bin/activate; pip install -r requirements.txt
  python main.py    # start the websocket server process
  ```

3. Server webpage, open another terminal and navigate to `website directory`
  ```shell
  cd website/ws/; python -m SimpleHTTPServer   # start serving the web page
  ```

4. Open chat -> goto [http://localhost:8000/ws.html](http://localhost:8000/ws.html)
