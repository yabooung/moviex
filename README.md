# README

## 관통프로젝트

#### 목표

- 영화 정보 기반 추천 서비스 구성
- 커뮤니티 서비스 구성
- HTML, CSS,, JavaScript. Vue.js Django, REST API, DataBase 등을 활용한 실제 서비스 설계
- 서비스 관리 및 유지보수

#### 개발환경

A. 언어

1.  Python 3.8+
2.  Django 3.x
3.  Node.js LTS
4.  Vue.js 2.x

B. 도구

1.  VSCode
2. Chrome Browser

C. 아키텍처
1. Django REST API 서버 & Vue.js

#### 서비스 개요

영화 정보를 활용한 웹 서비스

- TMDB API를 기반으로 영화정보를 제공
- 사용자에 평점에 따라 맞춤영화 서비스 제공
- 영화 평가 및 커뮤니티 기능을 통한 커뮤니케이션 제공

# 패치노트

! fixtures json loaddata 순서
  genre ,movie, people순


## 11/25

- vuetify 추가
- 스타일링

## 11/24

- 개별 영화 링크추가 기능 구현
- 버그 수정

## 11/23

- 댓글 수정, 삭제 기능 추가 -> 따로 페이지 이동할 필요 없이
- 비슷한 영화 추가
- 메인페이지 추천 영화 추가
- 영화 평가 기능 추가 -> 랜덤 영화를 보여주면 평점을 매기는 방식. 추천 영화 계산에 사용
- 게시판 조회수 추가
- 회원가입, 로그인 실패 시 에러메세지 추가
- 영화 추가 페이지 추가 - tmdb api 검색
- 유저 프로필 이미지 업로드 기능 추가

## 11/22

- 검색 키 추가
- 검색결과 페이지네이션 - 영화, 배우, 게시글 각각 페이지당 12, 12, 10개씩

## 11/20~21

- 자동완성기능 구현
- 다크모드 구현 시작

## 11/19

- 외부 api 사용 중이던 것들 내부 api 사용으로 바꿈
- 검색 기능 구현. 자동완성 구현 시작

## 11/18

- 게시판 기능 추가 - 글쓰기, 댓글 생성
- 메인페이지 인기 영화 목록 swiper 추가
- fuse.js를 통한 검색 기능 추가 시작
- JWT 토큰을 통한 인증 추가

## 11/17

- 로그인, 회원가입 기능 추가
- 게시판 기능 추가 중
- 에러 시 뜨는 페이지 따로 생성
- 데이터 베이스 전체 영화 조회 페이지, 영화 상세페이지 생성
- 장고와 연결 - 데이터 가져오기
- fixtures 데이터 생성
- 혹시 모를 상황 대비해서 성인 영화 거르도록 filter 이용
- bootstrap -> tailwind css로 변경
- vue-awesome-swiper 추가
- 메인 페이지 carousel로 변경

## 11 / 16

- 기본모델 구성
- Face 컴포넌트 구성
  - 메인 이미지 가져오기 - 상영작 중 인기작
- 인기 영화 가져오기

# 문제점 & 해결

- 영화 카드에 마우스를 올리면 영화 제목이 뜨도록 하는 것

  css hover 속성 사용. translate를 사용하여 더 자연스럽게 작동하도록 구현. 나중에 더 수정해야할 필요는 있음

- actions에서 router 사용. 영화 디테일로 가는 method가 여러 곳에서 쓰이다 보니 vuex의 actions에서 처리하려고 했는데, 작동을 안한다....

  간단히 router를 import 해주니 해결되었다.

- 어떤 css 프레임워크를 사용해야 할지?

  bootstrap, tailwind, bootstrap-vue 중 고민 중

  tailwind css -> 익숙한 bootstrap과 방법이 유사하면서 vs code에서 편의성이 매우 뛰어남. 생각한대로 커스터마이징이 자유로움.

- 영화 목록 이미지 크기 똑같이 맞추기

  carousel을 추가하니 이미지 크기가 다시 달라져 버렸던 문제.. swiper 쪽에서 너비와 높이쪽을 건드려서 그런 듯. object-fit: cover 가 작동을 안해서 한참 해멨는데, 찾아보니 이 설정은 너비와 높이 설정이 필요하다고 한다. 높이와 너비 100% 값을 줘서 해결.

- 뷰 라우터에서 같은 컴포넌트간 이동

  영화 디테일 페이지 -> 영화 디테일 페이지 인 경우 같은 컴포넌트를 사용하는데 라이프 사이클 훅이 달라서 데이터가 잘 불러와지지 않는 문제. 컴포넌트 재사용 시 생기는 `beforeRouteUpdate` 훅을 이용하였다.

- 유저 프로필 이미지 업로드

  `FormData` 인스턴스 생성 후 자료를 append 해주고, axios 요청 시 헤더에` 'Content-Type': 'multipart/form-data'` 를 넣어줘서 해결.

## i. 팀 정보

팀원 : 박종선 , 전건하

### 주 역할

박종선 :Backend / django

​	django를 바탕으로 서버 구축 및 알고리즘을 통한 맞춤 서비스 구현

전건하 : Frontend / Vue.js

​	Vue.js를 사용하여 사용자 경험을 향상시키는 웹 페이지 설계

공통 : 프로젝트 설계,  서비스 기획, 데이터베이스 모델 구현

## ii. 구현 기능

### 1. 영화

회원가입, 로그인, 로그아웃을 통해서 맞춤형 영화 추천 서비스를 제공

사용자간에 팔로우, 팔로잉 기능을 통해서 사용자 간의 커뮤니케이션 서비스 제공

게시판과 댓글을 통해 자유로운 소통가능

검색을 통해서 영화, 인물등의 정보를 제공

평점, 코멘트, 찜 기능을 통한 영화 서비스 제공

영화별로 영화내용과 관련된 정보를 제공

영화평가기능을 통해서 빠르고 간편하게 영화 평점 매기는 서비스 제공

사이트내 유저들의 영화 평가를 통해서 자체 영화평가지수 서비스 제공

![bandicam 2021-11-25 16-57-20-964](./README.assets/1.jpg)![bandicam 2021-11-25 16-57-56-628](README.assets/2.jpg)![bandicam 2021-11-25 16-57-31-246](README.assets/3.jpg)

![bandicam 2021-11-25 16-43-12-076](README.assets/4.jpg)![bandicam 2021-11-25 16-42-57-594](README.assets/5.jpg)![bandicam 2021-11-25 16-42-56-171](README.assets/6.jpg)

### 핵심기능

#### 랜덤영화 평가하기

사용자는 '영화평가' 기능을 활용해서 빠르고 간편하게 영화의 평점을 등록할 수있다.  평점등록, 넘어가기를 통해서 내가 선별적으로 영화의 평점을 등록할 수있고, 디테일 페이지를 통해서 영화의 줄거리를 확인할 수 있다.

#### 영화 DB 등록하기(관리자용)

관리자는 ADD페이지를 통해서 빠르고 편리하게 영화의 데이터베이스를 등록할 수있다.

### 2. 관리

관리자는 검색을 통해서 영화의 DB를 추가 할 수 있음![bandicam 2021-11-25 16-39-38-532](README.assets7.jpg)

![bandicam 2021-11-25 16-39-59-441](README.assets/8.jpg)

### 3. 프로필

프로필에서 사용자는 좋아하는 영화, 평가한 영화등의 목록을 제공 받음

팔로우 팔로잉 기능을 통해 다른 사용자와 커뮤니케이션 할 수 있음

팔로우 팔로잉 목록을 제공

이미지 등록을 통해 사용자의 개성을 표현할 수있음![bandicam 2021-11-25 16-59-38-013](README.assets/9.jpg)

![bandicam 2021-11-25 16-59-39-546](README.assets/10.jpg)

![bandicam 2021-11-25 16-59-43-439](README.assets/11.jpg)

![bandicam 2021-11-25 17-00-30-738](README.assets/12.jpg)

![bandicam 2021-11-25 17-00-34-517](README.assets/13.jpg)

![bandicam 2021-11-25 17-00-50-449](README.assets/14.jpg)

![bandicam 2021-11-25 17-00-56-803](README.assets/15.jpg)

### 4. 게시판

모든 회원은 게시판과 댓글을 통해 자유로운 소통이 가능

## iii. 데이터베이스 모델링

![project-db](README.assets/project-db.png)

## iv. 필수 기능에 대해 설명

### A. 관리자 뷰

admin페이지를 통해서 영화 추가 및 삭제 가능

![bandicam 2021-11-25 16-15-09-698](README.assets/16.jpg)

슈퍼유저와 일반유저가 분리되어 있음

### B. 영화 정보

데이터베이스를 통해 50개이상의 영화 목록 저장

모든 유저는 영화마다 평점을 등록하거나 수정, 삭제가 가능

### C. 추천 알고리즘

유저마다 평가한 영화를 기반으로 추천알고리즘을 생성

![bandicam 2021-11-25 16-40-09-733](README.assets/17.jpg)

#### 추천방식

자카드 유사도 - 아이템들의 교집합/합집합 값을 구해서 유사도를 측정  0~1사이의 값 중에 1의 값에 가까울수록 유사도가 높다는 것을 의미

영화마다 갖고 있는 장르를 통해서 영화간의 자카드 유사도를 구함.

ex) A 영화의 장르 (드라마, 코미디, 연애)

​	B 영화의 장르 (코미디, 액션)

이라면 두 영화의 자카드 유사도는 0.25가 됌

유저가 평가한 영화별로 1:N 비교를 통해 자카드 유사도를 구하고,  TMDB를 통해서 불러온 영화별 평점과 인기지수를 조합하여 영화별 추천지수 산출,

식) 자카드 유사도 * 유저 평점 * TMDB영화평점 + (인기지수)/1000

메인페이지에서 추천영화목록을 제공

### D. 커뮤니티

게시판, 댓글을 조회, 작성, 수정, 삭제 할 수있는 커뮤니티 기능 제공![bandicam 2021-11-25 16-40-19-778](README.assets/18.jpg)

작성자 본인만 본인 글을 수정/삭제 제공

댓글 작성및 수정/삭제 기능 제공![bandicam 2021-11-25 16-40-27-072](README.assets/19.jpg)

작성시간, 수정시간 정보 제공

### E. 기타

![bandicam 2021-11-25 16-40-54-581](README.assets/20.jpg)영화 평가 서비스 제공![bandicam 2021-11-25 16-40-58-423](README.assets/21.jpg)

## v. 기타

### 소감

#### 박종선

- 11-19 ~ 11.25  약 1주일간 영화 정보를 기반으로 영화 추천과 커뮤니티 기능을 제공하는 서비스를 구현하였다.

- 팀을 이루어서 하는 프로젝트라서 JIRA, GIT, FIGMA등의 협업툴을 사용해보았다.

- 실제 작업을 하면서 기획과 구조를 잘 짜는 것이 중요하다는 것을 느끼게 되었다.  작업을 하면서 생각한 것과 다른 부분이 많았고,  구조가 제대로 설계 되었더라면 더 신속하게 작업을 할 수 있었을 것이라고 생각한다.  

- 구현을 하면서 1학기 동안 배운 것을 다시 복습하고 익히는 시간이 되었다고 생각한다. 배웠던 내용들을 프로젝트를 진행하면서 적용했다.  잘 이해하지 못했던 부분이나 생소한 기능들이 실제로 서비스를 구현하는데 사용되는 것들이라는 것을 알게 되었다.

- 또 구상하고 설계했던 기능을 만들기 위해서 다양한 표현과 방법들을 생각하게 되었다. 프로젝트를 진행하는 1주일 동안 1학기 동안 배운 내용을 압축해서 다시 공부했다고 생각한다.

- 처음 진행하는 프로젝트였는데 이번 경험을 바탕으로 꾸준히 성장해야겠다.

#### 전건하

- 17일부터 대략 8~9일 정도 동안 만든 프로젝트였다. 처음엔 시간이 너무 짧다고 생각해서 큰 추가기능 없이 기본을 갖춘 프로젝트를 완성하는걸 목표로 했는데, 하다보니까 그러기에는 시간이 좀 많았다. 그래서 기획에 없던 몇몇 기능을 추가하게 되었는데, 덕분에 10일은 그리 긴 시간이 아니란걸 뼈저리게 느꼈다.
- vue를 다루는 건 익숙하지 않다보니 처음에 vuex와 vue router를 추가하긴 했는데, 처음엔 프로젝트가 깊이가 깊지 않다보니 vuex를 사용안하는게 편했었는데, 프로젝트가 기획보다 커지다보니 중복되는 코드들이 많아지고, vuex의 필요성이 느껴졌다. 지금은 시간이 부족해 코드 정리를 하지는 못했지만, 끝난 후에 코드도 정리해보고, 다음 프로젝트 때는 처음부터 고려해야겠다.
- 이번 프로젝트를 진행하면서 여러 라이브러리를 사용해봤는데, 확실히 어지간한 기능은 만들어져 있는게 많아서 편리했다. 다만 생각하지 못했던 버전 호환성 문제 등이 있어서 잘 알아보고 써야할 것 같다.
