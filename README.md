<!--
 @since 2023.07.18, 22:23
 @changed 2023.07.18, 22:23
-->

# Sample tg bot


## Build info (auto-generated)

- Version: 0.0.1
- Last changes timestamp: 2023.07.18, 22:23
- Last changes timetag: 230718-2223


## TODO

Describe used techologies & their relations.


## Install

Install all required node dependencies:

```
npm i
```

Initialize python virtual environment:

```
sh utils/venv-init.sh
```


## Start dev server

Acivate virtual environment:

On windows:

```
call .venv/Scripts/activate
```

On unix:

```
. ./.venv/Scripts/activate
```

Start local flask server (can be located in browser with `http://localhost:5000/*`, but mostly using for api requests):

```
npm run start
```

Or just:

```
flask run
```


## API

Basic api structure:

TODO: Describe api here (for specific server version)


## Server urls

Remote server: `https://tournament-game-build.march.team/` (with built app)

Use local flask server instance for local nextjs server development.


## Server

Server runs on python/flask platform.

TODO: Describe basic server functionality.


## Python venv maintenance

Server command for creating venv:

```
virtualenv -p python3 ~/.venv-py3.10-flask
source ~/.venv-py3.10-flask/bin/activate
pip install -r requirements.txt
```

Local script for venv creating and initialization:

```
sh utils/util-venv-init.sh
```

Local command for activate venv:

```
call .venv/Scripts/activate
source .venv/Scripts/activate
```


## Python dependencies

```
pip install PKGNAME
pip install -r requirements-general.txt -r requirements-dev-only.txt
```

To freeze requirements use:

```
pip freeze > requirements-frozen.txt
```

Use `utils/venv-init.*` scripts to initialize virtual environment.
