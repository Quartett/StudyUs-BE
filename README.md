# Django_Final_Project 
# StudyUs
- 스터디원 모집 기능 및 실시간 채팅, 개인용 암기 카드 기능을 지원하는 웹 서비스입니다.

|Name|남영훈|오정배|윤재우|이수민|
|:-:|-|-|-|-|
| Profile  |-|-|-|-|
| Position |테크 리더 & Frontend & Backend Develop & CICD|팀장 & Frontend & Backend Develop & UIUX|Frontend & Backend Develop & UIUX|Frontend & Backend Develop & UIUX|
| GitHub |[Eric](https://github.com/Nam-Younghoon)|[OH_JUNGBAE](https://github.com/Alexmint001)|[bardnia](https://github.com/bardnia)|[su2minig](https://github.com/su2minig)|

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경 및 배포 링크](#2-개발-환경-및-배포-링크)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도](#4-요구사항-시각화,-데이터베이스-모델링(ERD),-배포-아키텍처-구성도)<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>
[9. 프로젝트 소감(어려웠던 점 & 배운 점)](#9-프로젝트-소감(어려웠던-점-&-배운-점))<br>
<br>

## 1. 목표와 기능
### 1.1 목표
#### 공부를 하려고 마음먹은 당신!
- 스터디에 들어가고 싶거나 모집하고 싶으신가요? 지금 당장 **StudyUs**로!
#### 스터디원과 소통하고 싶은 당신!
- **실시간 채팅** 기능을 통해 소통하며 스터디에 참여해 보아요!
#### 암기를 해야하는데 막막한 당신!
- **암기 플래시 카드** 기능을 이용해서 암기의 두려움을 없애 보아요!

### 1.2 기능
- 신규 스터디 모집  및 기존 스터디 가입
- 실시간 채팅
- 암기용 플래시 카드

<br>

## 2. 개발 환경 및 배포 링크

### 2.1 개발 기술
#### [FrontEnd]  
<div>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
    <img src="https://img.shields.io/badge/Bootstrapap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/>
</div>

#### [BackEnd]
<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
    <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>
</div>

#### [DataBase]
<div>
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
</div>

### 2.2 개발 환경 및 버전 관리
<div>
    <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</div>


<br>

### 2.2 배포 Link<br>
[StudyUs](#)
<details>
<summary>테스트용 ID 및 PW</summary>
<div markdown="1">
ID : 아이디<br>
PW : 비밀번호
</div>
</details>

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조

<br>

### 3.2 API 명세서
- accounts

    |App|URL|HTTP Method|HTML File Name|Note|Login|
    |:-:|:-|:-:|:-|:-:|:-:|
    |accounts|join/|POST|join.html|회원가입|-|
    |accounts|login/|POST|login.html|로그인|-|
    |accounts|user/|GET|profile.html|프로필 조회|O|
    |accounts|user/|PATCH|profile_edit.html|프로필 수정|O|
    |accounts|user/delete/|DELETE|-|회원 탈퇴|O|
    |accounts|token/verify/|POST|-|토큰 유효성 검증|O|
    |accounts|token/refresh/|POST|-|토큰 재발급|O|
    |accounts|account-confirm-email/|POST|-|인증 메일 발송|-|
    |accounts|account-confirm-email/{key}/|GET|-|이메일 인증|-|
    |accounts|resend-email/|POST|-|인증 메일 재발송|-|
    |accounts|password/change/|POST|change_password.html|비밀번호 변경|O|

- study

    |App|URL|HTTP Method|HTML File Name|Note|Login|Author|Member|
    |:-:|:-|:-:|:-|:-:|:-:|:-:|:-:|
    |study|create/|POST|studygroup_create.html|스터디그룹 생성|O|-|-|
    |study|join/|POST|-|스터디그룹 참가|O|-|-|
    |study|/|GET|index.html|스터디그룹 리스트 조회|-|-|-|
    |study|{id}/|GET|studygroup_detail.html|스터디그룹 상세 조회|-|-|-|
    |study|{id}/update/|PATCH|studygroup_edit.html|스터디그룹 수정|O|O|O|
    |study|{id}/delete/|DELETE|-|스터디 그룹 삭제|O|O|O|
    |study|{id}/member/|GET|-|스터디그룹 멤버 리스트 조회|-|-|-|
    |study|{id}/member/delete/|DELETE|-|스터디그룹 탈퇴|O|-|O|
    |study|{id}/member/update/|PATCH|-|스터디그룹 그룹장 위임|O|O|O|
    |study|{id}/comments/|POST|-|댓글 작성|O|-|-|
    |study|{id}/comments/|GET|-|댓글 리스트 조회|-|-|-|
    |study|{id}/comments/{id}/update/|PATCH|-|댓글 수정|O|O|-|
    |study|{id}/comments/{id}/delete/|DELETE|-|댓글 삭제|O|O|-|

- memorycard

    |App|URL|HTTP Method|HTML File Name|Note|Login|
    |:-:|:-|:-:|:-:|:-|:-:|
    |memorycard|/|GET|memorycard.html|암기 카드 전체 리스트 조회|O|
    |memorycard|/|POST|-|암기 카드 생성|O|
    |memorycard|{id}/|GET|memorycard_detail.html|암기 카드 상세 내역 조회|O|
    |memorycard|{id}/|PATCH|-|암기 카드 수정|O|
    |memorycard|{id}/|DELETE|-|암기 카드 삭제|O|
    |memorycard|subject/|GET|subject.html|암기 카드 주제 리스트 조회|O|
    |memorycard|subject/|POST|-|암기 카드 주제 리스트 생성|O|
    |memorycard|subject/{id}/|GET|-|암기 카드 주제 상세 조회|O|
    |memorycard|subject/{id}/|DELETE|-|암기 카드 주제 삭제|O|

### 3.3 개발 일정

<div align="center">
<img width="800" alt="NotionTimeline" src=""><br>
- 타임라인 - 이미지 수정 필요<br>
<br>

<img width="800" alt="WBS" src=""><br>
[WBS 스프레드시트](#)
이미지 수정 및 링크 수정 필요
</div>
<br>

## 4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도

<div align="center">
<img width="800" alt="MindMap" src=""><br>
    - 기능 요구사항(마인드맵) - 이미지 수정 필요<br>
<br>

<img width="800" alt="FlowChart" src=""><br>
    - 플로우 차트 - 이미지 수정 필요<br>
<br>

<img width="800" alt="ERD" src=""><br>
    - 데이터베이스 모델링(ERD 설계) - 이미지 수정 필요<br>
<br>

<img width="800" alt="architecture" src=""><br>
    - 배포 아키텍처 구성도 - 이미지 수정 필요<br>
<br>
</div>
<br>

## 5. UI

### 5.1. 와이어프레임
<div align="center">
<img width="100%" alt="image" src="">
이미지 수정 필요
</div>

### 5.2. 실제 UI
- GitHub Link : [StudyUs-FE](https://github.com/Quartett/StudyUs-FE)

## 6. 메인 기능

<br>

## 7. 추가 기능
    
<br>

## 8. 개발하며 경험한 오류와 해결방법

<br>

## 9. 프로젝트 소감(어려웠던 점 & 배운 점)