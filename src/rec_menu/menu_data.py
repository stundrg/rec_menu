from .models import Menu, MenuCategory


MENU_DATABASE = [
    # 한식
    Menu("김치찌개", MenuCategory.KOREAN, "저렴", 3, 15, ["따뜻한", "든든한"]),
    Menu("된장찌개", MenuCategory.KOREAN, "저렴", 1, 15, ["따뜻한", "건강한"]),
    Menu("비빔밥", MenuCategory.KOREAN, "보통", 1, 10, ["건강한", "든든한"]),
    Menu("불고기", MenuCategory.KOREAN, "비싸", 2, 20, ["든든한", "맛있는"]),
    Menu("삼겹살", MenuCategory.KOREAN, "비싸", 0, 25, ["든든한", "기름진"]),
    Menu("냉면", MenuCategory.KOREAN, "보통", 0, 10, ["시원한", "가벼운"]),
    Menu("갈비탕", MenuCategory.KOREAN, "비싸", 0, 30, ["따뜻한", "든든한"]),

    # 중식
    Menu("짜장면", MenuCategory.CHINESE, "저렴", 0, 15, ["든든한", "달콤한"]),
    Menu("짬뽕", MenuCategory.CHINESE, "저렴", 4, 15, ["따뜻한", "매운", "든든한"]),
    Menu("탕수육", MenuCategory.CHINESE, "보통", 0, 20, ["달콤한", "바삭한"]),
    Menu("마파두부", MenuCategory.CHINESE, "보통", 3, 15, ["매운", "따뜻한"]),
    Menu("볶음밥", MenuCategory.CHINESE, "저렴", 1, 10, ["든든한", "간단한"]),

    # 일식
    Menu("초밥", MenuCategory.JAPANESE, "비싸", 0, 20, ["신선한", "고급스러운"]),
    Menu("라멘", MenuCategory.JAPANESE, "보통", 2, 15, ["따뜻한", "든든한"]),
    Menu("돈까스", MenuCategory.JAPANESE, "보통", 0, 15, ["바삭한", "든든한"]),
    Menu("우동", MenuCategory.JAPANESE, "저렴", 0, 10, ["따뜻한", "가벼운"]),
    Menu("카레라이스", MenuCategory.JAPANESE, "보통", 1, 15, ["든든한", "부드러운"]),

    # 양식
    Menu("스테이크", MenuCategory.WESTERN, "비싸", 0, 25, ["고급스러운", "든든한"]),
    Menu("파스타", MenuCategory.WESTERN, "보통", 1, 15, ["든든한", "크리미한"]),
    Menu("피자", MenuCategory.WESTERN, "보통", 0, 20, ["든든한", "치즈가 많은"]),
    Menu("샐러드", MenuCategory.WESTERN, "보통", 0, 5, ["건강한", "가벼운", "시원한"]),
    Menu("리조또", MenuCategory.WESTERN, "보통", 0, 20, ["크리미한", "든든한"]),

    # 분식
    Menu("떡볶이", MenuCategory.SNACK, "저렴", 3, 10, ["매운", "따뜻한", "간식"]),
    Menu("김밥", MenuCategory.SNACK, "저렴", 0, 5, ["간단한", "가벼운"]),
    Menu("라면", MenuCategory.SNACK, "저렴", 2, 5, ["따뜻한", "간단한"]),
    Menu("순대", MenuCategory.SNACK, "저렴", 0, 10, ["든든한", "따뜻한"]),
    Menu("호떡", MenuCategory.SNACK, "저렴", 0, 10, ["달콤한", "따뜻한", "간식"]),

    # 패스트푸드
    Menu("햄버거", MenuCategory.FAST_FOOD, "보통", 0, 10, ["든든한", "빠른"]),
    Menu("치킨", MenuCategory.FAST_FOOD, "보통", 2, 15, ["바삭한", "든든한"]),
    Menu("감자튀김", MenuCategory.FAST_FOOD, "저렴", 0, 5, ["바삭한", "간식"]),
    Menu("핫도그", MenuCategory.FAST_FOOD, "저렴", 1, 5, ["간단한", "빠른"]),

    # 디저트
    Menu("아이스크림", MenuCategory.DESSERT, "저렴", 0, 2, ["시원한", "달콤한", "간식"]),
    Menu("케이크", MenuCategory.DESSERT, "보통", 0, 5, ["달콤한", "부드러운", "간식"]),
    Menu("커피", MenuCategory.DESSERT, "저렴", 0, 5, ["쓴맛", "따뜻한", "각성"]),
    Menu("빙수", MenuCategory.DESSERT, "보통", 0, 10, ["시원한", "달콤한", "간식"]),
]