# Presenter Draw Program
엔코아 플레이데이터 데이터 엔지니어링 파이널 프로젝트용 발표자 추첨 프로그램입니다.  
This program is made to draw a presenter for the Encore® PlayData Data Engineering final project.

## Dev
본 프로그램은 파이썬 3.12 환경에서 개발되었습니다. 아래 명령어 중 `docker pull python:3.12`는 선택 사항으로, 도커 허브에서 [파이썬 공식 도커 이미지](https://hub.docker.com/_/python)를 불러오기 때문에 빌드 과정에서 로컬 환경에 이미지가 없음을 감지하면 자동으로 이미지를 pull 해옵니다. 도커 컨테이너 실행 시 연동시킬 디렉토리가 없다면 `-v` 옵션에 해당하는 부분은 생략할 수 있습니다. 단, 이럴 경우 도커 환경에서 작성한 파이썬 스크립트 파일을 수동으로 로컬 환경으로 가져와야 합니다.    
This program is developed on Python 3.12 environment. Among the commands below, `docker pull python:3.12` is optional. As the docker hub fetches [the Python official docker image](https://hub.docker.com/_/python), it will pull the image automatically when the build detects that there is no image in the local environment. If you don't have a directory to bind with the Docker container, you can skip the `-v` option. However, in this case, you should manually bring your Python script file to your local environment.  
```Bash
$ docker pull python:3.12
$ docker run -it -v ~/code/presenterdraw:/app --name mypy312 python:3.12
$ docker exec -it mypy312 bash
$ cd app
```  
> **Note**  
도커 환경에서 Vim과 같은 에디터를 설치할 때 `apt-get` 기반의 명령어가 제대로 실행되지 않고 오류 메시지를 출력하거나 무의미한 실행 결과를 출력하는 경우가 있습니다. 이 경우는 우분투, 더 나아가서 사용자의 컴퓨터의 DNS 설정이 잘못 되어 있는 경우에 해당합니다. 따라서 이 경우 위 코드 블록의 명령어 중 두 번째 명령어를 아래와 같이 수정해서 실행하면 됩니다.  
When one try installing an editor such as Vim, it often doesn't work properly and print error message, or even shows meaningless result. In this case, a DNS configuration of Ubuntu (or, further, user's own computer) might not set correctly. Therefore, if this is your case, you can change the second line of the code block above like command below and run.  
```Bash
$ docker run -it --dns 8.8.8.8 -v ~/code/presenterdraw:/app --name mypy312 python:3.12
```
## Run the Script
```Bash
$ python draw_presenter.py
```
