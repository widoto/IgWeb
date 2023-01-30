# igboard 프로젝트

# 실행방법

1. 가상환경 만들기
    
    `python -m venv 가상환경이름`
    
2. 가상환경 실행하기
    
    `source 가상환경이름/bin/activate`
    
3. 가상환경에 설치
    
    `pip install django`
    
    `pip install django-summernote`
    
    `pip install mysqlclient`
    
    `pip install pillow`
    
    설치 목록 생성 확인
    
    `pip freeze`
    
4. 서버 시작
    
    `python manage.py runserver`

## Django-api Document

### 게시판
#### 게시글
1.board_list
- 요청방식 : get
- 기능 : 전체(과학자 + 일반인) 게시글 목록 보여줌 (제목, 작성자, 글 작성일)
- url : /board
```
{ 
    "title":"제목" ,
    "writer": "작성자",
    "write_dttm": "작성날짜",
 }
```
2. file_download
- 요청방식 : GET
- 기능 : 누르면 파일 다운로드
url : /board/public/download?path={{ board.file }}
- board.file : 파일 이름

#### 댓글
1. comments_create
- 요청방식 : POST
- 기능 : 댓글 생성
- url : /board/ public/detail/board_n/comments/
- board_n : 게시판 번호
```
{
    "content" : "댓글내용"
    "board" : "게시판 번호"
    "user" : "작성자"
    "create_at" : "작성날짜"
}
```
2. comments_delete
- 요청방식 : POST
- 기능 : 댓글 삭제
- url : /board/board_n/comments/comment_n/delete/
- board_n : 게시판 번호, comment_n : 댓글 번호
