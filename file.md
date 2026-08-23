
##  **프로그램 실행 스크린샷**

- **메뉴 화면**<br>
  <img width="495" height="191" alt="image" src="https://github.com/user-attachments/assets/7580117e-89f5-4691-aeca-dd7d72d10aad" />

- **프롬프트 추가**<br>
  <img width="597" height="245" alt="image" src="https://github.com/user-attachments/assets/aca674f5-227f-4f94-b243-c7f8b39adc92" />

- **프롬프트 목록**<br>
  <img width="377" height="135" alt="image" src="https://github.com/user-attachments/assets/1630a1e4-72f4-4fb3-a4c8-940435a2211e" />

- **카테고리별 조회**<br>
  <img width="324" height="255" alt="image" src="https://github.com/user-attachments/assets/31bdb60b-2060-4a6c-8c34-c25c3cfa467f" />

- **프롬프트 검색**<br>
  <img width="385" height="112" alt="image" src="https://github.com/user-attachments/assets/5ae079b8-0bf4-4545-9e2f-4b9fa262cdaa" />

- **프롬프트 상세 보기**<br>
  <img width="588" height="266" alt="image" src="https://github.com/user-attachments/assets/ed14401f-b872-4f5d-a01c-b92ed4c1629b" />

- **즐겨찾기 관리**<br>
  <img width="452" height="78" alt="image" src="https://github.com/user-attachments/assets/7a80a026-3345-4780-a194-9fadf17c73c6" />

- **즐겨찾기 목록**<br>
  <img width="411" height="124" alt="image" src="https://github.com/user-attachments/assets/55e9aa17-04d6-4693-bf94-2e408bc34c95" />

## **데이터 구조**
```text
prompts = [
    {
        "title": "SEO 최적화 블로그 글 작성",
        "content": "다음 요소를 반영하여 블로그 글을 작성해줘.\n- 서론-본론-결론 구조\n- 3개 이상의 소제목(마크다운 헤딩) 구성\n- 결론부 CTA(행동유도) 강조\n- 충분한 본문 분량 확보",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "인스타그램 피드용 이미지 생성",
        "content": "인스타그램 피드에서 시선을 끄는 이미지를 생성해줘.\n- 비율: 4:5 세로형 (1080 x 1350)\n- 특징: 감성적이고 세련된 분위기\n- 강한 시각적 계층(Visual Hierarchy) 및 명확한 핵심 피사체",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 기획자 요구사항 문서(PRD) 작성",
        "content": "너는 10년 차 IT 서비스 기획자야. 회의록을 분석해 개발자와 QA가 바로 활용할 수 있는 요구사항 문서(PRD)를 작성해줘.\n[출력 규칙]\n1. 마크다운 제목과 불릿 사용\n2. 간결하고 구체적인 실무 문서 스타일\n3. 동일한 내용 반복 금지",
        "category": "페르소나",
        "favorite": True
    }
]
```






**git log --oneline --graph 결과 스크린샷**

<img width="593" height="358" alt="image" src="https://github.com/user-attachments/assets/cf150269-ee72-4523-9177-087443cab37e" />
