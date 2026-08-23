# 브랜치 생성!
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "SEO에 최적화된 블로그 글을 써줘.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 홍보 이미지 생성",
        "content": "세련된 느낌의 제품 사진을 그려줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "파이썬 코드 리뷰어",
        "content": "이 코드의 효율성을 점검해줘.",
        "category": "기타",
        "favorite": False
    }
]
# 브랜치 테스트
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
    category = input("카테고리를 입력하세요 (예: 텍스트 생성, 이미지 생성, 기타): ")

    # 2. 입력값 검증 (제목이나 내용을 안 적었을 경우 방지)
    if not title or not content:
        print("경고: 제목과 내용은 필수 입력 사항입니다. 추가가 취소되었습니다.")
        return  # 함수를 여기서 종료합니다.

    # 3. 새로운 딕셔너리 만들기
    new_prompt = {
        "title": title,
        "content": content,
        "category": category if category else "기타",  # 카테고리를 안 적으면 '기타'로 설정
        "favorite": False  # 새로 추가한 건 기본적으로 즐겨찾기 해제 상태
    }

    # 4. 기존 리스트에 추가하기
    prompts.append(new_prompt)
    print(f"✅ '{title}' 프롬프트가 성공적으로 추가되었습니다!")

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

    # 1. 찾고 싶은 카테고리 입력받기
    search_category = input("조회할 카테고리를 입력하세요 (예: 텍스트 생성, 번역): ")
    
    found = False  # 일치하는 항목을 찾았는지 기억하는 변수(깃발 역할)

    # 2. 전체 프롬프트를 하나씩 확인하기
    for i, p in enumerate(prompts):
        if p["category"] == search_category:  # 카테고리가 일치하면
            fav_icon = "⭐" if p["favorite"] else ""
            # i + 1을 해서 원본 목록과 똑같은 번호를 보여줍니다.
            print(f"{i + 1}. [{p['category']}] {p['title']} {fav_icon}")
            found = True  # 찾았다고 깃발을 듭니다!

    # 3. 다 뒤졌는데도 못 찾았을 경우
    if not found:
        print(f"경고: '{search_category}' 카테고리에 해당하는 프롬프트가 없습니다.")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 1. 검색할 단어 입력받기
    keyword = input("검색어를 입력하세요: ")
    
    found = False  # 검색 결과가 있는지 확인하는 깃발

    # 2. 전체 프롬프트를 하나씩 확인하기
    for i, p in enumerate(prompts):
        # 핵심! keyword가 제목(title)에 있거나(or) 내용(content)에 있으면 True
        if keyword in p["title"] or keyword in p["content"]:
            fav_icon = "⭐" if p["favorite"] else ""
            print(f"{i + 1}. [{p['category']}] {p['title']} {fav_icon}")
            found = True  # 찾았다고 깃발 들기!

    # 3. 검색 결과가 없을 경우
    if not found:
        print(f"경고: '{keyword}'(이)가 포함된 프롬프트를 찾을 수 없습니다.")

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

def main():
    while True:
        print("\n[ 메뉴를 선택하세요 ]")
        print("1. 목록 보기")
        print("2. 프롬프트추가")
        print("3. 상세보기")
        print("4. 카테고리별 조회")
        print("5. 검색")
        print("6. 즐겨찾기 설정/해제")
        print("7. 종료")
        
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
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# 실행 테스트
if __name__ == "__main__":
    main()
