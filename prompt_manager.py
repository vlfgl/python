# 기본 프롬프트 데이터
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

# 목록 보기 함수 정의
def show_list():
    print("=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        # 즐겨찾기 별표 표시
        fav_icon = "⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']} {fav_icon}")

    print(f"\n총 {len(prompts)}개의 프롬프트가 있습니다.")

def add_prompt():
    print("\n=== 새 프롬프트 추가 ===")
    
    # 1. 사용자에게 정보 입력받기
    title = input("제목을 입력하세요: ")
    content = input("내용을 입력하세요: ")

    # 2. 입력값 검증 (제목이나 내용을 안 적었을 경우 방지)
    if not title or not content:
        print("경고: 제목과 내용은 필수 입력 사항입니다. 추가가 취소되었습니다.")
        return  # 함수를 여기서 종료합니다.

    # 3. 카테고리 선택 기능 (새로 추가된 부분!)
    print("\n[카테고리 선택]")
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
        
    choice_str = input("번호를 선택하세요 (엔터 입력 시 '기타'로 설정됨): ")
    
    # 사용자가 올바른 숫자를 입력했는지 확인
    if choice_str.isdigit() and 1 <= int(choice_str) <= len(categories):
        category = categories[int(choice_str) - 1]
    else:
        category = "기타"  # 잘못된 번호나 빈칸을 입력하면 자동으로 '기타' 설정

    # 4. 새로운 딕셔너리 만들기
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False  # 새로 추가한 건 기본적으로 즐겨찾기 해제 상태
    }

    # 5. 기존 리스트에 추가하기
    prompts.append(new_prompt)
    print(f"✅ '{title}' 프롬프트가 [{category}] 카테고리에 성공적으로 추가되었습니다!")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 사용자에게 번호 입력받기
    num_str = input("상세히 볼 프롬프트 번호를 입력하세요: ")

    # 입력한 값이 숫자인지 확인 (.isdigit()은 숫자로만 이루어져 있으면 True를 반환)
    if num_str.isdigit():
        num = int(num_str) # 문자를 숫자로 변환
        
        # 입력한 번호가 실제 목록 범위 안에 있는지 확인
        if 1 <= num <= len(prompts):
            # 사용자는 1번부터 보지만, 파이썬 리스트는 0번부터 시작하므로 -1을 해줍니다!
            p = prompts[num - 1] 
            
            fav_icon = "⭐" if p["favorite"] else "" # 즐겨찾기가 아니면 빈 별 표시
            
            print("\n-----------------------------------")
            print(f"제목: {p['title']} {fav_icon}")
            print(f"카테고리: {p['category']}")
            print(f"내용:\n{p['content']}")
            print("-----------------------------------")
        else:
            print("경고: 목록에 없는 번호입니다.")
    else:
        print("경고: 숫자를 입력해주세요.")

def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 1. 고정된 카테고리 목록 보여주기
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
        
    # 2. 사용자에게 번호 입력받기
    choice_str = input("선택: ")

    if choice_str.isdigit():
        choice = int(choice_str)
        
        # 입력한 번호가 1~6 사이인지 확인
        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]
            print(f"\n[{selected_category}] 카테고리 프롬프트:")
            
            count = 0  # 찾은 개수를 세기 위한 변수
            
            for i, p in enumerate(prompts):
                if p["category"] == selected_category:
                    fav_icon = "⭐" if p["favorite"] else ""
                    print(f"{i + 1}. {p['title']} {fav_icon}")
                    count += 1
            
            # 3. 결과 출력 (개수 포함)
            if count == 0:
                print("해당 카테고리에 등록된 프롬프트가 없습니다.")
            else:
                print(f"\n총 {count}개의 프롬프트")
        else:
            print("경고: 목록에 있는 번호를 선택해주세요.")
    else:
        print("경고: 숫자를 입력해주세요.")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ")
    
    count = 0  # 검색된 개수를 세는 변수

    for i, p in enumerate(prompts):
        if keyword in p["title"] or keyword in p["content"]:
            fav_icon = "⭐" if p["favorite"] else ""
            print(f"{i + 1}. [{p['category']}] {p['title']} {fav_icon}")
            count += 1  # 찾을 때마다 1씩 증가

    # 검색 결과 출력
    if count == 0:
        print(f"경고: '{keyword}'(이)가 포함된 프롬프트를 찾을 수 없습니다.")
    else:
        print(f"\n총 {count}개의 프롬프트가 검색되었습니다.")

def toggle_favorite():
    print("\n=== 즐겨찾기 설정/해제 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 1. 번호 입력받기
    num_str = input("즐겨찾기 상태를 변경할 프롬프트 번호를 입력하세요: ")

    # 2. 입력값 검증 (숫자인지, 범위 안에 있는지 확인)
    if num_str.isdigit():
        num = int(num_str)
        
        if 1 <= num <= len(prompts):
            p = prompts[num - 1] 
            
            # 3. 핵심! 현재 상태를 반대로 뒤집기 (True -> False, False -> True)
            p["favorite"] = not p["favorite"]
            
            # 4. 결과 알려주기
            status = "설정" if p["favorite"] else "해제"
            print(f"✅ '{p['title']}' 프롬프트가 즐겨찾기에 {status}되었습니다!")
        else:
            print("경고: 목록에 없는 번호입니다.")
    else:
        print("경고: 숫자를 입력해주세요.")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    count = 0
    
    for i, p in enumerate(prompts):
        if p["favorite"]:  # 즐겨찾기가 True인 것만 출력
            print(f"{i + 1}. [{p['category']}] {p['title']} ⭐")
            count += 1

    if count == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 즐겨찾기 프롬프트가 있습니다.")

def main():
    while True:
        print("\n[ 메뉴를 선택하세요 ]")
        print("1. 프롬프트 목록")
        print("2. 프롬프트 추가")
        print("3. 프롬프트 상세보기")
        print("4. 카테고리별 조회")
        print("5. 프롬프트 검색")
        print("6. 즐겨찾기 설정/해제")
        print("7. 즐겨찾기 목록")
        print("8. 종료")
        
        choice = input("선택: ")

        if choice == "1":
            show_list() # 목록보기 
        elif choice == "2":
            add_prompt() # 프롬프트 추가 
        elif choice == "3":
            show_detail() # 상세보기 
        elif choice == "4":
            show_by_category() # 카테고리별 조회
        elif choice == "5":
            search_prompt() # 검색
        elif choice == "6":
            toggle_favorite() # 즐겨찾기 설정/해제
        elif choice == "7":
            show_favorites() # 즐겨찾기 목록
        elif choice == "8":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# 실행 테스트
if __name__ == "__main__":
    main()
